from machine import UART, Pin 
from time import sleep

# uos provides information such as the machine name and build version numbers
import uos

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=115200

# create the UART
uart = UART(id=id, baudrate=baudrate,tx=tx, rx=rx, bits=8, parity=None, stop=1)

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    sleep(0.1)