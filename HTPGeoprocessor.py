"""
/***************************************************************************
Name                 : HTP Geoprocessor
Description          : Tools for processing HTP geospatial data
Date                 : 29/Mar/12
copyright            : (C) 2012 by Dr. Kelly Thorp, USDA-ARS
email                : kelly.thorp@ars.usda.gov 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
import os
import sys
# Import the code for the dialogs
from MapCreatorDlg import MapCreatorDlg
from GeoprocessorDlg import GeoprocessorDlg
from PreprocessorDlg import PreprocessorDlg

class HTPGeoprocessor: 

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'htpgeoprocessor_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):  
        # Create action that will start plugin configuration
        icon = QIcon(":/plugins/htpgeoprocessor/icon.png")
        self.createmap = QAction(icon,u"Map Creator", self.iface.mainWindow())
        self.preprocess = QAction(icon,u"Preprocessor", self.iface.mainWindow())
        self.geoprocess = QAction(icon,u"Geoprocessor", self.iface.mainWindow())
        self.helpme = QAction(icon, u"Help", self.iface.mainWindow())
        
        # connect the action to a method
        self.createmap.triggered.connect(self.CreateMap)
        self.preprocess.triggered.connect(self.Preprocess)
        self.geoprocess.triggered.connect(self.Geoprocess)
        self.helpme.triggered.connect(self.Help)
         
        # Add toolbar button and menu item
        self.iface.addPluginToMenu(u"&HTP Geoprocessor", self.createmap)
        self.iface.addPluginToMenu(u"&HTP Geoprocessor", self.preprocess)
        self.iface.addPluginToMenu(u"&HTP Geoprocessor", self.geoprocess)
        self.iface.addPluginToMenu(u"&HTP Geoprocessor", self.helpme)
                
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&HTP Geoprocessor", self.createmap)
        self.iface.removePluginMenu(u"&HTP Geoprocessor", self.preprocess)
        self.iface.removePluginMenu(u"&HTP Geoprocessor", self.geoprocess)
        self.iface.removePluginMenu(u"&HTP Geoprocessor", self.helpme)
        
    # run methods that perform all the real work
    def CreateMap(self):
        dlg = MapCreatorDlg(self.iface)
        dlg.exec_()
    
    def Preprocess(self):
        dlg = PreprocessorDlg()
        dlg.exec_()
          
    def Geoprocess(self): 
        # create and show the dialog 
        dlg = GeoprocessorDlg(self.iface) 
        # show the dialog
        #dlg.show() #Modeless dialog
        dlg.exec_() #Modal dialog
        
    def Help(self):
        path = os.path.dirname(sys.modules[__name__].__file__)
        if sys.platform == 'linux':
            os.system(path+"//HTP Geoprocessor README.pdf")
        elif sys.platform == 'win32':
            os.startfile(path+"\\HTP Geoprocessor README.pdf")
        else:
            QMessageBox.critical(self.iface.mainWindow(),'Help','Error opening document. Look in plug-in install directory for PDF.')
