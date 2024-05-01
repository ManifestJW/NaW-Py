import pyglet
import random
import common

currentPosition = "Outside View"
previousPosition = ""
AiNum = 6

def generateRandomSeedRobber():
    random.seed(None)

def robberMovement():
    global currentPosition
    global previousPosition
    
    if currentPosition == "Outside View":
        randAi = random.randint(1, 3)

        previousPosition = currentPosition
        
        if randAi == 1:
            currentPosition = "Outside Garden"
            print("Garden!")
        elif randAi == 2:
            currentPosition = "Outside Left Entrance"
            print("Left Entrance!")
        else:
            currentPosition = "Outside Right Entrance"
            print("Right Entrance!")
    else:
        currentPosition = "Outside View"
        #common.gameState = "Robbed"
        print("Robbed!")
    
    print(currentPosition)

def robberAI(dt):
    if common.gameState == "in game":
        randAi = random.randint(1, 20)

        if AiNum >= randAi:
            robberMovement()