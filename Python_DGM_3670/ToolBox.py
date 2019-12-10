import maya.cmds as cm

class ToolboxCG():
    def __init__(self):
        self.window_name = "mnToolbox"

    def create(self):
        self.delete()

        self.window_name = cm.window(self.window_name)
        self.m_column = cm.columnLayout(parent= self.window_name, adjustableColumn=True)
        
        cm.button(label="BallSpawn",
                    command=lambda *args: cm.polySphere(radius=2))
        
        cm.button(p=self.m_column, label='cntlSpawn',
                    command=lambda *args: self.cntlSpawn())


        self.color = cm.textField(parent=self.m_column)
        cm.button(p=self.m_column, label='colorChange',
                    command=lambda *args: self.cC())
                    
                    
        cm.button(p=self.m_column, label='Random',
                    command=lambda *args: self.Rand())
                    
        self.name = cm.textField(parent=self.m_column)
        self.padding = cm.intField(parent=self.m_column)
        self.suffix = cm.textField(parent=self.m_column)
        cm.button(p=self.m_column, label='Rename',
                    command=lambda *args: self.Re())
                    
        cm.button(p=self.m_column, label='Locator',
                    command=lambda *args: self.locCreate())
        
        
        cm.showWindow(self.window_name)
    def delete(self):
        if cm.window(self.window_name, exists=True):
            cm.deleteUI(self.window_name)


    def cC(self):
        import colorControl
        cCV = cm.textField(self.color, q=True, text=True)
        colorControl.colorControl(cCV)
            
    def cntlSpawn(self):
        import cntlcreate
        cntlcreate.CntlCreate()
        
    def Rand(self):
        import Random
        Random.spawnRand()
        
    def Re(self):
        import Rename
        name = cm.textField(self.name, q=True, text=True)
        padding = cm.intField(self.padding, q=True, value=True)
        suffix = cm.textField(self.suffix, q=True, text=True)
        Rename.Rename(name, padding, suffix)
        
    def locCreate(self):
        import crateLocator
        crateLocator.cenGs()
        


myTool = ToolboxCG()
myTool.create()