
from time import sleep as dly
from smbus2 import SMBus
import numpy as np

I2C_ADDR = 104
PWR_MNG_REG = 107
STARTING_REG = 65

with SMBus(1) as bus:
    bus.write_byte_data(I2C_ADDR, PWR_MNG_REG, 0)
    dly(1)

def comb_bytes(inb1, inb2):
    inb1 = inb1 & 127
    #print(bin(inb1))
    #print(bin(inb2))
    outb = inb1 << 8 | inb2
    print(outb)
    temp = (outb / 340.00) + 36.53
    print(temp)
    return temp

def temperature(inv1, inv2):
    #print(bin(inv1), "|", inv2)
    #print(type(np.uint16(inv1)), "|", np.uint16(inv2))
    #inval = np.uint16(inv1) << 8 | np.uint16(inv2)
    inval = inv1 << 8 | inv2
    temp = (np.int16(inval) / 340.00) + 36.53
    #temp = (inval / 340.00) + 36.53
    print(temp)
    #return temp

for i in range(25):

    with SMBus(1) as bus:
        block = bus.read_i2c_block_data(I2C_ADDR, STARTING_REG, 2)
        #print(block)

    print(i)
    #print(np.int16(block[0] << 8 | block[1]))
    temperature(block[0], block[1])
    #print(type(block[6]))
    #comb_bytes(block[0], block[1])
    #print(comb_bytes(block[6], block[7]))
    #print(block[7] << 8 | block[8] )

    dly(1)

print("end")