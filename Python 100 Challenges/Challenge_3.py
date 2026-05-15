# Challenge 3 Description:
# With a given integral number n, write a program to generate a dictionary.
# Which contains (i, i*i) such that is an integral number between 1 and n (both included).
# Then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

dict1 = {}

n = int(input("Enter How many key: value pair you want : "))
for i in range(1, n + 1):
    dict1.setdefault(i, i * i)  # i is key, default is value

print(dict1)

