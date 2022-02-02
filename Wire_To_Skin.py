#select wire first then wiredMesh :) , Made By : Vishal Nagpal, Gmail : vishalnagpal878@gamil.com
#change skincluster name of wire "skinCluster1" to skinCluster2
# one tip distance could be euual to weight
import maya.cmds as cmds

start_time = time.time()
selection0 = cmds.ls(sl=True)

cmds.duplicate(selection0[0], n = 'Get_Test_Crv')

AllAtO = cmds.listAttr('Get_Test_Crv',l =True)
for x in AllAtO:
    cmds.setAttr('Get_Test_Crv.'+x, l = 0)
    
cmds.makeIdentity(a = True )
spamSS =cmds.getAttr('Get_Test_Crv.spans')
cmds.select(d = True)

#------------------------------------------------------Find_SkinCluster


Meeshjnts = cmds.skinCluster(selection0[1], inf = True, q = True)
cmds.setAttr(Meeshjnts[0]+'.liw', 1)
#------------------------------------------------------Find_crv_Jnt

Aljnts = cmds.skinCluster(selection0[0], inf = True, q = True)
#------------------------------------------------------addInflunce_other_Jnts

for gfs in Aljnts:
    cmds.select(selection0[1])
    cmds.skinCluster(edit=True,ai=gfs,lw = 1)

#------------------------------------------------------Find_crv_Jnt_for Vertex
def fndJnt(verNam):
    myJnt = []
    for fg in Aljnts:
        getJntt = cmds.skinPercent('skinCluster1',selection0[0]+'.controlPoints['+str(verNam)+']' , tv = True, q = True,t = fg )
        if getJntt == 1.0:
            myJnt.append(fg)
            return myJnt

#------------------------------------------------------
for xx in range(spamS):
    whichVer = []
    PostionP = cmds.getAttr('Get_Test_Crv.controlPoints['+str(xx)+']')[0]
    verName = cmds.select(selection0[0]+'.cv['+str(xx)+']', r =True)
    cmds.setAttr(selection0[0]+'.cv['+str(xx)+'].xValue', 1)
    whichVer.append(xx)
    cmds.select(selection0[1])
    cmds.duplicate(n = 'Get_Test_Mesh')
    cmds.setAttr(selection0[0]+'.cv['+str(xx)+'].xValue', 0)
    cmds.select(selection0[1])
    polyCount = cmds.polyEvaluate( v=True )


    set_01Z = []
    set_02Z = []
    diff    = []
    AlWeight= []

    #-----------------------------------------------------set1
    for d in range(int(polyCount)):
        cmds.select(selection0[1]+'.vtx['+str(d)+']', r = True)
        Attr = '%.3f'%cmds.xform(selection0[1]+'.vtx['+str(d)+']', q =True, ws = True, t=True)[1]
        set_01Z.append((Attr))
        
    for b in range(int(polyCount)):
        cmds.select('Get_Test_Mesh'+'.vtx['+str(b)+']', r = True)
        Attrs = '%.3f'%cmds.xform('Get_Test_Mesh'+'.vtx['+str(b)+']', q =True, ws = True, t=True)[1]
        set_02Z.append((Attrs))

    #---------------------------------------------------getDiff
    for o in range(int(polyCount)):
        dif = float(set_02Z[o]) - float(set_01Z[o])
        diff.append((dif))
        AlWeight.append((diff[o]/1.0))
    #---------------------------------------------------addSkin
    for R in range(int(polyCount)):
        cmds.setAttr(Meeshjnts[0]+'.liw', 0)
        
        if AlWeight[R] != 0.0:

            cmds.skinPercent( 'skinCluster2','Normal.vtx['+str(R)+']', tv=(fndJnt(whichVer[0])[0], AlWeight[R]))
         

    cmds.setAttr(selection0[0]+'.cv['+str(xx)+'].xValue', 0)
    cmds.delete('Get_Test_Mesh')
cmds.delete('Get_Test_Crv')

#---------------------------------------------------Total_Time         
print("--- %s seconds ---" % (time.time() - start_time))


