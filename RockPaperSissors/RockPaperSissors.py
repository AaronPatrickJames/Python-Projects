#Weekly Python final project
from random import *
import time
from playsound import playsound

def main():
    Intro()
    RockPaperSissorsBackEnd()
        

def RockPaperSissorsBackEnd():
    counter = 0
    WinnerCheck = 1
    PlayerScore = 0
    ComputerScore = 0
    Games = GamesAmmount()
    while WinnerCheck == 1:
        if counter == 0:
            counter = counter + 1
            Games = Games
        else:
            Games = Games + 1
                
        while Games != 0:
            print("Rounds Left: " + str(Games))
            ROSHAMBO()
            Play = Player()
            Comp = Computer()
            point = CenteralProcessing(Play, Comp)
            if point == 0:
                PlayerScore = PlayerScore + 1
            elif point == 2:
                ComputerScore = ComputerScore + 1
            print("The Score is " + str(PlayerScore) + " for you, and " + str(ComputerScore) + " for the computer")
            print("")
            Games = int(Games) - 1
        WinnerCheck = Winner(PlayerScore, ComputerScore)
    print("")
    print("Thank you for playing")
    playsound("Win.mp3")

def Rock():
    print("Rock")
    print("")
    
def Paper():
    print("Paper")
    print("")

    
def Sissor():
    print("Scissors")
    print("") 

def Computer():
    #1=Rock, #2=Paper, #3=Sissors
    print("Computer")
    CompPick = randint(1,3)
    CompOption = {1 : Rock,
                2 : Paper,
                3 : Sissor}
    CompOption[CompPick]()
    return CompPick
    
def Player():
    PlayerPick = input("Please enter a number, 1=Rock, 2=Paper, 3=Sissors")
    print(" ")
    while int(PlayerPick).isdigit() != True:
        print("Must be a digit")
        print("")
        PlayerPick = input("Please enter a number, 1=Rock, 2=Paper, 3=Sissors")
        PlayerPick = int(PlayerPick)
        print("")
    if type(PlayerPick) != str:
        PlayerPick = int(PlayerPick)
            
    if int(PlayerPick) > int(3) or int(PlayerPick) < int(1):
        print("Number Must be between 1 and 3")
        print("Becase you tried to cheat. You will be auto assigned ROCK")
        Rock()
        PlayerPick = 1
    else:
        PlayerPick = int(PlayerPick)
        PlayerOption = {1 : Rock,
                        2 : Paper,
                        3 : Sissor}

        PlayerOption[PlayerPick]()
    return PlayerPick

        
def GamesAmmount():
    Games = 0
    while Games == 0:
        print("Must be an odd number of games...")
        print("For selection, please enter one...")
        Games = input("How many games would you like to play? ")
        print("")
        if Games.isdigit() == True:
            if ((int(Games) % 2) == 0):
                print("Must be an odd number")
                Games = 0
            else:
                Games = Games

        else:
            print("Must be numbers!!!!!!! NO LETTERS!!!!!!")
            print("")
            Games = 0
        return Games

def IntroSound():
    MusicComp = randint(1,2)
    if MusicComp == 1:
        playsound("KeyClick.wav")
    else:
        playsound("KeyClick2.wav")

def IntroTimeRand():
    RandomTime = randint(1,4)
    if RandomTime == 1:
        time.sleep(.05)
    elif RandomTime == 2:
        time.sleep(.005)
    elif RandomTime == 3:
        time.sleep(.1)
    else:
        time.sleep(.45)

def CenteralProcessing(PlayerInput, ComputerInput):
    if PlayerInput == 1:
        if ComputerInput == 1:
            return 1
        elif ComputerInput == 2:
            return 2
        else:
            return 0
    elif PlayerInput == 2:
        if ComputerInput == 1:
            return 0
        elif ComputerInput == 2:
            return 1
        else:
            return 2
    else:
        if ComputerInput == 1:
            return 2
        elif ComputerInput == 2:
            return 0
        else:
            return 1

def Winner(P1, C1):
    if P1 == C1:
        return 1
    elif P1 > C1:
        print("YOU ARE THE WINNER")
        return 0
    else:
        print("YOU SUCK EGGS LOSER")
        return 0
    
def Intro():
    FirstLine = ["H", "E", "L", "L", "O", ",", " ", "L", "E", "T", "S", " ", "P", "L", "A", "Y", " ", "A", " ", "G", "A", "M", "E"]
    SecondLine = ["I", " ", "A", "M", " ", "T", "H", "E", " ", "C", "O", "M", "P", "U", "T", "E", "R"]
    ThirdLine = ["R", "O", "C", "K", " ", "P", "A", "P", "E", "R", " ", "S", "C", "I", "S", "S", "O", "R", "S"]
    
    FirstLen = len(FirstLine)
    FirstCount = 0
    while FirstCount != FirstLen:
        print(FirstLine[FirstCount], end="")
        IntroSound()
        IntroTimeRand()
        FirstCount = FirstCount + 1
    print("")
    playsound("D:\python\RockPaperSissors\KeyClick3.wav")
    SecondLen = len(SecondLine)
    SecondCount = 0
    while SecondCount != SecondLen:
        print(SecondLine[SecondCount], end="")
        IntroSound()
        IntroTimeRand()
        SecondCount = SecondCount + 1
    print("")
    playsound("D:\python\RockPaperSissors\KeyClick3.wav")
    ThirdLen = len(ThirdLine)
    ThirdCount = 0
    while ThirdCount != ThirdLen:
        print(ThirdLine[ThirdCount], end="")
        IntroSound()
        IntroTimeRand()
        ThirdCount = ThirdCount + 1
    print("")

def ROSHAMBO():
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(2)
    print("SHOOT!")
main()
