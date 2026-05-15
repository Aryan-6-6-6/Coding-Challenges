# Challenge 9 Description:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT    

print("Enter as many strings as you want.") 
while True:
    str1 = input()
    
    if(str1 == ""):
        print("\bEnd of input")
        break
    
    # Convert the string to uppercase
    print(str1.upper())