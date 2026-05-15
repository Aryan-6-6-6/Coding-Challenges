# Exercise - 23:  99 Bottles of Beer

for i in range(100,0,-1):
    if i > 1:
        print(f"{i-1} bottles of beer on the wall,")
        print(f'{i-1}  bottles of beer,')
        print("Take one down, \nPass it around,")
    if i == 1:
        print("No more bottles of beer on the wall!")
    
