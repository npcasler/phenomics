'''
Created on Mar 22, 2012

@author: kthorp
'''
import os
import math
import LatLongUTMconversion
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_PreprocessorDlg import Ui_PreprocessorDlg

class PreprocessorDlg(QDialog): 
    def __init__(self): 
        QDialog.__init__(self) 
        # Set up the user interface from Designer. 
        self.ui = Ui_PreprocessorDlg()
        self.ui.setupUi(self)
        self.rownum = 50
        self.colnum = 9  
        for i in range(self.rownum):
            for j in range(self.colnum):
                self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(''))
                if j > 0:
                    self.ui.tblInstructions.item(i,j).setTextAlignment(Qt.AlignRight)
                else:
                    self.ui.tblInstructions.item(i,j).setTextAlignment(Qt.AlignLeft)

    @pyqtSignature("on_btnLoad_clicked()")
    def on_btnLoad_clicked(self):
        file = QFileDialog.getOpenFileName(self,
                                           'Load Instruction File:',
                                           os.getcwd(),
                                           '*.csv')
        if file == '':
            return
        
        for i in range(self.rownum):
            for j in range(self.colnum):
                self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(''))
        os.chdir(os.path.dirname(str(file)))
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        if len(lines) > self.rownum+1:
            QMessageBox.critical(self, 'Instruction File', 'Error reading file.')
            return
        lines = [line.rstrip().split(',') for line in lines]
        
        self.ui.txtNumCol.setText(lines[0][0])
        self.ui.txtEasting.setText(lines[0][1])
        self.ui.txtNorthing.setText(lines[0][2])
        
        for i,line in enumerate(lines[1:]):
            if i > self.rownum - 1:
                break
            for j in range(self.colnum):
                if j in range(6):
                    self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(line[j]))
                elif j in [6]: #the data columns
                    datacols = line[6:-2]
                    string=''
                    for item in datacols:
                        string += item + ','
                    self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(string[:-1]))
                elif j in [7]:
                    self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(line[-2]))
                elif j in [8]:
                    self.ui.tblInstructions.setItem(i,j,QTableWidgetItem(line[-1]))
                if j > 0:
                    self.ui.tblInstructions.item(i,j).setTextAlignment(Qt.AlignRight)
                else:
                    self.ui.tblInstructions.item(i,j).setTextAlignment(Qt.AlignLeft)
                   
    @pyqtSignature("on_btnSave_clicked()")
    def on_btnSave_clicked(self):
        file = QFileDialog.getSaveFileName(self,
                                           'Save Instruction File:',
                                           os.getcwd(),
                                           '*.csv')
        if file == '':
            return
        
        os.chdir(os.path.dirname(str(file)))
        f = open(file, 'w')
        string = str(self.ui.txtNumCol.text()) + ','
        string+=str(self.ui.txtEasting.text()) + ','
        string+=str(self.ui.txtNorthing.text()) + '\n'
        f.write(string)
        for i in range(self.rownum):
            if str(self.ui.tblInstructions.item(i,0).text()) != '':
                string = ''
                for j in range(self.colnum):
                    string+=str(self.ui.tblInstructions.item(i,j).text()) + ','
                string = string[:-1] + '\n'
                f.write(string)
        f.close()

    @pyqtSignature("on_btnRun_clicked()")
    def on_btnRun_clicked(self):
        ret = self.Preprocessor()

        if ret:
            QMessageBox.information(self,
                            'HTP Geoprocessor',
                            'Finished processing file!')
                
    @pyqtSignature("on_btnExit_clicked()")
    def on_btnExit_clicked(self):
        self.close()

    def Preprocessor(self):
        #This code prepares data from sensing vehicle platforms for input into a GIS.
        #Specifically, it:
        #0.  Assumes header information on the first line
        #1.  Removes blank lines and lines not having correct number of entries (self.ui.txtNumCol).
        #2.  Converts Lat/Long to UTM coordinates at GPS receiver with coordinate offset, if needed.
        #3.  Adjusts UTM GPS coordinate to sensor locations with coordinate offset, if needed.
        #4.  Writes a new CSV sensor output file with UTM coordinates added
        
        self.ui.progressBar.setValue(0)
        
        #Open file and split data by commas
        filename = QFileDialog.getOpenFileName(self,
                                               'Open Sensor Data File',
                                               os.getcwd(),
                                               '*.csv')
        if filename == '':
            return 0
        
        os.chdir(os.path.dirname(str(filename)))
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        lines = [line.rstrip().split(',') for line in lines]
        
        filename = filename[:-4] + '-preprocess' + filename[-4:]     
        f = open(filename, 'w')
        f.write('Sensor,SensorID,Latitude,Longitude,Heading,UTMX-rec,UTMY-rec,UTMZ-rec,')
        f.write('UTMX-sen,UTMY-sen,UTMZ-sen,')
        maxdatacols = 0
        requiredcols = []
        for i in range(self.rownum):
            if str(self.ui.tblInstructions.item(i,0).text()) != '':
                datacols = self.ui.tblInstructions.item(i,6).text().split(',')
                for j in datacols:
                    requiredcols.append(int(j))
                if len(datacols) > maxdatacols:
                    maxdatacols = len(datacols)
                if self.ui.tblInstructions.item(i,1).text() != '':
                    requiredcols.append(int(self.ui.tblInstructions.item(i,1).text()))
                if self.ui.tblInstructions.item(i,2).text() != '':
                    requiredcols.append(int(self.ui.tblInstructions.item(i,2).text()))
                if self.ui.tblInstructions.item(i,3).text() != '':
                    requiredcols.append(int(self.ui.tblInstructions.item(i,3).text()))
                if self.ui.tblInstructions.item(i,4).text() != '':
                    requiredcols.append(int(self.ui.tblInstructions.item(i,4).text()))
        string = ''
        for i in range(maxdatacols):
            string+='Data'+str(i+1)+','
        requiredcols = list(set(requiredcols))
        nonreqcols = []
        for i in range(int(self.ui.txtNumCol.text())):
            if (i+1) not in requiredcols:
                nonreqcols.append(i+1)
        for i in nonreqcols:
            string += lines[0][i-1] + ','
        f.write(string[:-1] + '\n')
        
        #Remove lines with entries not equal to self.ui.txtColNum 
        lines.pop(0)
        for i, line in enumerate(lines):
            if len(line) != int(self.ui.txtNumCol.text()):
                lines.pop(i)
        numlines = len(lines)
        
        #Calculate and add UTM coordinates 
        for i, line in enumerate(lines):       
            for j in range(self.rownum):
                if str(self.ui.tblInstructions.item(j,0).text()) != '':
                     
                    #For files with a sensor id on each line, check for a matching id.
                    sid = ''
                    try:
                        idcol = int(self.ui.tblInstructions.item(j,4).text())
                    except:
                        idcol = -99
                    if idcol >= 1 and idcol <= int(self.ui.txtNumCol.text()):
                        sid = str(self.ui.tblInstructions.item(j,5).text())
                        if line[idcol-1] != sid:
                            continue
                        
                    #Calculate the UTM coordinates at the GPS receiver
                    longitude = float(line[int(self.ui.tblInstructions.item(j,2).text())-1])
                    latitude = float(line[int(self.ui.tblInstructions.item(j,1).text())-1])
                    UTMrec = LatLongUTMconversion.LLtoUTM(23, latitude, longitude)
                    UTMZrec = UTMrec[0]
                    UTMXrec = UTMrec[1]
                    UTMYrec = UTMrec[2]
                    UTMXrec+=float(self.ui.txtEasting.text()) #X-offset from GPS receiver to field map, if any
                    UTMYrec+=float(self.ui.txtNorthing.text()) #Y-offset from GPS receiver to field map, if any

                    #Calculate sensor coordinates based on sensor geometry and tractor heading
                    heading = float(line[int(self.ui.tblInstructions.item(j,3).text())-1])
                    headingrad = heading*math.pi/180.0
                    x = float(self.ui.tblInstructions.item(j,7).text())
                    y = float(self.ui.tblInstructions.item(j,8).text())
                    xp = x*math.cos(-1*headingrad)-y*math.sin(-1*headingrad)
                    yp = x*math.sin(-1*headingrad)+y*math.cos(-1*headingrad)
                    UTMXsen = UTMXrec + xp
                    UTMYsen = UTMYrec + yp
                    UTMZsen = UTMZrec
                    
                    #Fix sensor names, if necessary
                    sensorname = self.ui.tblInstructions.item(j,0).text()
                    sensorname.replace(',',';')
                    
                    string=''
                    string+=sensorname + ','        #Sensor Name
                    string+=sid + ','               #Sensor ID
                    string+=str(latitude) + ','     #Latitude
                    string+=str(longitude) + ','    #Longitude
                    string+=str(heading) + ','      #Heading
                    string+=str(UTMXrec) + ','      #UTM Easting Receiver
                    string+=str(UTMYrec) + ','      #UTM Northing Receiver
                    string+=str(UTMZrec) + ','      #UTM Latitude Code
                    string+=str(UTMXsen) + ','      #UTM Easting Sensor
                    string+=str(UTMYsen) + ','      #UTM Northing Sensor
                    string+=str(UTMZsen) + ','      #UTM Latitude Code
                    
                    #Retrieve data values
                    datacols = self.ui.tblInstructions.item(j,6).text().split(',')
                    for k in range(maxdatacols):
                        try:
                            string+=line[int(datacols[k])-1] + ','
                        except:
                            string+=','
                            
                    #Write nonrequired data
                    for k in nonreqcols:
                        string+=line[k-1]+','
                    
                    string=string[:-1] + '\n'
                    f.write(string)
            
            self.ui.progressBar.setValue(float(i+1)/float(numlines)*100.0)
        
        f.close()
        return 1