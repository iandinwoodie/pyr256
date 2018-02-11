from r256 import r256

controller = r256.Driver(1, "COM5", 9600)
controller.open()
controller.close()
