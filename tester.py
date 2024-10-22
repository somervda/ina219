from machine import Pin, I2C
from ina219 import INA219
from logging import DEBUG

SHUNT_OHMS = 0.1

i2c = machine.I2C(0, scl=machine.Pin(13), sda=machine.Pin(12), freq=100000)
for device in i2c.scan():
    print("I2C hexadecimal address: ", hex(device))

ina = INA219(SHUNT_OHMS, i2c, log_level=DEBUG)
ina.configure()

print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())