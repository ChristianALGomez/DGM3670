import maya.cmds as cm

testScores = ['Bill',86,'Nancy',94,'Bob',75,'Sarah',100]
names=[]
scores=[]

for i in range(len(testScores)):
    if (i%2==0):
        scores.append(testScores[i])
    else:
        names.append(testScores[i])

print 'Names:', names
print 'Scores:', scores


