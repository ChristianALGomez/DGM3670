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

def Median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2
median([])


def Mode(data):

    data = iter(data)
    pairs = Counter(data).most_common(1)
    try:
        return pairs[0][0]
    except IndexError:
        raise StatisticsError('no mode for empty data')(None)


def calculator(values, operations):
    if operations == 1:
        Add(values)
    elif operations == 2:
        Sub(values)
    elif operations == 3:
        Mult(values)
    elif operations == 4:
        Div(values)
    elif operations == 5:
        Power(values)
    elif operations == 6:
        Mean(values)
    elif operations == 7:
        Median(values)
    elif operations == 8:
        Mode(values)