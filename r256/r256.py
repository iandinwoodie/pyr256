import time
import serial
import protocol

class Driver:

    def __init__(self, address, port, baud):
        """ Initialize the driver object """
        self.address = assign(address)
        self.con = serial.Serial(port, baud)

    def assign(self, address):
        if address in protocol.ADDRESS:
            return protocol.ADDRESS[address]
        try:
            tag = int(address)
            if (tag < 1) or (tag > 9):
                raise Exception('Out of bounds')
            return tag
        except:
            print("Error: invalid address " + address)
            exit()

    def open(self):
        """ Opening serial communications to the driver """
        self.con.open()
        if not self.con.isOpen():
            print("Error: %d failed to open" %self.con.port)
            exit()

    def move(self, steps):
        """ Driver actuation command """
        if steps >= 0:
            move_select = P.CMD_FORWARD
        else:
            move_select = P.CMD_BACKWARD
        self.con.write((P.CMD_START + self.address + move_select + str(steps) +
                        P.CMD_RUN + P.CMD_END).encode())
        bytesToRead = self.con.inWaiting()
        status = self.con.read(bytesToRead)
        status = self.page()
        while status != '0':
            status = self.page()
            print(status)
        return status

    def page(self):
        """ Driver status command """
        self.con.write((P.CMD_START + self.address + P.CMD_STS +
                        P.CMD_END).encode())
        time.sleep(0.1)
        bytesToRead = self.con.inWaiting()
        status = self.con.read().decode('utf-8')
        self.con.read(bytesToRead-1)
        return status

    def io(self, state):
        """ Driver I/O command """
        self.con.write((P.CMD_START + self.address + P.CMD_IO + str(state) +
                        P.CMD_END).encode())
        time.sleep(0.1)
        bytesToRead = self.con.inWaiting()
        status = (self.con.read(bytesToRead)).decode('utf-8')
        return status

    def close(self):
        """ Closing communication with the driver """
        while self.con.isOpen() == True:
            self.con.close()

