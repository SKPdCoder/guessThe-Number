# -*- coding: utf-8 -*-
"""
Author:Skpdcoder

This is a code created to play the game of guessing the number betwen user and computer.

At the game beginning the user is instructed to think a number between 0 and 100.

And then after delay the computer starts guessing the number.
the user has to input "Y" for a correct guess or "H" for a number guessed greater then user's number.
or "L" for a number guessed lesser then user's number.

the game continues till the computer guesses the correct number.

At the end When the computer guesses the correct number it Displays "How many guesses it took to guess the number".


"""

import random
import time


low=0
high=100
count=1



userNum=print("Please think a number between {} and {}!\n".format(low,high))
time.sleep(2)
guess=random.randrange(low,high)
print("READY!!\n")
time.sleep(1)


def guessGame(count,low,high,guess):
    
    guessPrint="My number-{} guess is {}!!".format(count,guess)
    gameInstruc="If my guess is correct,type 'Y'!!\nIf my guess is higher then  your number,type 'H'!!\nIf my guess is lower then your number,type 'L'!!\n\n"
    finalPrint="\nI guessed your number in {} attempts!!\nSo you thought {} as your number!!".format(count,guess)
    
    print(guessPrint)
    userInput=input(gameInstruc)
    
    
    if userInput=="H" or userInput=="h":
        count+=1
        high=guess
        guess=random.randrange(low,high)
        guess=int((low+high)/2)
        guessGame(count,low,high,guess)
    elif userInput=="L" or userInput=="l":
        count+=1
        low=guess
        guess=random.randrange(low,high)
        guess=int((low+high)/2)
        guessGame(count,low,high,guess)
    elif userInput=="Y" or userInput=="y":
        count+=1
        print(finalPrint)
        
            
            
guessGame(count,low,high,guess)            
        
        
    
    
    

    
    


