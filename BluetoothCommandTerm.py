from machine import UART, Pin 
from time import sleep

# uos provides information such as the machine name and build version numbers
import uos

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=115200 # default is 9600 for HC-06 and DX-BT04-E modules
                # default is 115200 for Waveshare Pico-BLE module

# create the UART
uart = UART(id=id, baudrate=baudrate,tx=tx, rx=rx, bits=8, parity=None, stop=1)

# Print a pretty command line
print("-"*50)
print("PicoTerm")
print(uos.uname())
print("type 'quit' to exit, or help for commands")
# Loop
command = ""
while True and command !='quit':
    # Write our command prompt
    command = input("PicoTerm> ")
    if command == 'help':
        help()
    elif command != 'quit':
        #uart.write(command)
        # DX-BT04-E and Waveshare Pico-BLE modules require appended CR and LF chars!
        commandTermin = str(command)+"\r\n" 
        uart.write(commandTermin)
        print(command)
        sleep(0.1)
        response = bytes()
        
        while uart.any() > 0:
            response = uart.read()
        # output = "".join(["'",str(command),"'","response:",str(response.decode('utf-8'))])
        try:
            print("decoded: ")
            output = str(response.decode('utf-8'))
            print(output)
        except:
            print("weird response")
        
    elif command == 'quit':
        print("-"*50)
        print('Bye.')