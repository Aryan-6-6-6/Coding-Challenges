# Exercise - 15: Median
from math import floor, ceil

def median(numbers):
    if not numbers:  # check for empty list
        return None
     
    numbers.sort()  # in-place sort
    num_length = len(numbers)
    
    if num_length % 2 != 0:
        # Odd length: return the middle element
        mid_idx = num_length // 2
        return numbers[mid_idx]
    else:
        # Even length: return the average of the two middle elements
        mid1 = numbers[num_length // 2 - 1]
        mid2 = numbers[num_length // 2]
        return (mid1 + mid2) / 2

# Test Cases
assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
 random.shuffle(testData)
 assert median(testData) == 6

