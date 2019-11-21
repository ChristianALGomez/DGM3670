
import maya.cmds as cm


class calculator():
    def __init__(self):
        pass

    def Add(self, values):
        sum = 0
        for val in values:
            sum += val

        return sum

    def printStuff(self):
        print 'stuff'

    def Power(self, value, power):
        import math
        return math.pow(value, power)

    Power()

    def Sub(self, values):
        sum = values[0]
        for val in values[1:]:
            sum -= val
        return sum

    Sub([])

    def Div(self, values):
        sum = values[0]
        for val in values[1:]:
            sum = sum / val
        return sum

    Div([])

    def Mult(self, values):
        sum = values[0]
        for val in values[1:]:
            sum *= val
        return sum

    Mult([])

    def Mean(self, values):
        sum = 0
        size = len(values)
        for val in values:
            sum += val
        return sum / size

    Mean([])

    def Median(self, data):
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

