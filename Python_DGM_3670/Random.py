import maya.cmds as cm
from random import uniform as rand


def spawnRand():
    objList = cm.ls( sl = True)
    mRX = 10
    mRX2 = -10
    mRY = 10
    mRY2 = -10
    mRZ = 10
    mRZ2 = -10
    rRX = (360)
    rRY = (360)
    rRZ = (360)
    dupR = 25
   
    
    for i in range(dupR):
        
        cm.move(rand(mRX,mRX2),rand(mRY,mRY2),rand(mRZ,mRZ2), objList)
        cm.rotate(rand(0,rRX),rand(0,rRY),rand(0,rRZ), objList)
        cm.instance(objList)

    
    

spawnRand()