import maya.cmds as cmds

class Toolbox():
    def __init__(self):
        self.window_name = "mnToolbox"

    def create(self):
        self.delete()

        self.window_name = cmds.window(self.window_name)
        self.m_column = cmds.columnLayout(parent= self.window_name, adjustableColumn=True)
        cmds.button(label="MyButton",
                    command=lambda *args: cmds.polySphere(radius=2))

        cmds.button(label="Yellow",
                    command=lambda *args: self.colorControl('yellow'))

        cmds.button(label="Red",
                    command=lambda *args: self.colorControl('red'))


        self.color = cmds.textField(parent=self.m_column)
        cmds.button(parent=self.m_column,
                    label='Change Color',
                    command=lambda *args: self.colorBtn())


        cmds.button(p= self.m_column, label='Select Everything Ever',
                    command=lambda *args: self.selectBtn())

        cmds.button(p=self.m_column, label='Ball',
                    command= lambda *args: self.ballBtn())
        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def ballBtn(self):
        import sceneTools
        sceneTools.ball()

    def selectBtn(self):
        import sceneTools
        sceneTools.selectAll()

    def colorBtn(self):
        value = cmds.textField(self.color, query=True, text= True)
        self.colorControl(value)
        cmds.textField(self.color, edit=True, text="")




    def colorControl(self, colorname):
        sels = cmds.ls(sl=True)
        if colorname == 'yellow':
            color = 17
        elif colorname == 'blue':
            color = 6
        elif colorname == 'red':
            color = 13
        elif colorname == 'black':
            color = 1
        elif colorname == 'green':
            color = 7
        elif colorname == 'pink':
            color = 9
        elif colorname == 'brown':
            color = 10
        elif colorname == 'neon green':
            color = 14
        else:
            color = 5

        for sel in sels:
            shapes = cmds.listRelatives(sel, children=True, shapes=True)

            for shape in shapes:
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, color)


myTool = Toolbox()
myTool.create()

