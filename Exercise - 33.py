# Exercise - 33: Comma Formatted numbers

def commaFormat(numbers):
    convert = str(numbers)
    if len(convert) <= 3:
        return convert
    
    result = ""
    count = 0
    for ch in reversed(convert):   # go from right side
        result = ch + result
        count += 1
        if count % 3 == 0 and count != len(convert):
            result = ',' + result
    return result  

# test Cases
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
