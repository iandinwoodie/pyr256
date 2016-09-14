import pyR256

dpk1 = pyR256.driver(1, "COM5", 9600)
dpk1.open()
dpk1.move(2000)
dpk1.status()
dpk1.io(1,1)
dpk1.close()