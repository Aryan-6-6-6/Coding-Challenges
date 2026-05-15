# Exercise - 21: Validate Date
from Exercise_20 import isLeapYear 

# def checkDay(year,month,day):
#     if month < 1 or month > 12 or day < 1:
#        return False
    
#     days_in_month = [31,29 if isLeapYear(year) else 28, 31,30,31,30,31,31,30,31,30,31]

#     return day <= days_in_month[month-1] # as index start from 0
        
# def isValidDate(year,month,day):
#     return checkDay(year,month,day)

# book Way
def isValidDate(year, month, day):
    # Check if month is invalid
    if month not in range(1, 13):
        return False
    
    # Leap year check for Feb 29
    if isLeapYear(year) and month == 2 and day == 29:
        return True
    
    # February (non-leap year case left)
    if month == 2:
        return 1 <= day <= 28
    
    # Months with 31 days
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= day <= 31
    
    # Months with 30 days
    if month in (4, 6, 9, 11):
        return 1 <= day <= 30
    
    
    return False
 

# test Case
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
 assert isValidDate(d.year, d.month, d.day) == True
