import random
gameChoice = ["Rock", "Paper", "Scissor"]
while True:
    print("********************")
    print("Stone Paper Scissor Game>>>")
    yourScore, compScore = 0,0
    for i in range(1,6):
        print(f"Round {i} Start:")
        print("Select any option:")
        print("Rock(r)","Paper(p)","Scissor(s)", sep="\n")
        print("")
        yourChoice = input("Enter your choice: ")
        if yourChoice == 'r':
            print("********************")
            print(f"Round {i} Result:")
            print("You selected Rock")
            yourChoice = "Rock"
        elif yourChoice == 'p':
            print("********************")
            print(f"Round {i} Result:")
            print("You selected Paper")
            yourChoice = "Paper"
        elif yourChoice == 's':
            print("********************")
            print(f"Round {i} Result:")
            print("You selected Scissor")
            yourChoice = "Scissor"
        else:
            print("Please select a valid choice!")
            break
        compChoice = random.choice(gameChoice)
        print(f"Computer selected: {compChoice}")
        if yourChoice == compChoice:
            print("This Round is Draw")
            print("********************")
        elif (yourChoice == "Rock" and compChoice == "Scissor") or (yourChoice == "Scissor" and compChoice == "Paper") or (yourChoice == "Paper" and compChoice == "Rock"):
            print("You Win this Round")
            print("********************")
            yourScore+=1
        else:
            print("Computer Win this Round")
            print("********************")
            compScore+=1
    if yourChoice>compChoice:
        print("You Won the Game!")
        print(f"Your Score: {yourScore}, Computer Score: {compScore}")
        print("********************")
    elif compScore>yourScore:
        print("Computer Won the Game!")
        print(f"Your Score: {yourScore}, Computer Score: {compScore}")
        print("********************")
    else:
        print("Match Draw!")
        print(f"Your Score: {yourScore}, Computer Score: {compScore}") 
        print("********************")   
    gameContinue = input("Want to Play this game again? (yes/exit): ")
    if gameContinue == "yes" or gameContinue == "YES" or gameContinue == "Yes":
        continue
    else:
        print("********************")
        print("Thanks for Playing this Game!")
        print("********************")
        break
