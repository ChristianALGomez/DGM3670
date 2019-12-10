import maya.cmds as cm


def Rename(name, padding, suffix):
    ObjSel = cm.ls(selection=True)
    for count,obj in enumerate(ObjSel):
        cm.rename(obj, name +'_'+ str(count + 1).zfill(padding) +'_'+ suffix)
Rename()