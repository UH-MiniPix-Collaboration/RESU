HASP_SOH = 0x01
HASP_STX = 0x02
HASP_CMD_BYTE1 = 0x10
HASP_CMD_BYTE2 = 0x20
HASP_ETX = 0x03
HASP_CR = 0x0D
HASP_LF = 0x0A
HASP_CMD_COMPLETE = 0x30

# No idea if this works yet, needs to be tested


def processcmd(serial_conn):

    command_processed = False
    state = HASP_SOH
    cmd1 = None
    cmd2 = None

    while not command_processed:
        in_byte = serial_conn.read()

        if state == HASP_SOH:
            if in_byte == 0x01:
                state = HASP_STX
        elif state == HASP_STX:
            if in_byte == 0x02:
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
            if in_byte == 0x03:
                state = HASP_CR
            else:
                state = HASP_SOH
        elif state == HASP_CR:
            if in_byte == 0x0D:
                state = HASP_LF
            else:
                state = HASP_SOH
        elif state == HASP_LF:
            if in_byte == 0x0A:
                state = HASP_CMD_COMPLETE
                command_processed = True
            else:
                state = HASP_SOH
        else:
            state = HASP_SOH
    return cmd1, cmd2

