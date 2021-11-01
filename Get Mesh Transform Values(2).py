### This script helps you to select and give a list of objects which have Value on it ###

import maya.cmds as cmds



selection = cmds.ls(sl = True)



MyValueList =[]



if selection == []:

    raise ValueError ("Not selected anything is yet")





for obj in selection:



    MyobjTX = '%s.%s' % (obj,'tx')

    MyobjTY = '%s.%s' % (obj,'ty')

    MyobjTZ = '%s.%s' % (obj,'tz')

    MyobjRX = '%s.%s' % (obj,'rx')

    MyobjRY = '%s.%s' % (obj,'ry')

    MyobjRZ = '%s.%s' % (obj,'rz')

    MyobjSX = '%s.%s' % (obj,'sx')

    MyobjSY = '%s.%s' % (obj,'sy')

    MyobjSZ = '%s.%s' % (obj,'sz')





    tX = cmds.getAttr(MyobjTX)

    tY = cmds.getAttr(MyobjTY)

    tZ = cmds.getAttr(MyobjTZ)

    rX = cmds.getAttr(MyobjRX)

    rY = cmds.getAttr(MyobjRY)

    rZ = cmds.getAttr(MyobjRZ)

    sX = cmds.getAttr(MyobjSX)

    sY = cmds.getAttr(MyobjSY)

    sZ = cmds.getAttr(MyobjSZ)

    

    if tX == 0.0 and tY == 0.0 and tZ == 0.0 and rX == 0.0 and rY == 0.0 and rZ == 0.0 and sX == 1.0 and sY == 1.0 and sZ == 1.0:

        continue

    else:

        MyValueList.append(obj)

cmds.select(d = True )





TotalError = len(MyValueList)

ErrorValue = '%s' % (TotalError)



if MyValueList == []:

    

    print 'Sab bhadiya h bhai'

    

else:

    cmds.select(MyValueList)

    print "Total Values Error :", TotalError

    print MyValueList

    print '____________________________________________________________________________________________________________________________________________________________'

    raise ValueError(ErrorValue+" Values Error")



        

#

#

#

#

#

#

#

#

#

#

#

#___________________________________________________________________________________________________________________________________________________________

