# Convert temperature from Celsius to Fahrenheit using function parameters
def convert(censius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius : "))
# calling function with arguments
tmp = convert(celsius)

print("Temperature in Fahrenheit is : ",tmp)

# Calculate Simple Interest using function with parameters
def SI(principle, rate, time):
    simple_interest = (principle * rate * time) / 100
    return simple_interest

principle = int(input("Enter Principle amount : "))

rate = float(input("Enter Rate of interest(p.a) : "))

time = int(input("Enter Time in years : "))

if SI(principle, rate, time) > principle:
    print("Enter valid year or interest. Try again!")

print(f"Simple interest is {SI(principle,time,rate)}")

print("Your total payment is : ", principle + SI(principle,time,rate))