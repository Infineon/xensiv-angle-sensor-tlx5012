# spi3w_ard.py
# MicroPython 3-wire SPI cover
# Author: Infineon Technologies AG
# Version: 4.0.0
# Copyright: 2020-2024 Infineon Technologies AG
# SPDX-License-Identifier: MIT

from machine import Pin, SPI
import time


class SPI3W:
    def __init__(self, spi_num=0):
        # self.mCS = Pin(15, Pin.OUT)  # Default CS pin
        # self.mMISO = Pin(12)  # Default MISO pin
        # self.mMOSI = Pin(13)  # Default MOSI pin
        # self.mSCK = Pin(14)  # Default SCK pin
        self.mSpiNum = spi_num
        #self.spi = SPI(spi_num, baudrate=1000000, polarity=0, phase=1, bits=8, firstbit=SPI.MSB)

    def begin(self, misoPin='P9_1', mosiPin='P9_0', sckPin='P9_2', cs='P9_3'):
        #self.mMOSI = Pin(mosiPin)
        #self.mMISO = Pin(misoPin)
        #self.mSCK = Pin(sckPin)

        self.setCSPin(cs)
        self.mCS.value(1)
        #self.spi = SPI(baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=sckPin)
        self.spi = SPI(baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=sckPin, mosi=mosiPin, miso=misoPin)

    def setCSPin(self, cs):
        self.mCS = Pin(cs, Pin.OUT)

    def trigger_update(self):
        self.mSCK.off()
        self.mMOSI.on()
        self.mCS.off()
        # grace period for register snapshot
        time.sleep_us(5)
        self.mCS.on()

    def send_receive(self, sent_data, size_of_sent_data, received_data, size_of_received_data):
        data_index = 0
        # Send via TX
        self.mCS.value(0)
        #self.mMISO.init(Pin.IN)
        #self.mMOSI.init(Pin.OUT)
        print("sent_data: ", sent_data)
        print("size_of_sent_data: ", size_of_sent_data)
        print("received_data: ", received_data)
        print("size_of_received_data: ", size_of_received_data)
        

        for data_index in range(size_of_sent_data):
            #self.spi.write_readinto(sent_data[data_index], received_data[data_index:data_index+2])
            received_data[0] = self.spi.write_readinto(int(sent_data[data_index]).to_bytes(2, 'big'), bytearray(2))

        # Receive via RX
        #self.mMISO.init(Pin.OUT)
        #self.mMOSI.init(Pin.IN)
        time.sleep_us(5)

        for data_index in range(size_of_received_data):
            received_data[data_index] = int.from_bytes(self.spi.read(2), 'big')

        self.mCS.value(1)