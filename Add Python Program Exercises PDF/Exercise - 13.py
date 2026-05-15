# Exercise - 13: S U M & P R O D U C T

def calculateSum(numbers):
    if len(numbers) == 0: return 0
    else:
        sum = 0
        for i in numbers:
            sum += i
        return sum

def calculateProduct(numbers):
    if len(numbers) == 0: return 1
    else:
        product = 1
        for i in numbers:
            product *= i
        return product


# Test Cases
assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
