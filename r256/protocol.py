# DT PROTOCOL SYNTAX
CMD_START = "/"
CMD_RUN = "R"
CMD_END = "\r"

# POSITIONING
CMD_FORWARD = "P"
CMD_BACKWARD = "D"
CMD_HOME = "Z"
CMD_SETPOS = "z"
CMD_SETPOL = "f"
CMD_SETDIR = "F"
CMD_TERM = "T"
CMD_ABS = "A"
CMD_PJD = "D"		# Distance for pulse jog mode untested
CMD_VEL = "V"		# Units: usteps/sec
CMD_ACC = "L"		# Units: usteps/sec^2

# CURRENT
CMD_RCUR = "m"
CMD_HCUR = "h"

# LOGIC
CMD_SLOOP = "g"
CMD_ELOOP = "G"
CMD_DLY = "M"		# Units: msec
CMD_HLT = "H"
CMD_SKP = "S"
CMD_STR = "s"
CMD_EXE = "e"
CMD_RPT = "X"
CMD_ERS = "?9"

# STEPPING
CMD_MODE = "n"
CMD_DIV = "j"		# Values: 1, 2, 4, 8, 16, 32, 64, 128, 256
CMD_OFS = "o"

# DRIVERS
CMD_IO = "J"		# Range: 0-3

# QUERY
QRY_POS = "?0"
QRY_STVEL = "?1"
QRY_SWSPD = "?2"
QRY_STSPD = "?3"
QRY_IO = "?4"
QRY_CRVEL = "?5"
QRY_DIV = "?6"
QRY_OFS = "?7"
QRT_STS = "Q"
QRY_VER = "&"
QRY_EXE = "$"

# COMMUNICATION
CMD_BAUD = "b"		# Values: 9600, 19200, 38400
