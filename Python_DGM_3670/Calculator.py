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

    #sum = value1 + value2
    #return sum

    #return value1 + value2


    sum=0
    for val in values:
        if type(val) == 'int' or type(val) == 'float':
            sum += val
        else:
            print "your a dummy. you cant add", val

    return sum

def Power(value,power):
    import math
    return math.pow(value, power )
