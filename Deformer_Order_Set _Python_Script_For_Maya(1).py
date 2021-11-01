 import maya.cmds as cmds



firstDfm       =  'squash1'

secoundDfm     =  'bend1'



selection = cmds.ls( sl = True)



for obj in selection:

    

    suum = cmds.pickWalk( d = 'down')

    print suum

    

    cmds.reorderDeformers(firstDfm, secoundDfm, suum )

