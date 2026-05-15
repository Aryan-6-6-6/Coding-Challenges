# Find Area ot Volume of  Cone  

print("Click : ")
print("1 - Cylinder | 2 - Cone ")
option = int(input("Choose Option : "))

match option:

    case 1:
        radius = float(input("Enter Radius : "))
        height = float(input("Enter Height :"))
        print("1 - Area | 2 - Volume")
        option = int(input("Choose Option : "))
        # Cases for different options
        match option:
            case 1:
                area = 2 * 3.14 * radius * (height + radius)
                print("Area of Cylinder is : ",area)

            case 2:
                volume = 3.14 * radius * radius * height
                print("Volume of Cylinder is : ",volume)

            case _:
                print("Invalid Number!!!")

    case 2:
        radius = float(input("Enter Radius : "))
        length = float(input("Enter Length ; "))
        print("1 - Area(TSA) | 2 - Volume")
        option = int(input("Choose Option : "))
        # Cases for different options
        match option:
            case 1:
                area = 3.14 * radius * (radius + length)
                print("Area of Cone is : ",area)

            case 2:
                height = float(input("Enter Height : "))
                volume = (3.14 * radius *radius * height)
                print("Volume of Cone is : ",volume)

            case _:
                print("Invalid Number!!!")
    # For wrong input
    case _:
        print("Invalid Number!!!")




