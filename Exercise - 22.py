# Exercise - 22: Rock,Paper, Scissors
def rpsWinner(player1,player2):
    selector = ['rock','paper','scissor']
    result_matrix = [

        ["tie","player two","player one"],
        ["player one","tie","player two"],
        ["player two","player one","tie"]
    ]

    if player1 not in selector or player2 not in selector:
        return False

    else:
        p1_idx = selector.index(player1)
        p2_idx = selector.index(player2)

        return result_matrix[p1_idx][p2_idx]

while True:
    print("Write 'exit' when you want to leave")
    # Users Input
    player1 = input("Enter(Rock,Paper,Scissors) : ").lower()
    if player1 == 'exit':
        print("Exitted successfully from the loop!")
        break
    player2 = input("Enter(Rock,Paper,Scissors) : ").lower()
    if player2 == 'exit':
        print("Exitted successfully from the loop!")
        break

    print(rpsWinner(player1,player2))
    