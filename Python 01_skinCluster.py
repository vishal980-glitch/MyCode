### http://download.autodesk.com/us/maya/2011help/Commandspython/skinCluster.html ###
import maya.cmds as cmds


cmds.select(d=True)
cmds.joint(p=(-3.0, 0.0, -12.0))
cmds.joint(p=(-3.0, 0.0, -5.0))
cmds.joint(p=(1.0, 0.0, 5.0))
cmds.joint(p=(6.0, 0.0, 10.0))
cmds.polyPlane(w=20.0,h=20.0,sx=25,sy=25)

cmds.skinCluster('joint1', 'pPlane1', dr=4.5)### -dropoffRate 1.0

cmds.undo();
cmds.skinCluster('joint1','joint3','pPlane1', tsb=True)### -toSelectedBones

cmds.skinCluster('skinCluster1', e = True, mi = 3)### -maximumInfluences 0

cmds.select('pPlane1')
cmds.skinCluster(edit=True, ai ='joint2')### -addInfluence String

cmds.skinCluster('skinCluster1', query=True, inf=True)### -influence String (Query Arg Optional)

cmds.curve(d=3, p=[(2.0, 0.0, -7.0),(5.0, 0.0, -4.0),(6.0, 0.0, 1.0),(6.0, 0.0, 4.0),(5.0, 0.0, 6.0)],k=[0,0,0,1,2,2,2])
cmds.skinCluster('skinCluster1',edit=True, ai ='curve1')
cmds.skinCluster('skinCluster1',inf='curve1', q=True, ns =True)### -nurbsSamples 0
cmds.skinCluster('skinCluster1',e=True,inf='joint3', dr=5.0)
cmds.skinCluster('skinCluster1', inf='joint3', query=True, dr=True)
