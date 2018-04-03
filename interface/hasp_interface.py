#Python code for Raspberry Pi to receive serial commands from the Arduino.

#!/usr/bin/python3
import serial
import io
import datetime
import time

log_file = io.open("log.txt", "a")
ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0', 4800)


log_file.write("---Begin Log Entry---\n")

# Open serial port
if(ser.isOpen() == False):
        ser.open()
        print("Serial Connected")
        log_file.write("Serial Connected\n")
else:
        print("Serial Connected")
        log_file.write("Serial Connected\n")

        
# Read from Arduino
while True:
        s_input = ser.read(1) #.decode("utf8", "replace")
        
        if s_input == b'\x01':
                ts = str(datetime.datetime.utcnow())    #Gets the time at execution in UTC   
                log_file.write("Begin Arduino Transmission: " + str(ts) + "\n")
        print(s_input)
        log_file.write(str(s_input)+"\n")
#        import pdb; pdb.set_trace()  //Debugger

        if s_input == b'\x30':
                ts = str(datetime.datetime.utcnow())    #Gets the time at execution in UTC   
                log_file.write("End Arduino Transmission: " + str(ts) + "\n")
                succ = ser.write(b'n')
                ser.write(b'u')
                ser.write(b'd')
                ser.write(b'e')
                ser.write(b's')

                if succ == 1:
                        print ("Success: " + str(succ) + "\n")
                        log_file.write("Successful Transmission\n")

                log_file.write("---End Log Entry---\n\n\n")
        #input = ser.read(1) * 256
	#input = input + ser.read()
        #print ("Read input " + input.decode("utf-8") + " from Arduino")

# write something back

#ser.write(b'A')

# read response back from Arduino
#for i in range (0,3):
#        input = ser.read()
#        input_number = ord(input)
#        print ("Read input back: " + str(input_number))
