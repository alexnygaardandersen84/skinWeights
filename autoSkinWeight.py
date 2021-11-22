######################################################################################################
#                                    
#                                   SKIN WEIGHT EXPORT AND IMPORT
#                                   
#                                       Alex Nygaard Andersen
#
######################################################################################################

#Import the different imports for working with Maya. 
#Maybe looking more into PyMel
import maya.cmds as cmds
import maya.mel as mel
import sys
import os

    
#This is the window UI 
def ImportAndExportSkinWeights():

    #Creating the window 
    win = 'ImportAndExportSkinWeights'
    if(cmds.window (win, exists = 1)):
        cmds.deleteUI(win)
    cmds.window(win, rtf = 1, w = 200, h = 280, t = win, s=1)

    #

    #Make sure to have a layout or else it wont run
    cmds.columnLayout (adj = 1)

    #selection
    #sele = cmds.ls (sl=True)[0]

    cmds.rowColumnLayout (nc = 2)
    cmds.setParent('..')
    #I will run the maya import command directly from the button click release
    #cmds.text(l=str(sele), align='center', h=70)
    cmds.button(l = 'exportSkin', c = 'import autoSkinWeight; reload(autoSkinWeight); autoSkinWeight.exportSkinWeights()', bgc=[0,1,1], h=70)
   # cmds.text(l=str(sele), align='center', h =70)
    cmds.text(l = '' , align='center', h =70 )
    cmds.button(l = 'importSkin', c = 'import autoSkinWeight; reload(autoSkinWeight); autoSkinWeight.importSkinWeights()', bgc=[1,1,0], h=70)

    #create button for creating folders
    cmds.text(l = '' , align='center', h =70 )
    cmds.textField('textBox')
    cmds.button(l = 'MakeFolder', c ='import autoSkinWeight; reload(autoSkinWeight); autoSkinWeight.makeFolder()', bgc=[1,0,1], h=70)
    
    #Launch UI
    cmds.showWindow(win)

#This is the export function
def exportSkinWeights():

    allSelection = cmds.ls(sl=True)
    for each in allSelection: 
        cmds.select(each, r= True)
        #Select the object you want to export
        selection = cmds.ls (sl=True)[0]
        selForPath = selection

        #This is for when there is a group that is also in the namespace. So it removes that and only selects the object. 
        sel = selection.split("|")[-1]
        #shapes = cmds.listRelatives(sel, ad=True)[0]


        #Get skinCluster information on the object
        saveSkinCluster = cmds.ls(cmds.listHistory(selection), type='skinCluster')[0]
        print (saveSkinCluster)


        #Make sure which path it should follow on the specific rig
        if cmds.listRelatives(selForPath, ap=True):
            selectRoot = cmds.select(ado=True)
            selForPath = cmds.ls (sl=True)[0]
            print (selForPath)

            if (selForPath == 'daniel_rig_grp'):
                print('DANIEL IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\daniel\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel)) 
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )

            elif (selForPath == 'mariko_rig_grp'):
                print('MARIKO IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\mariko\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel))
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )
                

            elif (selForPath == 'rig_grp'):
                print('SPIDER IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\spider\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel))
                print(pathForFiles)
                #try to use deformer instead of shape and find out how to find the skinClusters instead 
                #cmds.deformerWeights (str(sel)+'.json', ex=True, vc=True, df=saveSkinCluster, p = pathForFiles)
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )
                #print("Exported skinWeight for: {}".format(sel))
            #Do this in another file to check setup for groups in those files
        #elif(parentOfControl_grp == ''):
    
    
        #Making the names and saving it as a json file
        #incremental = cmds.scriptJob(ex=1, ro=True)
        #Maybe use textField instead, then people can just write the next number for export and the same with import. 
        incremental = 1
        for i in range(incremental):
            count = i+1
            deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), ex=True, df = saveSkinCluster,ig=True,vc=True, m="index", p = pathForFiles)


    '''


        increment = 1
        #increment = each
        #arr = [ord(x) for x in increment]
        #print (arr)
        #length = len(arr)
        #print (length)

        if os.path.isfile('.json') == True:
            for i in range(increment):
                i = i + 1   
                deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), ex=True, df = saveSkinCluster, vc=True, p = pathForFiles)

        else:         
            deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), ex=True, df = saveSkinCluster, vc=True, p = pathForFiles)
                
        print (i)
    '''    

            #deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), ex=True, sh=shapes, vc=True, p = pathForFiles)
        #while cmds.file((str(sel)+'_{}.json'.format(i)), q=True, ex=True):
                #i = i + 1
            
        
        #print(i)


def importSkinWeights():


    allSelection = cmds.ls(sl=True)
    for each in allSelection: 
        cmds.select(each, r= True)
        #Select the object you want to export
        selection = cmds.ls (sl=True)[0]
        selForPath = selection

        #This is for when there is a group that is also in the namespace. So it removes that and only selects the object. 
        sel = selection.split("|")[-1]
        #shapes = cmds.listRelatives(sel, ad=True)[0]


        #Get skinCluster information on the object
        saveSkinCluster = cmds.ls(cmds.listHistory(selection), type='skinCluster')[0]
        print (saveSkinCluster)


        #Make sure which path it should follow on the specific rig
        if cmds.listRelatives(selForPath, ap=True):
            selectRoot = cmds.select(ado=True)
            selForPath = cmds.ls (sl=True)[0]
            print (selForPath)

            if (selForPath == 'daniel_rig_grp'):
                print('DANIEL IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\daniel\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel)) 
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )

            elif (selForPath == 'mariko_rig_grp'):
                print('MARIKO IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\mariko\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel))
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )
                

            elif (selForPath == 'rig_grp'):
                print('SPIDER IT IS')
                pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\spider\\Scenefiles\\rig\\skinWeights\\{}_skinWeight".format(sel))
                print(pathForFiles)
                #try to use deformer instead of shape and find out how to find the skinClusters instead 
                #cmds.deformerWeights (str(sel)+'.json', ex=True, vc=True, df=saveSkinCluster, p = pathForFiles)
                window = cmds.window( title="Success!", iconName='Short Name', widthHeight=(300, 150) )
                cmds.columnLayout( adjustableColumn=True )
                cmds.text('You exported skinWeights for: {}'.format(sel), w = 60, h = 60)
                cmds.button( label='Close',al="center", command=('cmds.deleteUI(\"' + window + '\", window=True)') )
                cmds.setParent( '..' )
                cmds.showWindow( window )
                #print("Exported skinWeight for: {}".format(sel))
            #Do this in another file to check setup for groups in those files
        #elif(parentOfControl_grp == ''):
    
    
        #Making the names and saving it as a json file
        #incremental = cmds.scriptJob(ex=1, ro=True)
        #Maybe use textField instead, then people can just write the next number for export and the same with import. 
        incremental = 1
        for i in range(incremental):
            count = i+1
            deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), im=True, df = saveSkinCluster, ig=True,vc=True, m="index", p = pathForFiles)
            #deform = cmds.deformerWeights (str(sel)+'_{}.json'.format(i), ex=True, sh=shapes, vc=True, p = pathForFiles)
        #while cmds.file((str(sel)+'_{}.json'.format(i)), q=True, ex=True):
                #i = i + 1
            
        
        #print(i)



#Bug but not really - you have to select the object while creating a folder, so it can check to see which dir it has to go to. 
# Create path for folder structure 
def pathForFolder(pathForFiles):
    #Select the object you want to export
    sel = cmds.ls (sl=True)[0]
    selForPaths = sel
    print(selForPaths)

    #Make sure which path it should follow on the specific rig
    if cmds.listRelatives(selForPaths, ap=True):
        selectRoot = cmds.select(ado=True)
        selForPaths = cmds.ls (sl=True)[0]
        print (selForPaths)
        if (selForPaths == 'daniel_rig_grp'):
            print('DANIEL IT IS')
            pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\daniel\\Scenefiles\\rig\\skinWeights") 
        

        elif (selForPaths == 'mariko_rig_grp'):
            print('MARIKO IT IS')
            pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\mariko\\Scenefiles\\rig\\skinWeights")
         
            

        elif (selForPaths == 'rig_grp'):
            print('SPIDER IT IS')
            pathForFiles = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\03_production\\Assets\\char\\spider\\Scenefiles\\rig\\skinWeights")

    return pathForFiles



def makeFolder(*args):
    #Make folders depending on dir and naming
    userInput = cmds.textField('textBox', q=1, tx=1)
    Paths = pathForFolder(userInput)
    print ('{}_folder has been created').format(Paths)
    #Make warning if the file already exsits
    if os.path.isdir(userInput):
        cmds.warning("This folder already exsists")
        return
    else:
    #This is what tells the OS to create a new folder. It takes the path given and creates the name of what the user inputet. 
        os.chdir(Paths)
        os.makedirs(userInput)





#TO DO
#Add the rest of the rigs to this "pipeline"
#Add iteration of files, so that you can keep exporting and it does not save on top of the excisting file
#The import then needs to take the newest file. [-1] can be used for that in an array
#Maybe adding so you can select multiple object to export and import  (done)
#maybe a button to select multiple objects and create folders in that location you want that has the name you need to export and import skinWeights. Look into arrays and lists. (partly done, you could make a button that does all three things)