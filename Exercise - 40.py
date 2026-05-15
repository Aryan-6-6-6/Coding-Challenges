# Exercise - 40: Merging two sorted list

def mergeTwoLists(list1 : list, list2 : list) -> list:
    mergedList = []
    i,j = 0,0

    # Traverse both list
    while i < len(list1) and j <    len(list2):
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
    
    # Adding remaining element(if any)
    while i < len(list1):
        mergedList.append(list1[i])
        i += 1
    while j < len(list2):
        mergedList.append(list2[j])
        j += 1
    
    return mergedList


print( mergeTwoLists([1, 3, 6], [5, 7, 8, 9]))

assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]


