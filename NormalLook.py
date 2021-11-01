import maya.cmds as cmds

normalCnstrnt = "pSphere1"
selection = cmds.ls(sl = True)
for rom in selection:
    cmds.select(normalCnstrnt)
    cmds.select(rom, add= True)
    cmds.normalConstraint(w= 1, u =(1,0,0), aim = (0,1,0))
    cmds.delete("*normalConstraint*")
cmds.select( d = True)