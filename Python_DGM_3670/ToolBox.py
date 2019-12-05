import maya.cmds as cm


class Toolbox():
    def __init__(self):
        self.window_name = "cgToolbox"


def create(self):
    self.delete()

    self.window_name = cm.window(self.window_name)
    self.m_column = cm.columnLayout(p=self.window_name, adj=True)
    cm.button(label - 'MyButton'
              c=lambda *args: cm.polySphere(r=2)

    cm.showWindow(self.window_name)


def delete(self):
    if cm.window(self.window_name, exists=True):
        cm.deleteUI(self.window_name)


myTool = Toolbox()
myTool.create()


