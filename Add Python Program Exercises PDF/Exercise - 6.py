# Exercise - 6: Ordinal Suffix

def ordinalSuffix(n):
    # Special case: 11, 12, 13 → all get "th"
    # if 10 <= n % 100 <= 13:
    #     return str(n) + "th"
    
    # 1. Convert into string
    num_str = str(n)  
    
    # 11, 12, and 13 have the suffix th:
    if num_str[-2:] in ('11', '12', '13'):
        return num_str + 'th'

    # 2. Assign suffix using ends with
    if num_str.endswith('1'):  # we can use negative indexing as well
        return num_str + 'st'
    elif num_str.endswith('2'):
        return num_str + 'nd'
    elif num_str.endswith('3'):
        return num_str + 'rd'
    else:
        return num_str + 'th'
    

try:
    # User Input
    n = int(input("Enter number to assign suffix: "))
    result = ordinalSuffix(n)
    print(f"Result is: {result}")
except ValueError:
    print("Error is : Enter numbers only!")
except Exception as e:
    print("Error is :", e)
