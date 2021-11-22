import sys 
import maya.cmds as cmds

libScriptPath = ("C:\\Truemax Academy\\Class 2019 - Files\\sem04\\nightingale\\05_tools\\skinWeight_export_and_import")
for spath in [libScriptPath]:
    if not spath in sys.path:
        sys.path.append(spath)
                
#import(autoRig)
import autoSkinWeight

#reload(autoRig)
reload(autoSkinWeight)

#using functions
autoSkinWeight.ImportAndExportSkinWeights()