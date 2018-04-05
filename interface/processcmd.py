import logging
import binascii

from time import sleep

logging.getLogger('')

HASP_SOH = b'\x01'
HASP_STX = b'\x02'
HASP_CMD_BYTE1 = b'\x10'
HASP_CMD_BYTE2 = b'\x20'
HASP_ETX = b'\x03'
HASP_CR = b'\x0D'
HASP_LF = b'\x0A'
HASP_CMD_COMPLETE = '\x30'


# No idea if this works yet, needs to be tested
class SerialConnectionTest:
    command = [HASP_SOH,
               HASP_STX,
               b'\x41',
               b'\x42',
               HASP_ETX,
               HASP_CR,
               HASP_LF]
    cmd_index = 0

    def isOpen(self):
        return True

    def write(self, x):
        pass

    def open(self):
        pass

    def read(self, n):
        sleep(.2)
        val = self.command[self.cmd_index]
        self.cmd_index = (self.cmd_index + 1) % len(self.command)
        return val


def processcmd(serial_conn):
    command_processed = False
    state = HASP_SOH
    cmd1 = None
    cmd2 = None



    while not command_processed:
        in_byte = serial_conn.read(1)
        logging.debug("Received byte: {}".format(binascii.hexlify(in_byte)))

        if state == HASP_SOH:
            if in_byte == b'\x01':
                logging.info("Begin Arduino Transmission")
                state = HASP_STX
        elif state == HASP_STX:
            if in_byte == b'\x02':
                state = HASP_CMD_BYTE1
            else:
                state = HASP_SOH
        elif state == HASP_CMD_BYTE1:
            cmd1 = in_byte
            state = HASP_CMD_BYTE2
        elif state == HASP_CMD_BYTE2:
            cmd2 = in_byte
            state = HASP_ETX
        elif state == HASP_ETX:
            if in_byte == b'\x03':
                state = HASP_CR
            else:
                state = HASP_SOH
        elif state == HASP_CR:
            if in_byte == b'\x0D':
                state = HASP_LF
            else:
                state = HASP_SOH
        elif state == HASP_LF:
            if in_byte == b'\x0A':
                state = HASP_CMD_COMPLETE
                command_processed = True
            else:
                state = HASP_SOH
        else:
            state = HASP_SOH

    logging.info("End Arduino Transmission")

    return cmd1, cmd2


if __name__ == "__main__":
    test_serial = SerialConnectionTest()

    while True:
        cmd1, cmd2 = processcmd(test_serial)
        sleep(1)
        print("Received CMD1: {0} CMD2: {1}".format(binascii.hexlify(cmd1), binascii.hexlify(cmd2)))
