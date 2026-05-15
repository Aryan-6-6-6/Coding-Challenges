height = float(input("Enter Your Height(in m) : "))
weight = float(input("Enter Your Weight(in kg) : "))

bmi = weight / pow(height,2)
print("Your BMI is : ",bmi)
# Check height for BMI using if else
if (bmi < 15):
    print("Dude! You are in Starvation")
    
elif(bmi > 15.0 and bmi < 17.5):
    print("Dude! You are in Anorexic")

elif(bmi >= 17.6 and bmi < 18.5):
    print("Dude! You are in Underweight")
elif(bmi >= 18.6 and bmi < 24.9):
    print("Dude! You are Ideal")
elif(bmi >= 25 and bmi < 29.9):
    print("Dude! You are OverWeight")
elif(bmi >= 30 and bmi < 39.9):
    print("Dude! You are Obese")
else:
    print("Dude! You are Morbidly Obese")
    