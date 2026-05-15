# Exercise - 34: Uppercase Letters

def getUppercase(text:str) -> str:
    if not text:
        return text
    else:
        result = ""
        for ch in text:
            flag = 0
            for i in range(65,92):
                convert_lower = chr(i).lower()
                if  convert_lower == ch:
                    result += chr(i)
                    flag += 1
            if not flag:
                result += ch
        return result


print(getUppercase("hello world!"))

# Test Cases
assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''
