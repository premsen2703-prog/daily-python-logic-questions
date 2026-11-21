# Python Bitwise Operators
# Bitwise operators in Python are used to perform operations on individual bits (0 and 1) of integer numbers.

# Before learning them, remember:
# - 0 means OFF
# - 1 means ON
# Python has 6 bitwise operators.
# 1. Types of Bitwise Operators
# Operator	Name	Meaning
# &	AND	Both bits must be 1
# \|	OR	At least one bit must be 1
# ^	XOR	Bits must be different
# ~	NOT	Reverses the bits
# <<	Left Shift	Shifts bits to the left
# >>	Right Shift	Shifts bits to the right

bitwise_and = 5 & 3  # 0101 & 0011 = 0001 (1)
bitwise_or = 5 | 3   # 0101 | 0011 = 0111 (7)
bitwise_xor = 5 ^ 3  # 0101 ^ 0011 = 0110 (6)
bitwise_not = ~5     # ~0101 = 1010 (-6 in two's complement)#means 
#for a 4-bit representation, ~5 would be 1010, which is -6 in decimal (two's complement representation).
left_shift = 5 << 1  # 0101 << 1 = 1010 (10)
right_shift = 5 >> 1 # 0101 >> 1 = 0010 (2)

