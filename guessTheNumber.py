# -*- coding: utf-8 -*-
"""
Author:Shekhar Kumar Patra

This is a file created to play the game of guessing the number between player and computer.

At the game beginning the user is instructed to think a number between 0 and 100.

And then after delay the computer starts guessing the number.
the user has to input "Y" for a correct guess or "H" for a number guessed greater then user's number.
or "L" for a number guessed lesser then user's number.

the game continues till the computer guesses the correct number.

At the end When the computer guesses the correct number it Displays "How many guesses it took to guess the number".


"""

import random  #imported the random module
import time    #imported the time module


low=0          #lower range for the numbers to be guessed
high=100      #higher range for the numbers to be guessed
count=1       #count is set for the guesses the computer has taken


# Here the user instruction is given for the player of the game 
userNum=print("Please think a number between {} and {}!\n".format(low,high))
time.sleep(2)
guess=random.randrange(low,high)   #the first guessis initiated using random function
print("READY!!\n")
time.sleep(1)

#here a function is defined for the game which will guess the number thought by the player
#Here the function is a recursive function which calls itself again and again
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
        
            
#function call is done in the main program            
guessGame(count,low,high,guess)            
        
        
    
    
    

    
    


