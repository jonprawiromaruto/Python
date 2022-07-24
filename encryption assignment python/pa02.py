################################################################################
# Assignment: pa01 - Calculating an 8, 16, or 32 bit
#                    checksum on an ASCII input file
#
# Author: Jonathan Prawiromaruto
# Language: python
#
# python pa02.py i1.txt 8/16/32
#            or
# python3 pa02.py i1.txt 8/16/32
#
# To Execute: 
# python -> python pa02.py i1.txt 8
# where i1.txt is a test input file
# and '8' is the number of bits sample
#
# Class: CIS3360 - Security in Computing - Spring 2022
# Instructor: McAlpin
# Due Date: 04/03/2022
#
###############################################################################

import math
import binascii
import sys

# opening file through shell / terminal
file = sys.argv[1]
bit_count = sys.argv[2]
with open(file) as f:
    contents = f.read()
# closing file    
f.close()  

new_content = ""

for c, char in enumerate(contents):
  if c % 80 == 0:
    new_content += '\n'
  new_content += char

print(new_content.rstrip())

# convert to binary
temp = ''.join(format(ord(i), '08b') for i in contents)

# splitting bits to group of 4 bits
binArray = []
total = 0
n  = 8
for index in range(0, len(temp), n):
    binArray.append(temp[index : index + n])

# converting chars to ascii vals
ascii_values = []
for character in contents:
    ascii_values.append(str(ord(character)))

# adding all ascii values of characters in the list
for chars in range(len(ascii_values)):
  total += int(ascii_values[chars])

# 8 bit choice entered
if bit_count == '8':
  hexa8 = hex(total%256)
  print(f"8 bit checksum is {hexa8[2:]} for all {len(ascii_values)} characters\n")

# 16 bit choice entered
elif bit_count == '16':
  X_val = ""
  if len(ascii_values) % 2 != 0:
    ascii_values.insert(len(ascii_values), "88")
    X_val += 'X'
  # print(ascii_values)
  # initializing variables
  val1 = 0
  val2 = 0
  i = 0
  # making 2 separate group for 16 bits
  for chars in range(len(ascii_values)):
    if chars % 2 == 0:
      val1 += int(ascii_values[chars])
    else:
      continue
  for chars in range(len(ascii_values)):
    if chars % 2 != 0:
      val2 += int(ascii_values[chars])
    else:
      continue
  print(X_val)  
  print(f"16 bit checksum is {hex(val1%256)[2:]}{hex(val2%256)[2:]} for all {len(ascii_values)} characters")

# 32 bit choice entered
elif bit_count == '32':
  X_val = ""
  while len(ascii_values) % 4 != 0:
    ascii_values.insert(len(ascii_values), "88")
    X_val += "X"
  # print(ascii_values)
  # initializing variables
  val1 = 0
  val2 = 0
  val3 = 0
  val4 = 0
  i = 0
  # making 4 separate group for 32 bits
  for i in range(0, len(ascii_values), 4):
    val1 += int(ascii_values[i])

  for i in range(1, len(ascii_values), 4):
    val2 += int(ascii_values[i])

  for i in range(2, len(ascii_values), 4):
    val3 += int(ascii_values[i])

  for i in range(3, len(ascii_values), 4):
    val4 += int(ascii_values[i])
  print(X_val)
  print(f"32 bit checksum is {hex(val1%256)[2:]}{hex(val2%256)[2:]}{hex(val3%256)[2:]}{hex(val4%256)[2:]} for all {len(ascii_values)} characters")

# if user entered bit value other than 8/16/32 = Error message
else:
  print("Error! Valid checksum sizes are 8, 16, or 32")
  quit()


################################################################################
# I Jonathan Prawiromaruto (jo352524) affirm that this program is
# entirely my own work and that I have neither developed my code together with
# any another person, nor copied any code from any other person, nor permitted
# my code to be copied or otherwise used by any other person, nor have I
# copied, modified, or otherwise used programs created by others. I acknowledge
# that any violation of the above terms will be treated as academic dishonesty.
################################################################################