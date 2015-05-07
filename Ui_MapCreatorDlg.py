# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MapCreatorDlg.ui'
#
# Created: Thu Feb 27 11:08:49 2014
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MapCreatorDlg(object):
    def setupUi(self, MapCreatorDlg):
        MapCreatorDlg.setObjectName(_fromUtf8("MapCreatorDlg"))
        MapCreatorDlg.resize(401, 181)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapCreatorDlg.sizePolicy().hasHeightForWidth())
        MapCreatorDlg.setSizePolicy(sizePolicy)
        MapCreatorDlg.setMinimumSize(QtCore.QSize(401, 181))
        MapCreatorDlg.setMaximumSize(QtCore.QSize(401, 181))
        self.verticalLayoutWidget = QtGui.QWidget(MapCreatorDlg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Label1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.Label1.setMinimumSize(QtCore.QSize(379, 0))
        self.Label1.setObjectName(_fromUtf8("Label1"))
        self.verticalLayout.addWidget(self.Label1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tbxInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.tbxInput.setObjectName(_fromUtf8("tbxInput"))
        self.horizontalLayout_5.addWidget(self.tbxInput)
        self.btnBrowse1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnBrowse1.setObjectName(_fromUtf8("btnBrowse1"))
        self.horizontalLayout_5.addWidget(self.btnBrowse1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(MapCreatorDlg)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ProgressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_2)
        self.ProgressBar.setObjectName(_fromUtf8("ProgressBar"))
        self.horizontalLayout_3.addWidget(self.ProgressBar)
        self.btnRun = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout_3.addWidget(self.btnRun)
        self.btnExit = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout_3.addWidget(self.btnExit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(MapCreatorDlg)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 381, 51))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Label3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.Label3.setObjectName(_fromUtf8("Label3"))
        self.verticalLayout_3.addWidget(self.Label3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tbxOutput = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.tbxOutput.setObjectName(_fromUtf8("tbxOutput"))
        self.horizontalLayout_2.addWidget(self.tbxOutput)
        self.btnBrowse2 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.btnBrowse2.setObjectName(_fromUtf8("btnBrowse2"))
        self.horizontalLayout_2.addWidget(self.btnBrowse2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MapCreatorDlg)
        QtCore.QMetaObject.connectSlotsByName(MapCreatorDlg)

    def retranslateUi(self, MapCreatorDlg):
        MapCreatorDlg.setWindowTitle(QtGui.QApplication.translate("MapCreatorDlg", "Map Creator", None, QtGui.QApplication.UnicodeUTF8))
        self.Label1.setText(QtGui.QApplication.translate("MapCreatorDlg", "Select input coordinate file:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbxInput.setToolTip(QtGui.QApplication.translate("MapCreatorDlg", "Give the filepath and filename of the output shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse1.setToolTip(QtGui.QApplication.translate("MapCreatorDlg", "Gives dialog box for selecting output filepath and filename.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse1.setText(QtGui.QApplication.translate("MapCreatorDlg", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("MapCreatorDlg", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("MapCreatorDlg", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.Label3.setText(QtGui.QApplication.translate("MapCreatorDlg", "Specify output shapefile:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbxOutput.setToolTip(QtGui.QApplication.translate("MapCreatorDlg", "Give the filepath and filename of the output shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse2.setToolTip(QtGui.QApplication.translate("MapCreatorDlg", "Gives dialog box for selecting output filepath and filename.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse2.setText(QtGui.QApplication.translate("MapCreatorDlg", "Browse", None, QtGui.QApplication.UnicodeUTF8))

