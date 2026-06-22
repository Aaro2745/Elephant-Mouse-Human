import random
from background import incsruct
wins = 0
losses = 0
gamestart=None
choiceinvalid=None
options=["elephant","mouse","human"]
menu=True

while menu==True:
    print("------------------------------Elephant, Mouse, Human---------------------------")
    print("1,PLAY")
    print("2,HOW TO PlAY")
    print("3,EXIT")
    menuchoice=input("What would you like to do?: ")
    if menuchoice=="1":
        gamestart=True
        menu=False
    elif menuchoice=="2":
        incsruct()
    elif menuchoice=="3":
        print("Goodbye!")
        menu=False









# Game
    while gamestart==True:
        botchoice = random.choice(options)
        print("Welcome to elephant, mouse, human!")
        print("please choose the following:)")
        print("1. Elephant")
        print("2. Human")
        print("3. Mouse")
        playerschoice=input("Enter your choice: ")
        if playerschoice not in options:
                print("invalid choice")
                choiceinvalid=True
        while choiceinvalid is True:
                playerschoice=input("Enter your choice: ")
                if playerschoice not in options:
                    print("invalid choice")
                else:                choiceinvalid=False


    
        

        if playerschoice == "elephant" and  botchoice == "human":
            print(" You win!!!!!!!!!!!!!")
        elif playerschoice=="human" and botchoice=="mouse":
            print(" You Win !!!!!!!!!!!!!")
            wins=wins+1
        elif playerschoice=="mouse" and botchoice=="elephant":
            print(" You Win!!!!!!!!!!!!")
            wins=wins+1
        elif playerschoice==botchoice:
            print("It's a tie :(")
        else:
            print("You lose :(")
            losses=losses+1
        exitgame=input("Do you want to play again?(Y/N:")
        if exitgame=="y":
            gamestart=True
        elif exitgame=="n":
            gamestart=False
            print("Thanks for playing!")
            
        menu=True
        
             