# Secret Code Language
#           Rules:

# Coding:
# If : the word contain at least three characters remove the first letter 
# And append it at the end now open three random character at the starting and the end
# Else :  simply reverse the string

# Decoding:
# If word contain less than three character reverse it
# else removal three random character from start  and end. Now reverse the last letter and append append it to the beginning
str_original = input("Enter a string: ")
print("Length is : ",len(str_original))

if not str_original.isprintable():
    raise ValueError("The input contains non-printable characters like emojis or special symbols. Please enter a valid string with alphabets, numbers, and spaces only.")

if(len(str_original) == 1):
    raise ValueError("Use atleast 2 Characters")
if(len(str_original) == 2):
    # Convert str to list for append and remove methods
    str_converted  = list(str_original)
    # Reversed Original String
    str_converted.reverse() # It returns nothing
    print("Opposite is : ", ''.join(str_converted)) # to show in string form

print("Enter 1 - Coding | 2 - Decoding")
option = int(input("Choose : "))

match(option):
    
    # Encoding
    case 1:
        import random # to produce random string
        import string # for individual alphabets
        
        # Convert str to list for append and remove methods
        list1  = list(str_original)
        
        # Copy first index
        list2 = list1[0]
        
        # Add first character to the last
        list1.append(list2)
        
        # Removes the first element
        remove_element = list1.pop(0)
        
        # List with removed first element
        list1.append(remove_element)
        # Add 3 time single character at the end
        randomEnd = [] # creating list
        for i in range(0,3):
            randomEnd.append(random.choice(string.ascii_lowercase))
        print("Random End Characters : ",randomEnd)
        
        # Add 3 time single character at the beginning
        randomBeginning = [] # creating list
        for i in range(0,3):
            randomBeginning.append(random.choice(string.ascii_lowercase))
        print("Random Beginning Characters: ",randomBeginning)

        # String Methods
        list1.extend(randomEnd) # to add all elements
        list3 = randomBeginning + list1 # add at the beginning
        
        # print to check code
        print("Sample : ", ''.join(list3))

    case 2:
        # Convert str to list for append and remove methods
        list1 = list(str_original)
        
        # Remove 3 characters from the beginning and end
        list1 = list1[3:-3]
        
        
        # Move the last character to the beginning
        last_char = list1.pop(len(list1) -1)
        list1.insert(0, last_char)
        
        # Print the decoded string
        print("Decoded string: ", ''.join(list1))
        
    case _:
        print("Enter a valid number!")
    
    


