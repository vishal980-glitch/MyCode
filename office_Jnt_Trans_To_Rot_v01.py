import maya.cmds as cmds


sel = cmds.ls(sl = 1)
cmds.select(sel, hi = 1 )
sel2 = cmds.ls(sl = 1)
cmds.duplicate(sel2)
duplicateSel = cmds.ls(sl = 1)
cmds.group(n = "VN_group")
cmds.rename(duplicateSel[0], sel[0])
cmds.select(d = 1)


for f in sel2:
    cmds.rename('VN_group|'+ f, 'pre_'+ f)


for f in range(len(sel2)):
    if f < len(sel2)-1:
        cmds.select('VN_group|'+ 'pre_'+ sel2[f+1], sel2[f])
        cmds.aimConstraint(o= (0, 0, 0), w = 1, aim=(1, 0, 0), u =( 0, 1, 0), wut= "vector", wu = (0, 1, 0))
        
        cmds.select('VN_group|'+ 'pre_'+ sel2[f], sel2[f])
        cmds.pointConstraint(o =(0, 0, 0), w =1)
        
        cmds.delete(sel2[f]+ '_aimConstraint1')
        cmds.delete(sel2[f]+ '_pointConstraint1')

cmds.select('VN_group|'+ 'pre_'+ sel2[len(sel2)-1], sel2[len(sel2)-1])
cmds.pointConstraint(o =(0, 0, 0), w =1)

cmds.delete(sel2[len(sel2)-1]+ '_pointConstraint1')

cmds.delete('VN_group')


for f in sel2:
    shapes = cmds.listRelatives(f)
    if shapes ==  None:
        cmds.setAttr(f+".rotateX", 0)
        cmds.setAttr(f+".rotateY", 0)
        cmds.setAttr(f+".rotateZ", 0)
        cmds.setAttr(f+".jointOrientX", 0)
        cmds.setAttr(f+".jointOrientY", 0)
        cmds.setAttr(f+".jointOrientZ", 0)
        
cmds.select(d = 1)

cmds.select(sel, hi = 1 )
cmds.makeIdentity( a= 1, t= 1, r= 1, s= 1, n= 0, pn= 1)
cmds.select(d = 1)
