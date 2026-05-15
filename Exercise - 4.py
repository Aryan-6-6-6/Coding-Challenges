# Exercise - 4: Area and Volume of a Cylinder
import math
print("Enter the radius of the cylinder:")
radius = float(input())
print("Enter the height of the cylinder:")
height = float(input())
area = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius**2 * height
print(f"Surface Area of the cylinder: {area}")
print(f"Volume of the cylinder: {volume}")

