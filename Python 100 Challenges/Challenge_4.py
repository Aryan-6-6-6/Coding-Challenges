# Challenge 4 Description:
# Write a program which accepts a sequence of comma-separated numbers from console.
# also generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

n = int(input("How many numbers you want tpo display : "))

list1 = []
for i in range(1, n + 1):
    num = int(input(f"Enter {i} number : "))
    list1.append(num)

# print as a list
print(list1)

# convert list into tuple
tup = tuple(list1)
print(tup)