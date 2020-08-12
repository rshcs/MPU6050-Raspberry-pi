
from time import sleep as dly
from smbus2 import SMBus

I2C_ADDR = 104
PWR_MNG_REG = 107
STARTING_REG = 59

with SMBus(1) as bus:
    data = [PWR_MNG_REG, 0]
    bus.write_byte_data(I2C_ADDR, 0, data)

with SMBus(1) as bus:
    data = STARTING_REG
    bus.write_byte_data(I2C_ADDR, 0, data)

with SMBus(1) as bus:
    block = bus.read_i2c_block_data(I2C_ADDR, 0, 16)
    print(block)
