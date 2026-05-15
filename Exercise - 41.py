# Exercise - 41: Rot 13 Encrption

def rot13(text:str) -> str:
    if not text:
        return ''
    
    # Creating a Dictionary to store next 12 letters of lower alphabets
    sorted_letter = {}

    for new_val,i in enumerate(range(26),start = -13):
        key = chr(i + 97)
        value = i + 97 + 13
        if i > 12:
            sorted_letter[key] = chr(new_val + 97)
            
        else:
            sorted_letter[key] = chr(value)

    
    result = ''
    for ch in text:
        if ch.isupper():
            result += sorted_letter[ch.lower()].upper()
        elif ch.islower():
            result += sorted_letter[ch]
        # All other letters except alphabets
        else:
            result += ch

    return result

# Test Cases
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
