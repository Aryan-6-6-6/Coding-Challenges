def factorial(num):
    fact = 1
    for i in range(1,num + 1):
        fact *= i
    return fact

num = int(input("Enter a number : "))

if num < 0:
    print("Please enter a valid number!")

else:

    result = factorial(num)
    print(f"Factorial of {num} is : {result}")
