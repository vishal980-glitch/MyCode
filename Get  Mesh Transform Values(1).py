import maya.cmds as cmds



selection = cmds.ls(sl = True)



for obj in selection:



    MyobjT = '%s.%s' % (obj,'t')



    MyobjR = '%s.%s' % (obj,'r')



    MyobjS = '%s.%s' % (obj,'s')



    MyobjN = '%s' % (obj)







    translation = cmds.getAttr(MyobjT)



    Rotatation = cmds.getAttr(MyobjR)



    Scale = cmds.getAttr(MyobjS)



    print MyobjN , (translation+ Rotatation +Scale)



print "Total Selected Object :", len(selection)

