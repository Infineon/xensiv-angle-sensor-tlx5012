# \file        TLE5012b.py
# \name        TLE5012b core library for the TLx5012B angle sensor family.
# \author      Infineon Technologies AG
# \copyright   2019-2024 Infineon Technologies AG
# \version     Version: 4.0.0
# \brief       GMR-based angle sensor for angular position sensing in automotive applications
#
# SPDX-License-Identifier: MIT

from spi3w import SPI3W
from tle5012b_reg import Reg


TRIGGER_DELAY              = 5         # @brief 5 microseconds trigger delay time
READ_SENSOR                = 0x8000    # @brief base command for read
WRITE_SENSOR               = 0x5000    # @brief base command for write
READ_BLOCK_CRC             = 0x8088    # @brief initialize block CRC check command
SYSTEM_ERROR_MASK          = 0x4000    # @brief System error masks for safety words
INTERFACE_ERROR_MASK       = 0x2000    # @brief Interface error masks for safety words
INV_ANGLE_ERROR_MASK       = 0x1000    # @brief Angle error masks for safety words
CRC_POLYNOMIAL             = 0x1D      # @brief values used for calculating the CRC
CRC_SEED                   = 0xFF      # @brief values used for calculating the CRC
CRC_NUM_REGISTERS          = 0x0008    # @brief number of CRC relevant registers
MAX_REGISTER_MEM           = 0x0030    # @brief max readable register values buffer
MAX_NUM_REG                = 0x16      # @brief defines the value for temporary data to read all readable registers
DELETE_BIT_15              = 0x7FFF    # @brief Value used to delete everything except the first 15 bits
CHANGE_UINT_TO_INT_15      = 0x8000    # @brief Value used to change unsigned 16bit integer into signed
CHECK_BIT_14               = 0x4000    # @brief Value used to check if the 14th bit is set
GET_BIT_14_4               = 0x7FF0    # @brief Value used to get the 14th to 4th bit
DELETE_7BITS               = 0x01FF    # @brief values used to calculate 9 bit signed integer sent by the sensor
CHANGE_UNIT_TO_INT_9       = 0x0200    # @brief Value used to change unsigned 9bit integer into signed
CHECK_BIT_9                = 0x0100    # @brief Value used to check if the 9th bit is set
POW_2_15                   = 32768.0   # @brief values used to for final calculations of angle speed, revolutions, range and value
POW_2_7                    = 128.0     # @brief values used to for final calculations of angle speed, revolutions, range and value
ANGLE_360_VAL              = 360.0     # @brief values used to for final calculations of angle speed, revolutions, range and value
TEMP_OFFSET                = 152.0     # @brief values used to calculate the temperature
TEMP_DIV                   = 2.776     # @brief values used to calculate the temperature

# @brief Error types from safety word
NO_ERROR                   = 0x00      # @brief NO_ERROR = Safety word was OK
SYSTEM_ERROR               = 0x01      # @brief SYSTEM_ERROR = over/under voltage, VDD negative, GND off, ROM defect
INTERFACE_ACCESS_ERROR     = 0x02      # @brief INTERFACE_ACCESS_ERROR = wrong address or wrong lock
INVALID_ANGLE_ERROR        = 0x03      # @brief INVALID_ANGLE_ERROR = NO_GMR_A = 1 or NO_GMR_XY = 1
ANGLE_SPEED_ERROR          = 0x04      # @brief ANGLE_SPEED_ERROR = combined error, angular speed calculation wrong
CRC_ERROR                  = 0xFF      # @brief CRC_ERROR = Cyclic Redundancy Check (CRC), which includes the STAT and RESP bits wrong

# @brief Set the UPDate bit high (read from update buffer) or low (read directly)
UPD_low                    = 0x0000    # @brief read normal registers
UPD_high                   = 0x0400    # @brief read update buffer registers

# @brief Switch on/off safety word generation
SAFE_low                   = 0x0000    # @brief switch of safety word generation
SAFE_high                  = 0x0001    # @brief switch on safety word generation

TLE5012B_S0                = 0x0000    # @brief TLE5012B_S0 default setting for only one sensor on the SPI
TLE5012B_S1                = 0x2000    # @brief TLE5012B_S1 second sensor needs also a second CS pin
TLE5012B_S2                = 0x4000    # @brief TLE5012B_S2 third sensor and ditto
TLE5012B_S3                = 0x6000    # @brief TLE5012B_S3 fourth sensor and ditto

def get_first_byte(two_byte_word):
    return (two_byte_word >> 8) & 0xFF

def get_second_byte(two_byte_word):
    return two_byte_word & 0xFF

def crc8(data, length):
    crc = CRC_SEED
    for i in range(length):
        crc ^= data[i]
        for bit in range(8):
            if (crc & 0x80) != 0:
                crc <<= 1
                crc ^= CRC_POLYNOMIAL
            else:
                crc <<= 1
    return (~crc) & CRC_SEED

def crc_calc(crc_data, length):
    return crc8(crc_data, length)

def calculate_angle_speed(ang_range, raw_angle_speed, fir_md, prediction_val):
    microsec_to_sec = 0.000001
    fir_md_val = {1: 42.7, 2: 85.3, 3: 170.6}.get(fir_md, 21.3)
    dividend = ang_range * raw_angle_speed / (POW_2_15 * microsec_to_sec)
    divisor = prediction_val * fir_md_val
    final_angle_speed = dividend / divisor
    return final_angle_speed

class Tle5012b:
    def __init__(self):
        self.safetyWord = 0
        self.mSlave = TLE5012B_S0
        self.SPI3W = SPI3W(0)
        self.Reg = Reg(self)

    def begin(self, miso='P9_1', mosi='P9_0', sck='P9_2', cs='P9_3', slaveNum=TLE5012B_S0):
        self.SPI3W.begin(miso, mosi, sck, cs)
        self.mSlave = slaveNum
        self.write_slave_number(self.mSlave)
        return self.read_block_crc()

    def read_from_sensor(self, command, upd, safe):
        self._command = [READ_SENSOR | command | upd | safe]
        _received = [0] * MAX_REGISTER_MEM
        self.SPI3W.send_receive(self._command, 1, _received, 2)
        data = _received[0]
        if safe == SAFE_high:
            check_error = self.check_safety(_received[1], self._command[0], _received, 1)
            if check_error != NO_ERROR:
                data = 0
        return check_error, data

    def read_more_registers(self, command, upd, safe):
        self._command = [READ_SENSOR | command | upd | safe]
        _received = [0] * MAX_REGISTER_MEM
        _rec_data_length = self._command[0] & 0x000F
        self.SPI3W.send_receive(self._command, 1, _received, _rec_data_length + safe)
        data = _received[:_rec_data_length]
        if safe == SAFE_high:
            check_error = self.check_safety(_received[_rec_data_length], self._command[0], _received, _rec_data_length)
            if check_error != NO_ERROR:
                data = 0
        return check_error, data

    def write_to_sensor(self, command, data_to_write, change_crc):
        self._command = [WRITE_SENSOR | command | SAFE_high, data_to_write]
        safety = 0
        self.SPI3W.send_receive(self._command, 2, [safety], 1)
        check_error = self.check_safety(safety, self._command[0], [self._command[1]], 1)
        if change_crc:
            check_error = self.regular_crc_update()
        return check_error

    def write_temp_coeff_update(self, data_to_write):
        safety = 0
        self.SPI3W.trigger_update()
        self._command = [WRITE_SENSOR | self.Reg.REG_TCO_Y | SAFE_high, data_to_write]
        self.SPI3W.send_receive(self._command, 2, [safety], 1)
        check_error = self.check_safety(safety, self._command[0], [self._command[1]], 1)
        check_error = self.read_status()
        if self.read_status() & 0x0008:
            check_error = self.regular_crc_update()
        return check_error

    def check_safety(self, safety, command, readreg, length):
        self.safetyWord = safety
        if not (safety & SYSTEM_ERROR_MASK):
            return SYSTEM_ERROR
        elif not (safety & INTERFACE_ERROR_MASK):
            return INTERFACE_ACCESS_ERROR
        elif not (safety & INV_ANGLE_ERROR_MASK):
            return INVALID_ANGLE_ERROR
        else:
            self.reset_safety()
            temp = [get_first_byte(command), get_second_byte(command)]
            for i in range(length):
                temp.extend([get_first_byte(readreg[i]), get_second_byte(readreg[i])])
            crc_received_final = get_second_byte(safety)
            crc = crc_calc(temp, length * 2 + 2)
            if crc == crc_received_final:
                return NO_ERROR
            else:
                self.reset_safety()
                return CRC_ERROR

    def reset_safety(self):
        command = READ_SENSOR + SAFE_high
        receive = [0] * 4
        self.SPI3W.trigger_update()
        self.SPI3W.send_receive([command], 1, receive, 3)

    def regular_crc_update(self):
        self.read_block_crc()
        temp = []
        for i in range(CRC_NUM_REGISTERS):
            temp.extend([get_first_byte(self._registers[i]), get_second_byte(self._registers[i])])
        crc = crc_calc(temp, 15)
        val_to_send = (temp[14] << 8) | crc
        self._registers[7] = val_to_send
        return self.write_temp_coeff_update(val_to_send)

    def read_block_crc(self):
        self._command = [READ_BLOCK_CRC]
        self._registers = [0] * (CRC_NUM_REGISTERS + 1)
        self.SPI3W.send_receive(self._command, 1, self._registers, CRC_NUM_REGISTERS + 1)
        check_error = self.check_safety(self._registers[8], READ_BLOCK_CRC, self._registers, CRC_NUM_REGISTERS)
        self.reset_safety()
        return check_error

    def read_status(self, upd=UPD_low, safe=SAFE_high):
        return self.read_from_sensor(self.Reg.REG_STAT, upd, safe)

    def read_activation_status(self, upd=UPD_low, safe=SAFE_high):
        return self.read_from_sensor(self.Reg.REG_ACSTAT, upd, safe)

    def read_sil(self):
        return self.read_from_sensor(self.Reg.REG_SIL, UPD_low, SAFE_high)

    def read_int_mode1(self):
        return self.read_from_sensor(self.Reg.REG_MOD_1, UPD_low, SAFE_high)

    def read_int_mode2(self):
        return self.read_from_sensor(self.Reg.REG_MOD_2, UPD_low, SAFE_high)

    def read_int_mode3(self):
        return self.read_from_sensor(self.Reg.REG_MOD_3, UPD_low, SAFE_high)

    def read_int_mode4(self):
        return self.read_from_sensor(self.Reg.REG_MOD_4, UPD_low, SAFE_high)

    def read_offset_x(self):
        return self.read_from_sensor(self.Reg.REG_OFFX, UPD_low, SAFE_high)

    def read_offset_y(self):
        return self.read_from_sensor(self.Reg.REG_OFFY, UPD_low, SAFE_high)

    def read_synch(self):
        return self.read_from_sensor(self.Reg.REG_SYNCH, UPD_low, SAFE_high)

    def read_ifab(self):
        return self.read_from_sensor(self.Reg.REG_IFAB, UPD_low, SAFE_high)

    def read_temp_coeff(self):
        return self.read_from_sensor(self.Reg.REG_TCO_Y, UPD_low, SAFE_high)

    def read_temp_dmag(self):
        return self.read_from_sensor(self.Reg.REG_D_MAG, UPD_low, SAFE_high)

    def read_temp_iif_cnt(self):
        return self.read_from_sensor(self.Reg.REG_IIF_CNT, UPD_low, SAFE_high)

    def read_temp_raw(self):
        return self.read_from_sensor(self.Reg.REG_T_RAW, UPD_low, SAFE_high)

    def read_temp_t25(self):
        return self.read_from_sensor(self.Reg.REG_T25O, UPD_low, SAFE_high)

    def read_raw_x(self):
        status, raw_data = self.read_from_sensor(self.Reg.REG_ADC_X)
        if status != NO_ERROR:
            return status, None
        return status, raw_data

    def read_raw_y(self):
        status, raw_data = self.read_from_sensor(self.Reg.REG_ADC_Y)
        if status != NO_ERROR:
            return status, None
        return status, raw_data

    def get_angle_value(self):
        return self.get_angle_value_with_params(UPD_low, SAFE_high)

    def get_angle_value_with_params(self, upd, safe):
        status, raw_data = self.read_from_sensor(self.Reg.REG_AVAL, upd, safe)
        if status != NO_ERROR:
            return status, None, None
        raw_data &= DELETE_BIT_15
        if raw_data & CHECK_BIT_14:
            raw_data -= CHANGE_UINT_TO_INT_15
        raw_angle_value = raw_data
        angle_value = (ANGLE_360_VAL / POW_2_15) * raw_angle_value
        return status, angle_value, raw_angle_value

    def get_temperature(self):
        return self.get_temperature_with_params(UPD_low, SAFE_high)

    def get_temperature_with_params(self, upd, safe):
        status, raw_data = self.read_from_sensor(self.Reg.REG_FSYNC, upd, safe)
        if status != NO_ERROR:
            return status, None, None
        raw_data &= DELETE_7BITS
        if raw_data & CHECK_BIT_9:
            raw_data -= CHANGE_UNIT_TO_INT_9
        raw_temp = raw_data
        temperature = (raw_temp + TEMP_OFFSET) / TEMP_DIV
        return status, temperature, raw_temp

    def get_num_revolutions(self, upd=UPD_low, safe=SAFE_high):
        status, raw_data = self.read_from_sensor(self.Reg.REG_AREV, upd, safe)
        if status != NO_ERROR:
            return status, None
        raw_data &= DELETE_7BITS
        if raw_data & CHECK_BIT_9:
            raw_data -= CHANGE_UNIT_TO_INT_9
        num_rev = raw_data
        return status, num_rev

    def get_angle_speed(self):
        return self.get_angle_speed_with_params(UPD_low, SAFE_high)

    def get_angle_speed_with_params(self, upd, safe):
        num_of_data = 0x7
        status, raw_data = self.read_more_registers(self.Reg.REG_ASPD + num_of_data, upd, safe)
        if status != NO_ERROR:
            return status, None, None
        raw_speed = raw_data[0] & DELETE_BIT_15
        if raw_speed & CHECK_BIT_14:
            raw_speed -= CHANGE_UINT_TO_INT_15
        fir_md = raw_data[3] >> 14
        int_mode2_prediction = 3 if raw_data[5] & 0x0004 else 2
        raw_angle_range = (raw_data[5] & GET_BIT_14_4) >> 4
        angle_range = ANGLE_360_VAL * (POW_2_7 / raw_angle_range)
        final_angle_speed = calculate_angle_speed(angle_range, raw_speed, fir_md, int_mode2_prediction)
        return status, final_angle_speed, raw_speed

    def get_angle_range(self):
        status, raw_data = self.read_int_mode2()
        if status != NO_ERROR:
            return status, None
        raw_data = (raw_data & GET_BIT_14_4) >> 4
        angle_range = ANGLE_360_VAL * (POW_2_7 / raw_data)
        return status, angle_range

    def write_int_mode2(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_MOD_2, data_to_write, True)

    def write_int_mode3(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_MOD_3, data_to_write, True)

    def write_offset_x(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_OFFX, data_to_write, True)

    def write_offset_y(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_OFFY, data_to_write, True)

    def write_synch(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_SYNCH, data_to_write, True)

    def write_ifab(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_IFAB, data_to_write, True)

    def write_int_mode4(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_MOD_4, data_to_write, True)

    def write_temp_coeff(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_TCO_Y, data_to_write, True)

    def write_activation_status(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_ACSTAT, data_to_write, False)

    def write_int_mode1(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_MOD_1, data_to_write, False)

    def write_sil(self, data_to_write):
        return self.write_to_sensor(self.Reg.REG_SIL, data_to_write, False)

    def write_slave_number(self, data_to_write):
        return self.write_to_sensor(WRITE_SENSOR, data_to_write, False)

    def read_reg_map(self):
        self.SPI3W.trigger_update()
        for i in range(MAX_NUM_REG):
            status = self.read_from_sensor(self.Reg.addrFields[i].regAddress, self.Reg.regMap[i], UPD_low, SAFE_high)
        return status

    def write_interface_type(self, iface):
        status, raw_data = self.read_int_mode4()
        if status != NO_ERROR:
            return status
        raw_data &= ~(1 << 0)
        raw_data &= ~(1 << 1)
        raw_data |= iface
        return self.write_int_mode4(raw_data)

    def set_calibration(self, cal_mode):
        status, raw_data = self.read_int_mode2()
        if status != NO_ERROR:
            return status
        raw_data &= ~(1 << 0)
        raw_data &= ~(1 << 1)
        raw_data |= cal_mode
        return self.write_int_mode2(raw_data)