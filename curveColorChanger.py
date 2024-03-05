import maya.cmds as cmds


#change this number to desired maya index color number
newColor = 17 #6=blue, 13=red, 14=green, 17=yellow, pink=20

selected = cmds.ls(sl=True)
shapes = cmds.listRelatives(shapes=True)

for each in shapes:
    cmds.setAttr('{}.overrideEnabled'.format(each), 1)
    cmds.setAttr('{}.overrideColor'.format(each), newColor)