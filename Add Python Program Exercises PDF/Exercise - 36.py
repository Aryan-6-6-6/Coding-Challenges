# Exercise - 36:  Reverse String

def reverseString(text):
    if not text:
        return ''
    
    return text[::-1]

print(reverseString("Hello"))

# Test Cases
assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
assert reverseString('12345') == '54321'