# Exercise - 8: Read/Write File

def writeToFile(fileName, fileFormat):
    print("Enter Data to add into File: ")
    fileData = input()
    
    with open(f"{fileName}.{fileFormat}", "w") as w:
        w.write(fileData)
    print("File created successfully!")


def appendToFile(fileName, fileFormat, fileAppend):
    with open(f"{fileName}.{fileFormat}", "a") as a:
        a.write(fileAppend)
    print("Data appended successfully!")


def readFromFile(fileName, fileFormat):
    with open(f"{fileName}.{fileFormat}", "r") as r:
        content = r.read()
    print("File content is:\n")
    print(content)


while True:
    print("\n1 - Write Data | 2 - Append Data")
    print("3 - Read Data  | 4 - Exit")
    option = int(input("Choose: "))

    match option:
        case 1:
            fileName = input("Enter File Name: ")
            fileFormat = input("Enter File Format: ")
            writeToFile(fileName, fileFormat)

        case 2:
            fileAppend = input("Enter Data to append into the file: ")
            fileName = input("Enter File Name: ")
            fileFormat = input("Enter File Format: ")
            appendToFile(fileName, fileFormat, fileAppend)

        case 3:
            fileName = input("Enter File Name: ")
            fileFormat = input("Enter File Format: ")
            readFromFile(fileName, fileFormat)

        case 4:
            print("Exiting program...")
            break

        case _:
            print("Enter a valid number!")
