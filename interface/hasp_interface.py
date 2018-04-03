#Python code for Raspberry Pi to receive serial commands from the Arduino.

#!/usr/bin/python3
import serial
from processcmd import processcmd
ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0', 4800)
print("Serial Connected")

# read from Arduino
while True:
    cmd1, cmd2 = processcmd(ser)
    print(cmd1, cmd2)

#ser.write(b'A')

# read response back from Arduino
#for i in range (0,3):
#        input = ser.read()
#        input_number = ord(input)
#        print ("Read input back: " + str(input_number))
