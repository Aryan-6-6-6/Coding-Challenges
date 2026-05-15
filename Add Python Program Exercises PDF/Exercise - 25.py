# Exercise - 25: Multiplication Table

print("    |",end = "") # for header row

# Header row
for i in range(1,11):
    print(f"{str(i).rjust(4)}", end = "")

# print divider row
print("\n----+" + '-' * 40)

# print table row
for i in range(1,11):
    print(f'{str(i).rjust(3)}' + " |", end = "")
    for j in range(1,11):
        print(f"{str(i*j).rjust(4)}", end = "")
    print()
