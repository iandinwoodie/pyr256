import serial
from .constants import PROTOCOL as P

class driver:
	def __init__(self, address, port, baud):
		self.address = address
		self.port = port
		self.baud = baud
		self.con = serial.Serial()
	
	def open(self):
		self.con.baudrate = self.baud
		self.con.port = self.port
		self.con.open()
		if self.con.isOpen() != True:
			print("	Error, "+self.con.port+" failed to open")
			exit()
	
	def move(self, steps):
		self.con.write(
			(P.CMD_START+
			str(self.address)+
			P.CMD_FORWARD+
			str(steps)+
			P.CMD_RUN+
			P.CMD_END
			).encode())
	
	def close(self):
		while self.con.isOpen() == True:
			self.con.close()
	
	def status(self):
		print("status")
	
	def io(self, output, state):
		print("io")