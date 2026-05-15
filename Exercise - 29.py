# Exercise - 29: Pyramid Drawing

def drawPyramid(height:int):
    for row in range(height):
            print(" " * (height-row-1) + '#' * ((row * 2) + 1))

height = int(input("Enter Height : "))
drawPyramid(height)

