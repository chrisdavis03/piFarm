#!/home/chestnut/venv-piFarm/bin/python3

import smbus
import time

def getLux():
    bus  = smbus.SMBus(1)
    bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
    bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

    time.sleep(.5)

    data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
    data1 = bus.read_i2c_block_data(0x39, 0x0E| 0x80, 2)

    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]

    #full spectrum, IR, Visible
    return ch0, ch1, (ch0-ch1)
