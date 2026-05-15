# Exercise - 12:  S M A L L E S T & B I G G E S T

def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    else:
        min = numbers[0] # assume
        for i in numbers:
            if min > i:
                min = i
        return min
    
# ASSert are nothing but test cases
assert getSmallest([1, 2, 3]) == 1 # change 1 to any other number to check
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
