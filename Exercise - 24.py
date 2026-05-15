# Exercise - 24: Every 15 minute

def minute(hour):
    for minute in ["00","15","30","45"]:
        print(f"{hour} : {minute} {meridiem}")

for meridiem in ['am','pm']:
    for hour in [str(i) for i in range(0,12)]:
        if hour == '0':
            minute(12)
            continue
        minute(hour)
