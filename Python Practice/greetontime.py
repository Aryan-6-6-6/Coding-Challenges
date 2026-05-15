import time
name = input("Enter your name : ")

currentTime = time.strftime("%H:%M:%S")

print("Current Time is : ",currentTime)

# Converts string into int
currentHour = int(time.strftime("%H"))
c = name.capitalize()

# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59

# Condition to check
if(currentHour >= 4 and currentHour < 12):
    print("Good Morning ",c)

elif(currentHour >= 12 and currentHour < 17):
    print("Good Afternoon ",c)

elif(currentHour >= 17 and currentHour < 21 ):
    print("Good Evening ",c)

else:
    print("Good Night ",c)