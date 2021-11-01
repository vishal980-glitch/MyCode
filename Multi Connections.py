### This Script help to Create multi connections for attribute like scale, translate, rotate ###

###https://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectAttr.html###

import maya.cmds as cmds





'''Destination = Please Select'''

source         = "pSphere1"

Attr           = 'scale'   #example: scale, translate, rotate



selection = cmds.ls( sl = True)



for obj in selection:

    

    objList = '%s.%s' % (obj,Attr)

    

    Main = '%s.%s' % (source,Attr)

    

    cmds.connectAttr( Main, objList)

