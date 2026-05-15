# Challenge 6 Description:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

C = 50
H = 30


old_D = input("Enter value of D separated by comma ").split(',') # if not use , so it will not print the output

# Convert String to Integer
D = [int(z) for z in old_D]

print(D)
for i in D:
    Q = math.sqrt((2 * C * i) / H)
    print(round(Q))