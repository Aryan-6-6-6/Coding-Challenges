# Exercise - 32: Convert String to Integer
def convertStrToInt(numStr: str) -> int:
    Digits_Str_To_Int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
                         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
    result = 0
    for ch in numStr:
        digit = Digits_Str_To_Int[ch]     # map char to int
        result = result * 10 + digit      # shift left and add digit

    print(result)
    print(type(result))
    return result

convertStrToInt("12345")
