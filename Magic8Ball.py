#Random 8 ball

from random import *
import os

def main():
    ball8 = ["Yes, of couse!", "Without a doubt, yes", "You can Count on it.", "For Sure!", "Ask me later.", "Im not sure.", "I can't tell you right now.", "Tell you after my nap.", "No Way!", "I don't think so.", "Without a doubt, no", "The answer is clearly NO.", "Not today Jack.", "Try asking again"]
    shake = ""
    while shake != "EXIT":
        UserInput = input("ask a question")
        randomNumber = RandomNumberGen()
        print(ball8[randomNumber])
        print("")
        shake = input("to exit type exit, other wise press enter")
        shake = shake.upper()

def RandomNumberGen():
    randomNumber = randint(0,13)
    return randomNumber

main()
