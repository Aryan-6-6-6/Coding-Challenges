# List for answers
z = ["A", "A", "A", "C", "B"]  # Correct answers for the questions

earn = 0
chance = 2
count = 1

print("Rules of Playing:")
print("1. There are total 2 Chances.")
print("2. Total 5 Questions. Each Correct Answer Gives you a Reward.")
print("3. When there are 0 chances left, you can still play once. If the answer is incorrect, you will lose all your earnings.")

def incorrect():
    global chance  # For modifying the global chance variable
    print("Incorrect Answer!!")
    chance -= 1
    if chance == -1:
        print("No chances left! You lose all your earnings.")
        exit()
    else:
        print(f"You have {chance} chances left.")

while chance >= 0 and count <= 5:
    if count == 1:
        print("\nQuestion 1. Python is a _ language:")
        print("A. Low Level   B. Medium Level \nC. High Level  D. It's reptile bro")
        q1 = input("Choose any One option: ")
        if q1 == z[0]:
            print("Correct Answer. You Earned ₹1000")
            earn += 1000
        else:
            incorrect()

    elif count == 2:
        print("\nQuestion 2. Who Developed Python:")
        print("A. Guido Van Rossum  B. Ada Lovelace \nC. Dennis Ritchie  D. None of these")
        q2 = input("Choose any One option: ")
        if q2 == z[1]:
            print("Correct Answer. You Earned ₹3000")
            earn += 3000
        else:
            incorrect()

    elif count == 3:
        print("\nQuestion 3. What does HTML stand for?")
        print("A. HyperText Markup Language  B. HighText Machine Language \nC. HyperText Making Language  D. None of these")
        q3 = input("Choose any One option: ")
        if q3 == z[2]:
            print("Correct Answer. You Earned ₹5000")
            earn += 5000
        else:
            incorrect()

    elif count == 4:
        print("\nQuestion 4. Which company developed JavaScript?")
        print("A. Microsoft  B. Sun Microsystems  \nC. Netscape  D. Oracle")
        q4 = input("Choose any One option: ")
        if q4 == z[3]:
            print("Correct Answer. You Earned ₹10000")
            earn += 10000
        else:
            incorrect()

    elif count == 5:
        print("\nQuestion 5. What is the full form of CSS?")
        print("A. Creative Style Sheets  B. Cascading Style Sheets \nC. Computer Style Sheets  D. Centralized Style Sheets")
        q5 = input("Choose any One option: ")
        if q5 == z[4]:
            print("Correct Answer. You Earned ₹20000")
            earn += 20000
        else:
            incorrect()

    count += 1

# Final result
print(f"\nCongratulations! You finished the game with ₹{earn} earnings.")
