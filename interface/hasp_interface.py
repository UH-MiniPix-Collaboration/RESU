# Python code for Raspberry Pi to receive serial commands from the Arduino.

# !/usr/bin/python3
import logging
import serial
from processcmd import processcmd, SerialConnectionTest

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    filename='log.txt',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


"""
Using a custom object to fake a real serial connection, should work with a real connection as well.
"""

def listen():

    # Uncomment to use a real connection
    ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0', 4800)

    # Open serial port
    if not ser.isOpen():
        ser.open()
        logging.info("Serial Connected")
    else:
        print("Serial Connected")
        logging.info("Serial Connected")

    # Read from Arduino
    while True:
        cmd1, cmd2 = processcmd(ser)
        logging.info("Received CMD1: {} CMD2: {}".format(cmd1, cmd2))

        succ = ser.write(b'n')
        ser.write(b'u')
        ser.write(b'd')
        ser.write(b'e')
        ser.write(b's')

        if succ == 1:
            #print("Success: " + str(succ) + "\n")
            logging.info("Successful Transmission\n")

            # input = ser.read(1) * 256
            # input = input + ser.read()
            # print ("Read input " + input.decode("utf-8") + " from Arduino")

# write something back

# ser.write(b'A')

# read response back from Arduino
# for i in range (0,3):
#        input = ser.read()
#        input_number = ord(input)
#        print ("Read input back: " + str(input_number))

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        logging.info("Exitting...")
    except Exception as e:
        logging.info(e)

