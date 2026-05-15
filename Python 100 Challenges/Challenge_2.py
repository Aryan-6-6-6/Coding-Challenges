# Challenge 2 Description:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(num):
    # Base Case
    if (num == 0):
        return 1
    # Recursive case
    else:
        num = num * factorial(num - 1)
        return num


num = int(input("Enter a number : "))

# calling Function
result = factorial(num)

print(result)