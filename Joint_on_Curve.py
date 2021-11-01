 # First run all script and select Curve and Run CurveJnt()

import maya.cmds as cmds

    

def CurveJnt():

    

    selection01 = cmds.ls( sl = True)

    selection01 = cmds.ls( sl = True)

    if cmds.objExists(selection01[0]+'_Jnt*'):

        cmds.select(selection01[0]+'_Jnt*')

        cmds.delete()

        cmds.select(selection01[0], r = True)

    

    if len(selection01) == 1:

        

        '%s' %(selection01[0])

        cmds.duplicate(rr = True)

        cmds.makeIdentity( apply=True )

        

        selection = cmds.ls( sl = True)

        selectionShape = cmds.pickWalk(d = 'down')

        cmds.select(cl= True)

        

        '%s' %(selection[0])

        

        cvs = cmds.getAttr(selection[0]+'.cp',s=1)

        StartWdZero = cvs

        

        i  = 0

        

        

        while i < StartWdZero:

            controlPoints = 'controlPoints['+('%s' %(i))+']'

            Xvalue = cmds.getAttr (selectionShape[0]+"."+ controlPoints+ ".xValue")

            Yvalue = cmds.getAttr (selectionShape[0]+"."+ controlPoints+ ".yValue")

            Zvalue = cmds.getAttr (selectionShape[0]+"."+ controlPoints+ ".zValue")

            cmds.joint(n = selection01[0]+'_Jnt_', p = (Xvalue,Yvalue,Zvalue))

            cmds.select(cl= True)

            

            i = i + 1

        

            

        cmds.select(selection[0], r = True)

        cmds.Delete()

    

    else:

        cmds.error('Select one Curve at a time ')



#addnew thing...

#parent or not parent joints

#joint or somthing else to create

    

