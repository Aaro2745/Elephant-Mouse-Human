import random
from background import incsruct
wins = 0
losses = 0
gamestart=None
choiceinvalid=None
options=["foot","nuke","cockroach"]
menu=True

while menu==True:
    print("------------------------------FOOT, NUKE, COCKROACH---------------------------")
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
        print("Welcome to Foot, Nuke, Cockroach!")
        print("please choose the following:)")
        print("1. Foot")
        print("2. Nuke")
        print("3. Cockroach")
        playerschoice=input("Enter your choice: ")
        if playerschoice not in options:
                print("invalid choice")
                choiceinvalid=True
        while choiceinvalid is True:
                playerschoice=input("Enter your choice: ")
                if playerschoice not in options:
                    print("invalid choice")
                else:                choiceinvalid=False


    
        botchoice = random.choice(options)

        if playerschoice == "foot" and  botchoice == "cockroach":
            print("Foot squashes cockroach, You win!!!!!!!!!!!!!")
        elif playerschoice=="nuke " and botchoice=="foot:":
            print("Nuke obliterates Foot, You Win !!!!!!!!!!!!!")
            wins=wins+1
        elif playerschoice=="Cockroach:" and botchoice=="nuke":
            print("Cockroach survives  Nuke You Win!!!!!!!!!!!!")
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
        
             