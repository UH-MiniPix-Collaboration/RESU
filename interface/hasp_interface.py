#Python code for Raspberry Pi to receive serial commands from the Arduino.

#!/usr/bin/python3
import serial

ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0', 4800, timeout = 1)
print("Serial Connected")

# read from Arduino
while True:
	s_input = ser.read(1)#.decode("utf8", "replace")
	#input = ser.read(1) * 256
	#input = input + ser.read()
	print(s_input)
#print ("Read input " + input.decode("utf-8") + " from Arduino")

# write something back

#ser.write(b'A')

# read response back from Arduino
#for i in range (0,3):
#        input = ser.read()
#        input_number = ord(input)
#        print ("Read input back: " + str(input_number))
