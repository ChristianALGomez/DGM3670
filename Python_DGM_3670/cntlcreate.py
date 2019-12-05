import maya.cmds as cm

def CntlCreate():

    sels = cm.ls(sl=True)

    for i in sels:
        cntl = [cm.createNurbsCircleCtx]
        cm.matchTransform('sels', 'cntl[i]')

CntlCreate()
