# Factorial using recursiom
def factorial(num):
    if (num == 0 or num ==1):
        return 1
    else:
        z = num * factorial(num - 1)
        print(z)
        return z
        return num * factorial(num - 1)

num = int(input("Enter a number : "))
if num < 0:
    print("Please enter a valid number!")
    exit()
else:
    a = factorial(num)
    print(f"Factorial of {num} is : {a}")

# Fibonacci using recursion
def fibonacci(n):
    '''Take input and print fibonacci series'''
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number : "))
if n < 0:
    print("Please enter a valid number!")
else:
    print("Fibonacci Series : ")
    for i in range(n):
        print(fibonacci(i))
