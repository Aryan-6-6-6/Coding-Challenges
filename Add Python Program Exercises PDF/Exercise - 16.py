# Exercise - 16: Mode
from collections import Counter

def mode(numbers):
    if not numbers:
        return None

    count = Counter(numbers)

    # To done it manually
    # freq = {}
    # for n in freq:
    #     if n in freq:
    #         freq[n] += 1
    #     else:
    #         freq[n]

    # Find the key(s) with the maximum frequency
    max_count = max(count.values())
    
    # If multiple values have the same max frequency, take the first one
    for key, value in count.items():
        if value == max_count:
            return key

# Test cases:
assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1

import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
