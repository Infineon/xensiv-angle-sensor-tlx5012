# tle5012b_reg.py
# core registry definitions for the TLE5012B angle sensor.
# Author: Infineon Technologies AG
# Copyright: 2019-2024 Infineon Technologies AG
# Version: 4.0.0
# Brief: GMR-based angle sensor for angular position sensing in automotive applications
# SPDX-License-Identifier: MIT


class Reg:

    # Automatic calibration of offset and amplitude synchronicity for applications
    # with full-turn. Only 1 LSB corrected at each update. CRC check of calibration
    # registers is automatically disabled if AUTOCAL activated.
    noAutoCal = 0x0               # @brief noAutoCal = no auto-calibration
    mode1     = 0x1               # @brief mode1 update every angle update cycle (FIR_MD setting)
    mode2     = 0x2               # @brief mode2 update every 1.5 revolutions
    mode3     = 0x3               # @brief mode3 update every 11.25°

    factor1 = 0x080               # @brief magnetic angle from -180° to +180°, mapped values from -16384 to 16384
    factor4 = 0x200               # @brief magnetic angle from -45° to +45°, mapped values from -16384 to 16384
    factor5 = 0x040               # @brief magnetic angle from -180° to +180°, mapped values from -8192 to 8192


    # List of possible interface types witch are preset by fuses and can be changed into each other
    TLE5012B_E1000 = 0x01         # @brief TLE5012B_E1000 Sensor2Go variant
    TLE5012B_E3005 = 0x02         # @brief TLE5012B_E3005
    TLE5012B_E5000 = 0x03         # @brief TLE5012B_E5000 Sensor2Go variant
    TLE5012B_E5020 = 0x04         # @brief TLE5012B_E5020
    TLE5012B_E9000 = 0x05         # @brief TLE5012B_E9000 Sensor2Go variant

    # Registry access types
    REG_ACCESS_R    = 0x01        # @brief Read access register
    REG_ACCESS_W    = 0x02        # @brief Write access register
    REG_ACCESS_RW   = 0x03        # @brief Read & write access register
    REG_ACCESS_U    = 0x04        # @brief Update register
    REG_ACCESS_RU   = 0x05        # @brief Read & update register
    REG_ACCESS_RWU  = 0x07        # @brief Read & write & update register
    REG_ACCESS_RES  = 0x10        # @brief Reserved access register

    # Registry definitions
    REG_STAT         = 0x0000     # @brief STAT status register
    REG_ACSTAT       = 0x0010     # @brief ACSTAT activation status register
    REG_AVAL         = 0x0020     # @brief AVAL angle value register
    REG_ASPD         = 0x0030     # @brief ASPD angle speed register
    REG_AREV         = 0x0040     # @brief AREV angle revolution register
    REG_FSYNC        = 0x0050     # @brief FSYNC frame synchronization register
    REG_MOD_1        = 0x0060     # @brief MOD_1 interface mode1 register
    REG_SIL          = 0x0070     # @brief SIL register
    REG_MOD_2        = 0x0080     # @brief MOD_2 interface mode2 register
    REG_MOD_3        = 0x0090     # @brief MOD_3 interface mode3 register
    REG_OFFX         = 0x00A0     # @brief OFFX offset x
    REG_OFFY         = 0x00B0     # @brief OFFY offset y
    REG_SYNCH        = 0x00C0     # @brief SYNCH synchronicity
    REG_IFAB         = 0x00D0     # @brief IFAB register
    REG_MOD_4        = 0x00E0     # @brief MOD_4 interface mode4 register
    REG_TCO_Y        = 0x00F0     # @brief TCO_Y temperature coefficient register
    REG_ADC_X        = 0x0100     # @brief ADC_X ADC X-raw value
    REG_ADC_Y        = 0x0110     # @brief ADC_Y ADC Y-raw value
    REG_D_MAG        = 0x0140     # @brief D_MAG angle vector magnitude
    REG_T_RAW        = 0x0150     # @brief T_RAW temperature sensor raw-value
    REG_IIF_CNT      = 0x0200     # @brief IIF_CNT IIF counter value
    REG_T25O         = 0x0300     # @brief T25O temperature 25°c offset value

    # Registry position definitions
    REG_STAT_SRST                = 0x00
    REG_STAT_SWD                 = 0x01
    REG_STAT_SVR                 = 0x02
    REG_STAT_SFUSE               = 0x03
    REG_STAT_SDSPU               = 0x04
    REG_STAT_SOV                 = 0x05
    REG_STAT_SXYOL               = 0x06
    REG_STAT_SMAGOL              = 0x07
    REG_STAT_RESERVED            = 0x08
    REG_STAT_SADCT               = 0x09
    REG_STAT_SROM                = 0x0A
    REG_STAT_NOGMRXY             = 0x0B
    REG_STAT_NOGMRA              = 0x0C
    REG_STAT_SNR                 = 0x0D
    REG_STAT_RDST                = 0x0E

    REG_ACSTAT_ASRST             = 0x0F
    REG_ACSTAT_ASWD              = 0x10
    REG_ACSTAT_ASVR              = 0x11
    REG_ACSTAT_ASFUSE            = 0x12
    REG_ACSTAT_ASDSPU            = 0x13
    REG_ACSTAT_ASOV              = 0x14
    REG_ACSTAT_ASVECXY           = 0x15
    REG_ACSTAT_ASVEGMAG          = 0x16
    REG_ACSTAT_RESERVED1         = 0x17
    REG_ACSTAT_ASADCT            = 0x18
    REG_ACSTAT_ASFRST            = 0x19
    REG_ACSTAT_RESERVED2         = 0x1A

    REG_AVAL_ANGVAL             = 0x1B
    REG_AVAL_RDAV               = 0x1C

    REG_ASPD_ANGSPD             = 0x1D
    REG_ASPD_RDAS               = 0x1E

    REG_AREV_REVOL              = 0x1F
    REG_AREV_FCNT               = 0x20
    REG_AREV_RDREV              = 0x21

    REG_FSYNC_TEMPR             = 0x22
    REG_FSYNC_FSYNC             = 0x231

    REG_MOD_1_IIFMOD            = 0x24
    REG_MOD_1_DSPUHOLD          = 0x25
    REG_MOD_1_RESERVED1         = 0x26
    REG_MOD_1_CLKSEL            = 0x27
    REG_MOD_1_RESERVED2         = 0x28
    REG_MOD_1_FIRMD             = 0x29

    REG_SIL_ADCTVX              = 0x2A
    REG_SIL_ADCTVY              = 0x2B
    REG_SIL_ADCTVEN             = 0x2C
    REG_SIL_RESERVED1           = 0x2D
    REG_SIL_FUSEREL             = 0x2E
    REG_SIL_RESERVED2           = 0x2F
    REG_SIL_FILTINV             = 0x30
    REG_SIL_FILTPAR             = 0x31

    REG_MOD_2_AUTOCAL           = 0x32
    REG_MOD_2_PREDICT           = 0x33
    REG_MOD_2_ANGDIR            = 0x34
    REG_MOD_2_ANGRANGE          = 0x35
    REG_MOD_2_RESERVED1         = 0x36

    REG_MOD_3_PADDRV            = 0x37
    REG_MOD_3_SSCOD             = 0x38
    REG_MOD_3_SPIKEF            = 0x39
    REG_MOD_3_ANG_BASE          = 0x3A

    REG_OFFX_RESERVED1          = 0x3B
    REG_OFFX_XOFFSET            = 0x3C

    REG_OFFY_RESERVED1          = 0x3D
    REG_OFFY_YOFFSET            = 0x3E

    REG_SYNCH_RESERVED1         = 0x3F
    REG_SYNCH_SYNCH             = 0x40

    REG_IFAB_IFADHYST           = 0x41
    REG_IFAB_IFABOD             = 0x42
    REG_IFAB_FIRUDR             = 0x43
    REG_IFAB_ORTHO              = 0x44

    REG_MOD_4_IFMD              = 0x45
    REG_MOD_4_RESERVED1         = 0x46
    REG_MOD_4_IFABRES           = 0x47
    REG_MOD_4_HSMPLP            = 0x48
    REG_MOD_4_TCOXT             = 0x49

    REG_TCO_Y_CRCPAR            = 0x4A
    REG_TCO_Y_SBIST             = 0x4B
    REG_TCO_Y_TCOYT             = 0x4C

    REG_ADC_X_ADCX              = 0x4D

    REG_ADC_Y_ADCY              = 0x4E

    REG_D_MAG_MAG               = 0x4F
    REG_D_MAG_RESERVED1         = 0x50

    REG_T_RAW_TRAW              = 0x51
    REG_T_RAW_RESERVED1         = 0x52
    REG_T_RAW_TTGL              = 0x53

    REG_IIF_CNT_IIFCNT          = 0x54
    REG_IIF_CNT_RESERVED1       = 0x55

    REG_T25O_T250               = 0x56
    REG_T25O_RESERVED1          = 0x57



    # addrFields registry map
    addrFields = [
        (REG_STAT,     1    ),    # @brief STAT status register
        (REG_ACSTAT,   2    ),    # @brief ACSTAT activation status register
        (REG_AVAL,     3    ),    # @brief AVAL angle value register
        (REG_ASPD,     4    ),    # @brief ASPD angle speed register
        (REG_AREV,     5    ),    # @brief AREV angle revolution register
        (REG_FSYNC,    6    ),    # @brief FSYNC frame synchronization register
        (REG_MOD_1,    7    ),    # @brief MOD_1 interface mode1 register
        (REG_SIL,      8    ),    # @brief SIL register
        (REG_MOD_2,    9    ),    # @brief MOD_2 interface mode2 register
        (REG_MOD_3,   10    ),    # @brief MOD_3 interface mode3 register
        (REG_OFFX,    11    ),    # @brief OFFX offset x
        (REG_OFFY,    12    ),    # @brief OFFY offset y
        (REG_SYNCH,   13    ),    # @brief SYNCH synchronicity
        (REG_IFAB,    14    ),    # @brief IFAB register
        (REG_MOD_4,   15    ),    # @brief MOD_4 interface mode4 register
        (REG_TCO_Y,   16    ),    # @brief TCO_Y temperature coefficient register
        (REG_ADC_X,   17    ),    # @brief ADC_X ADC X-raw value
        (REG_ADC_Y,   18    ),    # @brief ADC_Y ADC Y-raw value
        (REG_D_MAG,   19    ),    # @brief D_MAG angle vector magnitude
        (REG_T_RAW,   20    ),    # @brief T_RAW temperature sensor raw-value
        (REG_IIF_CNT, 21    ),    # @brief IIF_CNT IIF counter value
        (REG_T25O,    22    ),    # @brief T25O temperature 25°c offset value
    ]

    # bitFields registry map 
    bitFields = [
        (REG_ACCESS_RU,  REG_STAT,    0x2,    1,  0x00,  0),       # @brief00 bits 0:0 SRST status watch dog
        (REG_ACCESS_R,   REG_STAT,    0x2,    1,  0x00,  0),       # @brief01 bits 1:1 SWD status watch dog
        (REG_ACCESS_R,   REG_STAT,    0x4,    2,  0x00,  0),       # @brief02 bits 2:2 SVR status voltage regulator
        (REG_ACCESS_R,   REG_STAT,    0x8,    3,  0x00,  0),       # @brief03 bits 3:3 SFUSE status fuses
        (REG_ACCESS_R,   REG_STAT,    0x10,   4,  0x00,  0),       # @brief04 bits 4:4 SDSPU status digital signal processing unit
        (REG_ACCESS_RU,  REG_STAT,    0x20,   5,  0x00,  0),       # @brief05 bits 5:5 SOV status overflow
        (REG_ACCESS_RU,  REG_STAT,    0x40,   6,  0x00,  0),       # @brief06 bits 6:6 SXYOL status X/Y data out limit
        (REG_ACCESS_RU,  REG_STAT,    0x80,   7,  0x00,  0),       # @brief07 bits 7:7 SMAGOL status magnitude out limit
        (REG_ACCESS_RES, REG_STAT,    0x100,  8,  0x00,  0),       # @brief08 bits 8:8 reserved
        (REG_ACCESS_R,   REG_STAT,    0x200,  9,  0x00,  0),       # @brief09 bits 9:9 SADCT status ADC test
        (REG_ACCESS_R,   REG_STAT,    0x400,  10, 0x00,  0),       # @brief10 bits 10:10 SROM status ROM
        (REG_ACCESS_RU,  REG_STAT,    0x800,  11, 0x00,  0),       # @brief11 bits 11:11 NOGMRXY no valid GMR XY Values
        (REG_ACCESS_RU,  REG_STAT,    0x1000, 12, 0x00,  0),       # @brief12 bits 12:12 NOGMRA no valid GMR Angle Value
        (REG_ACCESS_RW,  REG_STAT,    0x6000, 13, 0x00,  0),       # @brief13 bits 14:13 SNR slave number
        (REG_ACCESS_RU,  REG_STAT,    0x8000, 15, 0x00,  0),       # @brief14 bits 15:15 RDST read status

        (REG_ACCESS_RW,  REG_ACSTAT,  0x1,    0,  0x00,  1),       # @brief15 bits 0:0 ASRST Activation of Hardware Reset
        (REG_ACCESS_RWU, REG_ACSTAT,  0x2,    1,  0x00,  1),       # @brief16 bits 1:1 ASWD Enable DSPU Watch dog
        (REG_ACCESS_RWU, REG_ACSTAT,  0x4,    2,  0x00,  1),       # @brief17 bits 2:2 ASVR Enable Voltage regulator Check
        (REG_ACCESS_RWU, REG_ACSTAT,  0x8,    3,  0x00,  1),       # @brief18 bits 3:3 ASFUSE Activation Fuse CRC
        (REG_ACCESS_RWU, REG_ACSTAT,  0x10,   4,  0x00,  1),       # @brief19 bits 4:4 ASDSPU Activation DSPU BIST
        (REG_ACCESS_RWU, REG_ACSTAT,  0x20,   5,  0x00,  1),       # @brief20 bits 5:5 ASOV Enable of DSPU Overflow Check
        (REG_ACCESS_RWU, REG_ACSTAT,  0x40,   6,  0x00,  1),       # @brief21 bits 6:6 ASVECXY Activation of X,Y Out of Limit-Check
        (REG_ACCESS_RWU, REG_ACSTAT,  0x80,   7,  0x00,  1),       # @brief22 bits 7:7 ASVEGMAG Activation of Magnitude Check
        (REG_ACCESS_RES, REG_ACSTAT,  0x100,  8,  0x00,  1),       # @brief23 bits 8:8 Reserved
        (REG_ACCESS_RWU, REG_ACSTAT,  0x200,  9,  0x00,  1),       # @brief24 bits 9:9 ASADCT Enable ADC Test vector Check
        (REG_ACCESS_RWU, REG_ACSTAT,  0x400,  10, 0x00,  1),       # @brief25 bits 10:10 ASFRST Activation of Firmware Reset
        (REG_ACCESS_RES, REG_ACSTAT,  0xF800, 11, 0x00,  1),       # @brief26 bits 15:11 Reserved

        (REG_ACCESS_RU,  REG_AVAL,    0x7FFF, 0,  0x00,  2),       # @brief27 bits 14:0 ANGVAL Calculated Angle Value (signed 15-bit)
        (REG_ACCESS_R,   REG_AVAL,    0x8000, 15, 0x00,  2),       # @brief28 bits 15:15 RDAV Read Status, Angle Value

        (REG_ACCESS_RU,  REG_ASPD,    0x7FFF, 0,  0x00,  3),       # @brief29 bits 14:0 ANGSPD Signed value, where the sign bit [14] indicates the direction of the rotation
        (REG_ACCESS_R,   REG_ASPD,    0x8000, 15, 0x00,  3),       # @brief30 bits 15:15 RDAS Read Status, Angle Speed

        (REG_ACCESS_RU,  REG_AREV,    0xFF,   0,  0x00,  4),       # @brief31 bits 8:0 REVOL Revolution counter. Increments for every full rotation in counter-clockwise direction
        (REG_ACCESS_RWU, REG_AREV,    0x7E00, 9,  0x00,  4),       # @brief32 bits 14:9 FCNT Internal frame counter. Increments every update period
        (REG_ACCESS_R,   REG_AREV,    0x8000, 15, 0x00,  4),       # @brief33 its 15:15 RDREV Read Status, Revolution

        (REG_ACCESS_RWU, REG_FSYNC,   0xFF,   0,  0x00,  5),       # @brief34 bits 8:0 TEMPR Signed offset compensated temperature value
        (REG_ACCESS_RU,  REG_FSYNC,   0xFE00, 9,  0x00,  5),       # @brief35 bits 15:9 FSYNC Frame Synchronization Counter Value

        (REG_ACCESS_RW,  REG_MOD_1,   0x3,    0,  0x00,  6),       # @brief36 bits 1:0 IIFMOD Incremental Interface Mode
        (REG_ACCESS_RW,  REG_MOD_1,   0x4,    2,  0x00,  6),       # @brief37 bits 2:2 DSPUHOLD if DSPU is on hold, no watch dog reset is performed by DSPU
        (REG_ACCESS_RES, REG_MOD_1,   0x8,    3,  0x00,  6),       # @brief38 bits 3:3 Reserved1
        (REG_ACCESS_RW,  REG_MOD_1,   0x10,   4,  0x00,  6),       # @brief39 bits 4:4 CLKSEL switch to external clock at start-up only
        (REG_ACCESS_RES, REG_MOD_1,   0x3FE0, 5,  0x00,  6),       # @brief40 bits 13:5 Reserved2
        (REG_ACCESS_RW,  REG_MOD_1,   0x6000, 13, 0x00,  6),       # @brief41 bits 15:14 FIRMD Update Rate Setting

        (REG_ACCESS_RW,  REG_SIL,     0x7,    0,  0x00,  7),       # @brief42 bits 2:0 ADCTVX Test vector X
        (REG_ACCESS_RW,  REG_SIL,     0x38,   3,  0x00,  7),       # @brief43 bits 5:3 ADCTVY Test vector Y
        (REG_ACCESS_RW,  REG_SIL,     0x40,   6,  0x00,  7),       # @brief44 bits 6:6 ADCTVEN Sensor elements are internally disconnected and test voltages are connected to ADCs
        (REG_ACCESS_RES, REG_SIL,     0x380,  7,  0x00,  7),       # @brief45 bits 9:7 Reserved1
        (REG_ACCESS_RW,  REG_SIL,     0x400,  10, 0x00,  7),       # @brief46 bits 10:10 FUSEREL Triggers reload of default values from laser fuses into configuration registers
        (REG_ACCESS_RES, REG_SIL,     0x3800, 11, 0x00,  7),       # @brief47 bits 13:11 Reserved2
        (REG_ACCESS_RW,  REG_SIL,     0x4000, 14, 0x00,  7),       # @brief48 bits 14:14 FILTINV the X- and Y-signals are inverted. The angle output is then shifted by 180°
        (REG_ACCESS_RW,  REG_SIL,     0x8000, 15, 0x00,  7),       # @brief49 bits 15:15 FILTPAR the raw X-signal is routed also to the raw Y-signal input of the filter so SIN and COS signal should be identical

        (REG_ACCESS_RW,  REG_MOD_2,   0x3,    0,  0x00,  8),       # @brief50 bits 1:0 AUTOCAL Automatic calibration of offset and amplitude synchronicity for applications with full-turn
        (REG_ACCESS_RW,  REG_MOD_2,   0x4,    2,  0x00,  8),       # @brief51 bits 2:2 PREDICT Prediction of angle value based on current angle speed
        (REG_ACCESS_RW,  REG_MOD_2,   0x8,    3,  0x00,  8),       # @brief52 bits 3:3 ANGDIR Inverts angle and angle speed values and revolution counter behavior
        (REG_ACCESS_RW,  REG_MOD_2,   0x7FF0, 4,  0x00,  8),       # @brief53 bits 14:4 ANGRANGE Changes the representation of the angle output by multiplying the output with a factor ANG_RANGE/128
        (REG_ACCESS_RES, REG_MOD_2,   0x8000, 15, 0x00,  8),       # @brief54 bits 15:15 Reserved1

        (REG_ACCESS_RW,  REG_MOD_3,   0x3,    0,  0x00,  9),       # @brief55 bits 1:0 PADDRV Configuration of Pad-Driver
        (REG_ACCESS_RW,  REG_MOD_3,   0x4,    2,  0x00,  9),       # @brief56 bits 2:2 SSCOD SSC-Interface Data Pin Output Mode
        (REG_ACCESS_RW,  REG_MOD_3,   0x8,    3,  0x00,  9),       # @brief57 bits 3:3 SPIKEF Filters voltage spikes on input pads (IFC, SCK and CSQ)
        (REG_ACCESS_RW,  REG_MOD_3,   0xFFF0, 4,  0x00,  9),       # @brief58 bits 15:4 ANG_BASE Sets the 0° angle position (12 bit value). Angle base is factory-calibrated to make the 0° direction parallel to the edge of the chip

        (REG_ACCESS_RES, REG_OFFX,    0xF,    0,  0x00, 10),       # @brief59 bits 3:0 Reserved1
        (REG_ACCESS_RW,  REG_OFFX,    0xFFF0, 4,  0x00, 10),       # @brief60 bits 15:4 XOFFSET 12-bit signed integer value of raw X-signal offset correction at 25°C

        (REG_ACCESS_RES, REG_OFFY,    0xF,    0,  0x00, 11),       # @brief61 bits 3:0 Reserved1
        (REG_ACCESS_RW,  REG_OFFY,    0xFFF0, 4,  0x00, 11),       # @brief62 bits 15:4 YOFFSET 12-bit signed integer value of raw Y-signal offset correction at 25°C

        (REG_ACCESS_RES, REG_SYNCH,   0xF,    0,  0x00, 12),       # @brief63 bits 3:0 Reserved1
        (REG_ACCESS_RW,  REG_SYNCH,   0xFFF0, 4,  0x00, 12),       # @brief64 bits 15:4 SYNCH 12-bit signed integer value of amplitude synchronicity

        (REG_ACCESS_RW,  REG_IFAB,    0x3,    0,  0x00, 13),       # @brief65 bits 1:0 IFADHYST Hysteresis (multi-purpose)
        (REG_ACCESS_RW,  REG_IFAB,    0x4,    2,  0x00, 13),       # @brief66 bits 2:2 IFABOD IFA,IFB,IFC Output Mode
        (REG_ACCESS_RW,  REG_IFAB,    0x8,    3,  0x00, 13),       # @brief67 bits 3:3 FIRUDR Initial filter update rate (FIR)
        (REG_ACCESS_RW,  REG_IFAB,    0xFFF0, 4,  0x00, 13),       # @brief68 bits 15:4 ORTHO Orthogonality Correction of X and Y Components

        (REG_ACCESS_RW,  REG_MOD_4,   0x3,    0,  0x00, 14),       # @brief69 bits 1:0 IFMD Interface Mode on IFA,IFB,IFC
        (REG_ACCESS_RES, REG_MOD_4,   0x4,    2,  0x00, 14),       # @brief70 bits 2:2 Reserved1
        (REG_ACCESS_RW,  REG_MOD_4,   0x18,   3,  0x00, 14),       # @brief71 bits 4:3 IFABRES IIF resolution (multi-purpose)
        (REG_ACCESS_RW,  REG_MOD_4,   0x1E0,  5,  0x00, 14),       # @brief72 bits 8:5 HSMPLP Hall Switch mode (multi-purpose)
        (REG_ACCESS_RW,  REG_MOD_4,   0x7E00, 9,  0x00, 14),       # @brief73 bits 15:9 TCOXT 7-bit signed integer value of X-offset temperature coefficient

        (REG_ACCESS_RW,  REG_TCO_Y,   0x7F,   0,  0x00, 15),       # @brief74 bits 7:0 CRCPAR CRC of Parameters
        (REG_ACCESS_RW,  REG_TCO_Y,   0x80,   8,  0x00, 15),       # @brief75 bits 8:8 SBIST Startup-BIST
        (REG_ACCESS_RW,  REG_TCO_Y,   0x7E00, 9,  0x00, 15),       # @brief76 bits 15:9 TCOYT 7-bit signed integer value of Y-offset temperature coefficient

        (REG_ACCESS_R,   REG_ADC_X,   0xFFFF, 0,  0x00, 16),       # @brief77 bits 15:0 ADCX ADC value of X-GMR

        (REG_ACCESS_R,   REG_ADC_Y,   0xFFFF, 0,  0x00, 17),       # @brief78 bits 15:0 ADCY ADC value of Y-GMR

        (REG_ACCESS_RU,  REG_D_MAG,   0x3FF,  0,  0x00, 18),       # @brief79 bits 9:0 MAG Unsigned Angle Vector Magnitude after X, Y error compensation (due to temperature)
        (REG_ACCESS_RES, REG_D_MAG,   0xFC00, 10, 0x00, 18),       # @brief80 bits 15:10 Reserved1

        (REG_ACCESS_RU,  REG_T_RAW,   0x3FF,  0,  0x00, 19),       # @brief81 bits 9:0 TRAW Temperature Sensor Raw-Value at ADC without offset
        (REG_ACCESS_RES, REG_T_RAW,   0xFC00, 10, 0x00, 19),       # @brief82 bits 14:10 Reserved1
        (REG_ACCESS_RU,  REG_T_RAW,   0x8000, 15, 0x00, 19),       # @brief83 bits 15:15 TTGL Temperature Sensor Raw-Value Toggle toggles after every new temperature value

        (REG_ACCESS_RU,  REG_IIF_CNT, 0x7FFF, 0,  0x00, 20),       # @brief84 bits 14:0 IIFCNT 14 bit counter value of IIF increments
        (REG_ACCESS_RES, REG_IIF_CNT, 0x8000, 15, 0x00, 20),       # @brief85 bits 15:14 Reserved1

        (REG_ACCESS_R,   REG_T25O,    0x1FFF, 0,  0x00, 21),       # @brief86 bit 8:0 T250 Signed offset value at 25°C temperature; 1dig=0.36°C
        (REG_ACCESS_RES, REG_T25O,    0xFE00, 9,  0x00, 21),       # @brief87 bits 15:9 Reserved1

    ]

    MAX_REGISTER_MEM = 22

    UPD_low  = 0x0000
    UPD_high = 0x0400

    SAFE_low  = 0x0000
    SAFE_high = 0x0001

    def __init__(self, parent):
        self.parent = parent
        self.regMap = [0] * self.MAX_REGISTER_MEM

    def get_bit_field(self, bit_field):
        if (bit_field['regAccess'] & self.REG_ACCESS_R) == self.REG_ACCESS_R:
            p = self.parent
            if (bit_field['regAccess'] & self.REG_ACCESS_U) == self.REG_ACCESS_U:
                p.sBus.trigger_update()
            p.read_from_sensor(self.addrFields[bit_field['posMap']]['regAddress'], self.regMap[bit_field['posMap']], self.UPD_low, self.SAFE_high)
            bit_f_value = (self.regMap[bit_field['posMap']] & bit_field['mask']) >> bit_field['position']
            return True, bit_f_value
        return False, None

    def set_bit_field(self, bit_field, bit_f_new_value):
        if (bit_field['regAccess'] & self.REG_ACCESS_W) == self.REG_ACCESS_W:
            p = self.parent
            self.regMap[bit_field['posMap']] = (self.regMap[bit_field['posMap']] & ~bit_field['mask']) | ((bit_f_new_value << bit_field['position']) & bit_field['mask'])
            p.write_to_sensor(self.addrFields[bit_field['posMap']]['regAddress'], self.regMap[bit_field['posMap']], True)
            return True
        return False

    def is_status_reset(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SRST])
        return bitf if success else False

    def is_status_watch_dog(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SWD])
        return bitf if success else False

    def is_status_voltage(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SVR])
        return bitf if success else False

    def is_status_fuse(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SFUSE])
        return bitf if success else False

    def is_status_dspu(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SDSPU])
        return bitf if success else False

    def is_status_overflow(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SOV])
        return bitf if success else False

    def is_status_xy_out_of_limit(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SXYOL])
        return bitf if success else False

    def is_status_magnitude_out_of_limit(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SMAGOL])
        return bitf if success else False

    def is_status_adc(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SADCT])
        return bitf if success else False

    def is_status_rom(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SROM])
        return bitf if success else False

    def is_status_gmrxy(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_NOGMRXY])
        return bitf if success else False

    def is_status_gmra(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_NOGMRA])
        return bitf if success else False

    def is_status_read(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_RDST])
        return bitf if success else False

    def get_slave_number(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_STAT_SNR])
        return bitf if success else 0

    def set_slave_number(self, snr):
        self.set_bit_field(self.bitFields[self.REG_STAT_SNR], snr)

    def is_activation_reset(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASRST])
        return bitf if success else False

    def set_activation_reset(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASRST], 1)

    def enable_watchdog(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASWD], 1)

    def disable_watchdog(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASWD], 0)

    def is_watchdog(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASWD])
        return bitf if success else False

    def enable_voltage_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVR], 1)

    def disable_voltage_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVR], 0)

    def is_voltage_check(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASVR])
        return bitf if success else False

    def enable_fuse_crc(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASFUSE], 1)

    def disable_fuse_crc(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASFUSE], 0)

    def is_fuse_crc(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASFUSE])
        return bitf if success else False

    def enable_dspu_bist(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASDSPU], 1)

    def disable_dspu_bist(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASDSPU], 0)

    def is_dspu_bist(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASDSPU])
        return bitf if success else False

    def enable_dspu_overflow(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASOV], 1)

    def disable_dspu_overflow(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASOV], 0)

    def is_dspu_overflow(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASOV])
        return bitf if success else False

    def enable_xy_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVECXY], 1)

    def disable_xy_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVECXY], 0)

    def is_xy_check(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASVECXY])
        return bitf if success else False

    def enable_gmr_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVEGMAG], 1)

    def disable_gmr_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASVEGMAG], 0)

    def is_gmr_check(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASVEGMAG])
        return bitf if success else False

    def enable_adc_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASADCT], 1)

    def disable_adc_check(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASADCT], 0)

    def is_adc_check(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASADCT])
        return bitf if success else False

    def activate_firmware_reset(self):
        self.set_bit_field(self.bitFields[self.REG_ACSTAT_ASFRST], 1)

    def is_firmware_reset(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ACSTAT_ASFRST])
        return bitf if success else False

    def is_angle_value_new(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_AVAL_RDAV])
        return bitf if success else False

    def get_angle_value(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_AVAL_ANGVAL])
        return bitf if success else 0

    def is_speed_value_new(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ASPD_RDAS])
        return bitf if success else False

    def get_speed_value(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ASPD_ANGSPD])
        return bitf if success else 0

    def is_number_of_revolutions_new(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_AREV_RDREV])
        return bitf if success else False

    def get_number_of_revolutions(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_AREV_REVOL])
        revolutions = bitf & 0xFF
        if revolutions & 0x100:
            revolutions *= -1
        return revolutions

    def get_frame_counter(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_AREV_FCNT])
        return bitf if success else 0

    def set_frame_counter(self, fcnt):
        self.set_bit_field(self.bitFields[self.REG_AREV_FCNT], fcnt)

    def get_frame_sync_counter(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_FSYNC_FSYNC])
        return bitf if success else 0

    def set_frame_sync_counter(self, fsync):
        self.set_bit_field(self.bitFields[self.REG_FSYNC_FSYNC], fsync)

    def get_temperature_value(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_FSYNC_TEMPR])
        temperature = bitf & 0xFF
        if temperature & 0x100:
            temperature *= -1
        return temperature

    def set_filter_decimation(self, firmd):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_FIRMD], firmd)

    def get_filter_decimation(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_1_FIRMD])
        return bitf if success else 0

    def set_iif_mod(self, iifmod):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_IIFMOD], iifmod)

    def get_iif_mod(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_1_IIFMOD])
        return bitf if success else 0

    def hold_dspu(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_DSPUHOLD], 1)

    def release_dspu(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_DSPUHOLD], 0)

    def is_dspu_hold(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_1_DSPUHOLD])
        return bitf if success else False

    def set_internal_clock(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_CLKSEL], 0)

    def set_external_clock(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_1_CLKSEL], 1)

    def status_clock_source(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_1_CLKSEL])
        return bitf if success else False

    def enable_filter_parallel(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_FILTPAR], 1)

    def disable_filter_parallel(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_FILTPAR], 0)

    def is_filter_parallel(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_FILTPAR])
        return bitf if success else False

    def enable_filter_inverted(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_FILTINV], 1)

    def disable_filter_inverted(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_FILTINV], 0)

    def is_filter_inverted(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_FILTINV])
        return bitf if success else False

    def enable_adc_test_vector(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_ADCTVEN], 1)

    def disable_adc_test_vector(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_ADCTVEN], 0)

    def is_adc_test_vector(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_ADCTVEN])
        return bitf if success else False

    def set_fuse_reload(self):
        self.set_bit_field(self.bitFields[self.REG_SIL_FUSEREL], 1)

    def get_fuse_reload(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_FUSEREL])
        return bitf if success else False

    def set_test_vector_x(self, adctvx):
        self.set_bit_field(self.bitFields[self.REG_SIL_ADCTVX], adctvx)

    def get_test_vector_x(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_ADCTVX])
        return bitf if success else 0

    def set_test_vector_y(self, adctvy):
        self.set_bit_field(self.bitFields[self.REG_SIL_ADCTVY], adctvy)

    def get_test_vector_y(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SIL_ADCTVY])
        return bitf if success else 0

    def direction_clockwise(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_ANGDIR], 1)

    def direction_counter_clockwise(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_ANGDIR], 0)

    def is_angle_direction(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_2_ANGDIR])
        return bitf if success else False

    def enable_prediction(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_PREDICT], 1)

    def disable_prediction(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_PREDICT], 0)

    def is_prediction(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_2_PREDICT])
        return bitf if success else False

    def set_angle_range(self, range):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_ANGRANGE], range)

    def get_angle_range(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_2_ANGRANGE])
        return bitf if success else 0

    def set_calibration_mode(self, autocal):
        self.set_bit_field(self.bitFields[self.REG_MOD_2_AUTOCAL], autocal)

    def get_calibration_mode(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_2_AUTOCAL])
        return bitf if success else 0

    def enable_spike_filter(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_SPIKEF], 1)

    def disable_spike_filter(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_SPIKEF], 0)

    def is_spike_filter(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_3_SPIKEF])
        return bitf if success else False

    def enable_ssc_open_drain(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_SSCOD], 1)

    def enable_ssc_push_pull(self):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_SSCOD], 0)

    def is_ssc_output_mode(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_3_SSCOD])
        return bitf if success else False

    def set_angle_base(self, base):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_ANG_BASE], base)

    def get_angle_base(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_3_ANG_BASE])
        return bitf if success else 0

    def set_pad_driver(self, pad):
        self.set_bit_field(self.bitFields[self.REG_MOD_3_PADDRV], pad)

    def get_pad_driver(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_3_PADDRV])
        return bitf if success else 0

    def set_offset_x(self, offx):
        self.set_bit_field(self.bitFields[self.REG_OFFX_XOFFSET], offx)

    def get_offset_x(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_OFFX_XOFFSET])
        return bitf if success else 0

    def set_offset_y(self, offy):
        self.set_bit_field(self.bitFields[self.REG_OFFY_YOFFSET], offy)

    def get_offset_y(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_OFFY_YOFFSET])
        return bitf if success else 0

    def set_amplitude_synch(self, synch):
        self.set_bit_field(self.bitFields[self.REG_SYNCH_SYNCH], synch)

    def get_amplitude_synch(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_SYNCH_SYNCH])
        return bitf if success else 0

    def set_fir_update_rate(self, fir):
        self.set_bit_field(self.bitFields[self.REG_IFAB_FIRUDR], fir)

    def get_fir_update_rate(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_IFAB_FIRUDR])
        return bitf if success else 0

    def enable_ifab_open_drain(self):
        self.set_bit_field(self.bitFields[self.REG_IFAB_IFABOD], 1)

    def enable_ifab_push_pull(self):
        self.set_bit_field(self.bitFields[self.REG_IFAB_IFABOD], 0)

    def is_ifab_output_mode(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_IFAB_IFABOD])
        return bitf if success else False

    def set_orthogonality(self, ortho):
        self.set_bit_field(self.bitFields[self.REG_IFAB_ORTHO], ortho)

    def get_orthogonality(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_IFAB_ORTHO])
        return bitf if success else 0

    def set_hysteresis_mode(self, hyst):
        self.set_bit_field(self.bitFields[self.REG_IFAB_IFADHYST], hyst)

    def get_hysteresis_mode(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_IFAB_IFADHYST])
        return bitf if success else 0

    def set_interface_mode(self, ifmd):
        self.set_bit_field(self.bitFields[self.REG_MOD_4_IFMD], ifmd)

    def get_interface_mode(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_4_IFMD])
        return bitf if success else 0

    def set_ifab_res(self, res):
        self.set_bit_field(self.bitFields[self.REG_MOD_4_IFABRES], res)

    def get_ifab_res(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_4_IFABRES])
        return bitf if success else 0

    def set_hsm_plp(self, plp):
        self.set_bit_field(self.bitFields[self.REG_MOD_4_HSMPLP], plp)

    def get_hsm_plp(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_4_HSMPLP])
        return bitf if success else 0

    def set_offset_temperature_x(self, tcox):
        self.set_bit_field(self.bitFields[self.REG_MOD_4_TCOXT], tcox)

    def get_offset_temperature_x(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_MOD_4_TCOXT])
        if bitf & 0x8000:
            bitf *= -1
        return bitf if success else 0

    def set_offset_temperature_y(self, tcoy):
        self.set_bit_field(self.bitFields[self.REG_TCO_Y_TCOYT], tcoy)

    def get_offset_temperature_y(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_TCO_Y_TCOYT])
        if bitf & 0x8000:
            bitf *= -1
        return bitf if success else 0

    def enable_startup_bist(self):
        self.set_bit_field(self.bitFields[self.REG_TCO_Y_SBIST], 1)

    def disable_startup_bist(self):
        self.set_bit_field(self.bitFields[self.REG_TCO_Y_SBIST], 0)

    def is_startup_bist(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_TCO_Y_SBIST])
        return bitf if success else False

    def set_crc_par(self, crc):
        self.set_bit_field(self.bitFields[self.REG_TCO_Y_CRCPAR], crc)

    def get_crc_par(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_TCO_Y_CRCPAR])
        return bitf if success else 0

    def get_adc_x(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ADC_X_ADCX])
        return bitf if success else 0

    def get_adc_y(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_ADC_Y_ADCY])
        return bitf if success else 0

    def get_vector_magnitude(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_D_MAG_MAG])
        return bitf if success else 0

    def get_temperature_raw(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_T_RAW_TRAW])
        return bitf if success else 0

    def is_temperature_toggle(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_T_RAW_TTGL])
        return bitf if success else False

    def get_counter_increments(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_IIF_CNT_IIFCNT])
        return bitf if success else 0

    def get_t25_offset(self):
        success, bitf = self.get_bit_field(self.bitFields[self.REG_T25O_T250])
        return bitf if success else 0
