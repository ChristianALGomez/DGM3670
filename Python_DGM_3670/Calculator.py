import maya.cmds as cm

def Add(values):
    '''
    Add two or more numbers together and returns result
    inoput: list of floats/int values
    return: float/int
    '''


    sum=0
    for val in values:
        sum += val

    return sum
Add([])

    #Add([])

    #sum = value1 + value2
    #return sum

    #return value1 + value2


def Power(value,power):
    import math
    return math.pow(value,power)
Power()



def Sub(values):
    sum = values[0]
    for val in values[1:]:
        sum -= val
    return sum
Sub([])

def Div(values):
    sum = values[0]
    for val in values[1:]:
        sum = sum / val
    return sum
Div([])

def Mult(values):
    sum = values[0]
    for val in values[1:]:
        sum *= val
    return sum
Mult([])

def Mean(values):
    sum = 0
    size = len(values)
    for val in values:
        sum += val
    return sum / size
Mean([])


def Med(values):
    // import statistics
    import math
    numorder = values
    size = len(numorder)
    median = 0

    if size / 2 != 0:
        temp = int(math.floor(size / 2))
        median = numorder[temp]
    if size % 2 == 0:
        temp = size / 2
        medianalt = temp - 1

        median = numorder[temp] + numorder[medianalt]
        median = median / 2
    return median


Med([1, 2, 3, 4, 5, 6, 7, 8])
