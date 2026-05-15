# Exercise - 9: Chess Square Color

def getChessSquareColor(column, row):
    if (column + row) % 2 == 0:
        return "White"
    else:
        return "Black"

row = int(input("Enter row no(0-7) : "))
column = int(input("Enter column no(0-7) : "))

print(getChessSquareColor(column, row))
