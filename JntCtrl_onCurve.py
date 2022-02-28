import maya.cmds as cmds

def VNJntCtrl():
    crv = cmds.ls(sl=True)
    cmds.duplicate(n = 'Test_Jnt_01')
    AllAt = cmds.listAttr('Test_Jnt_01',l =True)
    
    if AllAt != None :
        
        for G in AllAt:
            cmds.setAttr('Test_Jnt_01.'+G, l = 0)
        
    cmds.makeIdentity(a = True )
    
    
    #----get vert count
    numSpans = cmds.getAttr(crv[0]+'.spans')
    degree = cmds.getAttr(crv[0]+'.degree')
    form = cmds.getAttr(crv[0]+'.form')
    if form == 2:
    	numCVs = numSpans
    if form == 0:
    	numCVs = numSpans + degree
    #----end get vert count
    
    
    cmds.select(d = True)
    
    for j in range(numCVs):
        PostionP = cmds.getAttr('Test_Jnt_01.controlPoints['+str(j)+']')
        cmds.select(d = True)
        cmds.joint(n = "Jnt_1",p = (PostionP[0][0],PostionP[0][1],PostionP[0][2]) )
        cmds.circle(n = "Test_Crv_"+str(j+1))
        cmds.group(n = "Test_Crv_Grp_"+str(j+1))
        cmds.parentConstraint('Jnt_'+str(j+1),'Test_Crv_Grp_'+str(j+1), mo =0)
        cmds.delete('Test_Crv_Grp_'+str(j+1)+'_parentConstraint1')
        cmds.parentConstraint('Test_Crv_'+str(j+1),'Jnt_'+str(j+1), mo =1)
        cmds.setAttr('Test_Crv_'+str(j+1) + '.overrideEnabled', 1)
        cmds.setAttr('Test_Crv_'+str(j+1) + '.overrideColor', 18)
    
    cmds.delete('Test_Jnt_01')

VNJntCtrl()
#coment : now it can create more then 10 jnts and ctrl
