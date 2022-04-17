from machine import UART, Pin 
from time import sleep

# uos provides information such as the machine name and build version numbers
import uos

# default baud rate is 9600 for HC-06 and DX-BT04-E modules

# create the UART with BT module
# GP0,1 corresponds to physical pins 1,2 on the Pico
uartBT = UART(id=0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)

# create the UART with TinyG
# GP4,5 corresponds to physical pins 6,7 on the Pico
uartTG = UART(id=1, baudrate=115200, tx=Pin(4), rx=Pin(5), bits=8, parity=None, stop=1)

# blink routine for debugging communication
led = Pin(25, Pin.OUT)
def blink():
    for i in range(20):
        led.toggle()
        sleep(0.1)

tinyGMode=False

while True:
    while uartBT.any() > 0:
        response = uartBT.read()
        try:
            output = str(response.decode('utf-8'))
            print(output)
        except:
            print("Unable to parse response")
            print("Verify correct baud setting")
            continue
        output = output.rstrip('\r\n')
        if output == "blink" :
            blink()
        elif output == "mode TinyG on" :
            tinyGMode = True
        elif output == "mode TinyG off" :
            tinyGMode = False
        print("tinyG mode: "+str(tinyGMode))