# Exercise - 27: Print Rectangle

def drawRectangle(width,height):
    for i in range(height):
        for j in range(width):
            print('#',end = "")
        print()

drawRectangle(101,100)
