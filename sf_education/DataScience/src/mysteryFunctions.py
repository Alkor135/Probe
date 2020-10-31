import numpy as np

def mysteryFunctionOne(inputParams):
    result= []
    for x in inputParams:
        y = x*x
        result.append(y)
    return result

def mysteryFunctionTwo(inputParams):
    result = []
    m = 2
    b = 3
    for x in inputParams:
        y = m*x + b
        result.append(y)

    return result


def mysteryFunctionSmall(inputParams):
    result=[]
    m = 2
    b = 3
    for x in inputParams:
        y = m*x + b + np.random.rand()
        result.append(y)
    return result

def mysteryFunctionLarge(inputParams):
    result=[]
    m = 2
    b = 3
    for x in inputParams:
        y = m*x + b + np.random.rand()*x
        result.append(y)
    return result