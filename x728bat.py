#!/usr/bin/env python
import struct
import smbus2

I2C_ADDR    = 0x36

def readVoltage(bus):
     address = I2C_ADDR
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage

def readCapacity(bus):
     address = I2C_ADDR
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

print ("Voltage:%5.2fV" % readVoltage(bus))
print ("Battery:%5i%%" % readCapacity(bus))
