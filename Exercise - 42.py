# Exercise - 42: Bubble Sort

def bubbleSort(numbers):
    for i in range(len(numbers)):
        tmp = 0
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j+1]:
                # Swap
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
    return numbers

# Test Cases
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]

