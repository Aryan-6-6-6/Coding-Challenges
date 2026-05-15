import random
import string

def generatePassword(length):
    if length < 12:
        length = 12

    # all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(all_chars, k=length))

    # validation counters
    isupper = islower = isdigit = isspecial = 0

    for ch in password:
        if ch.isupper():
            isupper += 1
        if ch.islower():
            islower += 1
        if ch.isdigit():
            isdigit += 1
        if not ch.isalnum():
            isspecial += 1

    if isupper >= 1 and islower >= 1 and isdigit >= 1 and isspecial >= 1:
        return password
    else:
        # regenerate until valid
        return generatePassword(length)


# Test Cases
assert len(generatePassword(8)) == 12  # should auto-expand to 12
pw = generatePassword(14)
assert len(pw) == 14

hasLowercase = any(ch.islower() for ch in pw)
hasUppercase = any(ch.isupper() for ch in pw)
hasNumber    = any(ch.isdigit() for ch in pw)
hasSpecial   = any(not ch.isalnum() for ch in pw)

assert hasLowercase and hasUppercase and hasNumber and hasSpecial

print("Generated password:", pw)
