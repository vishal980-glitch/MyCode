  ###for Deformer



import maya.cmds as cmds







firstDfm       =  'bend1'



secoundDfm     =  'squash1'







selection = cmds.ls( sl = True)







for obj in selection:



    



    suum = cmds.pickWalk( d = 'down')



    



    cmds.reorderDeformers(firstDfm, secoundDfm, suum )







###############################################################



  ###for SkinCluster ( skinCluster* name should be as *_SkinCluster )



import maya.cmds as cmds







firstDfm       =  'bend1'







selection = cmds.ls( sl = True)







for obj in selection:







    secoundDfm = '%s_SkinCluster' % (obj)



    



    suum = cmds.pickWalk( d = 'down')



    



    cmds.reorderDeformers(firstDfm, secoundDfm, suum )





