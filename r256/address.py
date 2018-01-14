def assign(address):
    try:
        address = int(address)
        if address < 0 or address > 9:
            print(address, "out of bounds")
        elif address == 0:
            tag = '@'
        else:
            tag = str(address)
    except:
        if address == 'A':
            tag = ':'
        elif address == 'B':
            tag = 'C'
        elif address == 'C':
            tag = '<'
        elif address == 'D':
            tag = '='
        elif address == 'E':
            tag = '>'
        elif address == 'F':
            tag = '?'
        elif address == '*':
            tag = '_'
        else:
            print(address, "out of bounds")
    return tag

# QUADS AND PAIR ASSIGNMENTS
#PAIR_1 = "A"	# Drivers 1 & 2
#PAIR_2 = "C"	# Drivers 3 & 4
#PAIR_3 = "E"	# Drivers 5 & 6
#PAIR_4 = "G"	# Drivers 7 & 8
#PAIR_5 = "I"	# Drivers 9 & A
#PAIR_5 = "K"	# Drivers B & C
#PAIR_5 = "M"	# Drivers D & E
#PAIR_5 = "O"	# Drivers F & 0
#QUAD_1 = "Q"	# Drivers 1, 2, 3, & 4
#QUAD_2 = "U"	# Drivers 5, 6, 7, & 8
#QUAD_3 = "Y"	# Drivers 9, A, B, & C
#QUAD_4 = "]"	# Drivers D, E, F, & 0
