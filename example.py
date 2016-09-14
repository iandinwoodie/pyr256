import pyR256

dpk1 = pyR256.driver(1, "COM5", 9600)
dpk1.open()
dpk1.close()