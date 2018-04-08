from random import randint
import numpy as np

def random():
    return randint(1, 4)


def performNextState(position):
    switcher = {
        1: [position[0] - 1, position[1]],
        2: [position[0] + 1, position[1]],
        3: [position[0], position[1] + 1],
        4: [position[0], position[1] - 1]
    }
    return switcher.get(random())


def checkValidState(nextAction):
    return (0 <= nextAction[0] and nextAction[0] < envRows) and (0 <= nextAction[1] and nextAction[1] < envColumns)


env = [['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
envRows = len(env)
envColumns = len(env[0])

entryPoint = env[2][0]
rewardPosition = [1, 3]

initialState = [2, 0]
previousState = []

while initialState != rewardPosition:
    tempState = performNextState(initialState)

    if checkValidState(tempState) and tempState != initialState and previousState != tempState:
        previousState = initialState
        initialState = tempState
        env[initialState[0]][initialState[1]] = "*"
        print(np.matrix(env))
        print('\n')
