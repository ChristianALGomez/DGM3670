import maya.cmds as cm

def CntlCreate():

    sels = cm.ls(sl=True)

    for i in sels:
        cntl = cm.circle(nr=(0,0,1), c=(0,0,0))
        cm.matchTransform (cntl ,i)

CntlCreate()