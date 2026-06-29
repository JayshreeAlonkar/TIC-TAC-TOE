import random

player_score=0
computer_score=0
round = 0
choices=["rock","paper","scissors"]

#result
while True:
    player=input("Enter rock ,paper or scissors : ").lower()
    if player not in choices:
       print(" Invalid choice! please choose rock ,paper or scissors")
       continue
    computer=random.choice(choices)
    print("Computer choice : ", computer)
    if player == computer:
        print("Its a tie ! ")
    elif (
        (player == "rock" and computer == "scissors") or 
        (player == "scissors" and computer == "paper") or 
        (player == "paper" and computer == " rock")):
        player_score += 1
        print("You Win🎉🎉")

    else:
        print("Computer wins !")
        computer_score += 1
    round += 1
    print ("Scores")       
    print ("round : ", round)     
    print("player : ",player_score)
    print("computer : ",computer_score) 
    
    
    if player_score==3 or computer_score==3:
        if player_score>computer_score:
            print ("You Won the game !")
        else:
            print(" computer Won the game ! ")    
    again=input("Do you want to play again ? (y/n): ").lower()
    if again !="y":
        print("Thanks for playing !")
        break      

