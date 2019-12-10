import maya.cmds as cm


def cenGS():
    sels = cm.ls(selection=True)

    if len(sels) > 1:
        dups = cm.duplicate(sels)
        cm.polyUnite(sels)
        cm.rename('polySurface1', 'dups')
        

        bb = cm.xform('dups', q=True, bb=True, ws=True)
        xmax = bb[0]
        xmin = bb[3]
        ymax = bb[1]
        ymin = bb[4]
        zmax = bb[2]
        zmin = bb[5]
       
        x = (xmax + xmin) / 2
        y = (ymax + ymin) / 2
        z = (zmax + zmin) / 2
        
        cm.spaceLocator(p=(x, y, z))
        cm.delete('dups', ch=True)
        cm.delete('dups')

    elif len(sels) == 1:
        Loc = cm.spaceLocator(p=(0, 0, 0))
        cm.matchTransform(Loc, sels)


cenGS()