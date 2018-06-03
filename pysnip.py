import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument



      <Script>import clr

import sys
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
import os   
# importing os without appending to path raises Import Error


clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN


clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from Autodesk.Revit.ApplicationServices import *
from Autodesk.Revit.DB import *
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


fp = BasicFileInfo.Extract(doc.PathName).CentralPath

d = os.path.splitext(fp)[0] + dataEnteringNode[0]

#Assign your output to the OUT variable.
OUT = d</Script>
    </PythonNodeModels.PythonNode>
    <PythonNodeModels.PythonNode guid="1c89481a-c2f2-4be5-b3e2-cc767d7ff0bd" type="PythonNodeModels.PythonNode" nickname="Python Script" x="305.267736242801" y="-804.379955185008" isVisible="true" isUpstreamVisible="true" lacing="Disabled" isSelectedInput="False" IsFrozen="false" isPinned="false" inputcount="1">
      <PortInfo index="0" default="False" />
      <Script>import clr
import System

#dataEnteringNode = IN

mods = None
for a in System.AppDomain.CurrentDomain.GetAssemblies():
	if 'IronPython.Modules' == a.GetName().Name:
		mods = a 
		break
if mods is not None:
	OUT = [m.Key for m in mods.IronPython.Modules]





</Script>