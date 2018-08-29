import random

choices = ["Rock", "Paper", "Scissors"]
playerScore = 0
computerScore = 0
tieScore = 0


def RockPaperScissors():
    computer = random.choice(choices)
    player = False
    global playerScore, computerScore, tieScore, winpercentagerounded

    while player == False:
        player = input("Rock, Paper, or Scissors?").capitalize()
        if player == computer:
            print("Tie! Try Again")
            tieScore += 1
            player = True

        elif player == "Rock":
            if computer == "Paper":
                print("You Lose!", computer, "covers", player)
                player = True
                computerScore += 1
            else:
                print("You Win!", player, "blunts", computer)
                player = True
                playerScore += 1

        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                player = True
                computerScore += 1
            else:
                print("You win!", player, "covers", computer)
                player = True
                playerScore += 1

        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "blunts", player)
                player = True
                computerScore += 1
            else:
                print("You win!", player, "cut", computer)
                player = True
                playerScore += 1
        else:
            print("You Lose! That's not a valid play. Check your spelling!")
            player = True
            computerScore += 1

    while player == True:
        print("Would you like to play again?")
        response = input("Yes or No?").capitalize()
        if response == "Yes":
            RockPaperScissors()
        else:
            print("Oh well, see you next time.")
            print("Players Total Wins ", playerScore)
            print("Computer Total Wins ", computerScore)
            print("Total Ties ", tieScore)
            playerwinpercentage = (playerScore / (playerScore + computerScore + tieScore)) * 100
            winpercentagerounded = round(playerwinpercentage, 2)
            print("Player Win Percentage", winpercentagerounded, "%")
        break


RockPaperScissors()
