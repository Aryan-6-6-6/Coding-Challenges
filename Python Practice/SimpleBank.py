print("Simple Bank System ")
print("What do you want :")
print("1 - Deposit Money | 2 - Withdraw Money")
print("3 - Check Balance | 4 - Exit")

option = 0
deposit = 0
# loop unit choose exit
while(option != 4):

    option = int(input("Choose an Option : "))

    # cases for different options
    match option:
        case 1:
            deposit = int(input("Enter the amount for deposit : "))
            # condition to check input
            if(deposit == 0):
                print("Nothing is deposited")

            elif(deposit > 0):
                print("Deposit successfully!")
                print("Your new balance is : ",deposit)

            else:
                print("Please enter a valid amount")


        case 2:
            withdraw = int(input("Enter the amount to withdraw : "))
            # Condition to check if bank have balance or not
            if(withdraw == 0):
                print("No amount is withdraw")

            elif(withdraw > 0):
                print("Withdrawal Successfully!")
                print("Your new balance is : ",deposit-withdraw)

        case 3:
            print("Your current balance is ",deposit)

        case 4:
                print("Thankyou for using!")

        case _:
            print("Invalid option. Please try again")

