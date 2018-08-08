# Project #1: Dice Rolling Simulator
# Generates random number from 1-6
#July 8 2018

import random #random class
again = True #boolean again
while (again==True):
    #print a random number
    print (random.randint(1,6))
    #ask if user wants to roll again
    answer = input("Would you like to roll again? (y/n)")
    if (answer=="n"):
        again=False
print ("Thank you!")
