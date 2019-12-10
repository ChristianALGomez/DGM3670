maya.cmds as cm

def colorControl(color):
    sels = cm.ls(sl=True)
        
    if color == 'black':
        color = 1
        
    elif color == 'gray':
        color = 3
        
    elif color == 'red':
        color = 4
        
    elif color == 'blue':
        color = 6
        
    elif color == 'green':
        color = 14
        
    elif color == 'brown':
        color = 10

    elif color == 'yellow':
        color = 17   
       
    else:
        color = 5 
        
    for sel in sels:
        shapes = cm.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cm.setAttr('%s.overrideEnabled' % shape, True)
            cm.setAttr('%s.overrideColor' % shape, color)
                
              

colorControl('green')