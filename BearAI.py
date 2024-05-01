import pyglet
import random
import common

currentPosition = "Outside"
previousPosition = ""
AiNum = 20

def generateRandomSeedBear():
    random.seed(None)

def bearMovement():
    global currentPosition
    global previousPosition
    
    if currentPosition == "Outside":
        currentPosition = "Door"
        print("Door!")
    else:
        currentPosition = "Outside"
        #common.gameState = "Attacked"
        print("Attacked by Bear!")
    
    print(currentPosition)

def bearAI(dt):
    global currentPosition
    
    if common.gameState == "in game":
        if currentPosition == "Outside":
            randAi = random.randint(1, (21 - AiNum))
        else:
            randAi = 20
        
        if randAi == 20 or randAi == (21 - AiNum):
            bearMovement()