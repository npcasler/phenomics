'''
Adapted from htp-geoprocessor plugin built by Kelly Thorp
Plugin can be found at https://plugins.qgis.org/plugins/htpgeoprocessor/


This is an attempt at parallelizing the field phenomics workflow

@author: npcasler
'''

import os
import math
import LatLongUTMconversion
from PyQt4.QtCore import *
from PyQt.QtGui import *
from Ui_PreprocessorDlg import Ui_PreprocessorDlg

class PreprocessorDlg(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui.setupUi(self)
        self.rownum = 50
        self.colnum = 9
        for i in range(self.rownum):
            for j in range(self.colnum):
                self.ui.tblInstructions.etItem(i,k,QTableWidgetItem(''))
                if j > 0:
                    self.ui.tblInstructions.item(i,j).setTextAlignment(Qt.AlignRight)
                else:
                    self.ui.tblInstructions.item(i,j, 
