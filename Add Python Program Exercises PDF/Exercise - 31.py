# Exercise - 31: Convert Integer to string

def convertIntToString(integerNum):
    Digits_Int_To_Str = {0:'0', 1:'1' ,2 : '2',3 : '3',4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    
    result = ""
    while integerNum != 0:
        last_digit = integerNum % 10
        result += Digits_Int_To_Str[last_digit]
        integerNum //= 10

    result = result[::-1]
    print(result)
    print(type(result))

convertIntToString(12345)
