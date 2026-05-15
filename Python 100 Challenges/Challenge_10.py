# Challenge 10 description:
# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Solution:

str1 = input("Enter anything in alphabets : ")
# split where whitespace occur
str1 = str1.split()
# print original list 
print("Unsorted List: ",str1)
# sort to assign alphabetically
# sort is a mutable method
str1.sort()
print("\nSortedList: ",str1)

# remove same words using set
s2 = set(str1)
print("\nRemove same words : ",s2)

