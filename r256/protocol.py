# DT protocol syntax
CMD_START = "/"
CMD_RUN = "R"
CMD_END = "\r"

# Movement commands
MOVE_POSITIVE = "P"
MOVE_NEGATIVE = "D"
MOVE_ABSOLUTE = "A"
INITIALIZE = "Z"
TERMINATE = "T"

# Driver commands
CMD_IO = "J" # Range: 0-3

# Movement settings
SET_POSITION = "z"
SET_HOME_DIRECTION = "f"
SET_MOVE_DIRECTION = "F"
SET_PJOG_DISTANCE = "B"
SET_VELOCITY = "V"
SET_ACCELERATION = "L"
SET_MODE = "n"
SET_RESOLUTION = "j"
SET_OFFSET = "o"

# Amperage settings
SET_REST_CURRENT = "m"
SET_HOLD_CURRENT = "h"

# Communication settings
CMD_BAUD = "b" # Values: 9600, 19200, 38400

# Logic commands
LOOP_START = "g"
LOOP_END = "G"
DELAY = "M"
HALT = "H"
SKIP = "S"
CMD_STR = "s"
EXECUTE = "e"
REPEAT = "X"
CMD_ERS = "?9"

# Query commands
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

# Address dictionary
ADDRESS = [
    '0': '@',
    'A': ':',
    'B': 'C',
    'C': '<',
    'D': '=',
    'E': '>',
    'F': '?',
    'all': '_'
    ]
