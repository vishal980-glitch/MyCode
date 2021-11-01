 import maya.cmds as cmds





FileFullPathName = cmds.file(q=True, sn=True)



CurrentFileName = FileFullPathName.split('/')[-1]

FileFullPathNameSplit = FileFullPathName.split('/')

FileFullPathNameSplit.remove(CurrentFileName)



CurrentFileNamePath = '/'.join(FileFullPathNameSplit)



CurrentVersion = CurrentFileName[-6:-3]

NewVersion = int(CurrentVersion)+1



if NewVersion <= 9:

    Add = "00"

else:

    Add = "0"

    

ConvertIntoString1 = Add+"%s" % (NewVersion)

ConvertIntoString2 = '%s' % (ConvertIntoString1)



NewFileName = (CurrentFileName).replace(CurrentVersion,ConvertIntoString2)



NewFileFullPathName = ( CurrentFileNamePath, NewFileName)



NewName = '/'.join(NewFileFullPathName)



cmds.file(rename=NewName)

Type = cmds.file(q=True, type=True)

cmds.file(save=True, type=Type[0])

