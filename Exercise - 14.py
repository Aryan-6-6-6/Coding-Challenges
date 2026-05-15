# Exercise - 14: A V E R A G E

def average(numbers):
    sum = 0
    for idx,i in enumerate(numbers,start = 1):
       sum += i
    return sum/idx
# Test Cases
assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
 random.shuffle(testData)
 assert average(testData) == 2
