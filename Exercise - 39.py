# Exercise - 39: Collatz Sequence/ 3n + 1 problem

def collatz(startingNumber:int)->list:
    l = []
    # First/Returned element append here
    if startingNumber > 0:
        l.append(startingNumber)
    
    # Base Case
    if startingNumber <= 1:
        return l
    
    # Recursive Case
    else:
        n = startingNumber
        # If element is even
        if n % 2 == 0:
            result = n // 2 
            return l + collatz(result)
        # For Odd elements 
        else:
            result = (3 * n) + 1
            return l + collatz(result)


# print(collatz(10))

# Test Cases
assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random
random.seed(42)
for i in range(1000):
 startingNum = random.randint(1, 10000)
 seq = collatz(startingNum)
 assert seq[0] == startingNum # Make sure it includes the starting number.
 assert seq[-1] == 1 # Make sure the last integer is 1.
