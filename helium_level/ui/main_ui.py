# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Mon Oct 13 21:40:12 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(711, 617)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lbl_lastResult = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lastResult.setFont(font)
        self.lbl_lastResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lastResult.setObjectName(_fromUtf8("lbl_lastResult"))
        self.verticalLayout_4.addWidget(self.lbl_lastResult)
        self.frm_mpl = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_mpl.sizePolicy().hasHeightForWidth())
        self.frm_mpl.setSizePolicy(sizePolicy)
        self.frm_mpl.setMinimumSize(QtCore.QSize(400, 400))
        self.frm_mpl.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_mpl.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_mpl.setObjectName(_fromUtf8("frm_mpl"))
        self.verticalLayout_4.addWidget(self.frm_mpl)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.groupBox_transfer = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_transfer.sizePolicy().hasHeightForWidth())
        self.groupBox_transfer.setSizePolicy(sizePolicy)
        self.groupBox_transfer.setFlat(False)
        self.groupBox_transfer.setCheckable(False)
        self.groupBox_transfer.setObjectName(_fromUtf8("groupBox_transfer"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_transfer)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pBtn_Transfer = QtGui.QPushButton(self.groupBox_transfer)
        self.pBtn_Transfer.setCheckable(True)
        self.pBtn_Transfer.setChecked(False)
        self.pBtn_Transfer.setObjectName(_fromUtf8("pBtn_Transfer"))
        self.horizontalLayout_3.addWidget(self.pBtn_Transfer)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cBox_ForceTransfer = QtGui.QCheckBox(self.groupBox_transfer)
        self.cBox_ForceTransfer.setChecked(False)
        self.cBox_ForceTransfer.setObjectName(_fromUtf8("cBox_ForceTransfer"))
        self.verticalLayout_3.addWidget(self.cBox_ForceTransfer)
        self.cB_Auto = QtGui.QCheckBox(self.groupBox_transfer)
        self.cB_Auto.setObjectName(_fromUtf8("cB_Auto"))
        self.verticalLayout_3.addWidget(self.cB_Auto)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addWidget(self.groupBox_transfer)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.groupBox_Measurement = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Measurement.sizePolicy().hasHeightForWidth())
        self.groupBox_Measurement.setSizePolicy(sizePolicy)
        self.groupBox_Measurement.setObjectName(_fromUtf8("groupBox_Measurement"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_Measurement)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pBtn_TakePoint = QtGui.QPushButton(self.groupBox_Measurement)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pBtn_TakePoint.setFont(font)
        self.pBtn_TakePoint.setObjectName(_fromUtf8("pBtn_TakePoint"))
        self.horizontalLayout_2.addWidget(self.pBtn_TakePoint)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cB_Fast = QtGui.QCheckBox(self.groupBox_Measurement)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cB_Fast.setFont(font)
        self.cB_Fast.setObjectName(_fromUtf8("cB_Fast"))
        self.verticalLayout.addWidget(self.cB_Fast)
        self.lbl_speed_value = QtGui.QLabel(self.groupBox_Measurement)
        self.lbl_speed_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_speed_value.setObjectName(_fromUtf8("lbl_speed_value"))
        self.verticalLayout.addWidget(self.lbl_speed_value)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.groupBox_Measurement)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuApp = QtGui.QMenu(self.menubar)
        self.menuApp.setObjectName(_fromUtf8("menuApp"))
        self.menuConfigure = QtGui.QMenu(self.menubar)
        self.menuConfigure.setObjectName(_fromUtf8("menuConfigure"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuHelp.sizePolicy().hasHeightForWidth())
        self.menuHelp.setSizePolicy(sizePolicy)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVISA_device = QtGui.QAction(MainWindow)
        self.actionVISA_device.setObjectName(_fromUtf8("actionVISA_device"))
        self.actionEmail_alert = QtGui.QAction(MainWindow)
        self.actionEmail_alert.setCheckable(True)
        self.actionEmail_alert.setObjectName(_fromUtf8("actionEmail_alert"))
        self.actionMeasurement = QtGui.QAction(MainWindow)
        self.actionMeasurement.setObjectName(_fromUtf8("actionMeasurement"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionA_propos = QtGui.QAction(MainWindow)
        self.actionA_propos.setObjectName(_fromUtf8("actionA_propos"))
        self.actionFAQ = QtGui.QAction(MainWindow)
        self.actionFAQ.setObjectName(_fromUtf8("actionFAQ"))
        self.actionSave_configuration = QtGui.QAction(MainWindow)
        self.actionSave_configuration.setObjectName(_fromUtf8("actionSave_configuration"))
        self.actionJauges = QtGui.QAction(MainWindow)
        self.actionJauges.setObjectName(_fromUtf8("actionJauges"))
        self.menuApp.addAction(self.actionSave_configuration)
        self.menuApp.addAction(self.actionQuit)
        self.menuConfigure.addAction(self.actionVISA_device)
        self.menuConfigure.addAction(self.actionEmail_alert)
        self.menuConfigure.addAction(self.actionMeasurement)
        self.menuConfigure.addAction(self.actionJauges)
        self.menuHelp.addAction(self.actionA_propos)
        self.menuHelp.addAction(self.actionFAQ)
        self.menubar.addAction(self.menuApp.menuAction())
        self.menubar.addAction(self.menuConfigure.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pBtn_Transfer, self.cBox_ForceTransfer)
        MainWindow.setTabOrder(self.cBox_ForceTransfer, self.cB_Auto)
        MainWindow.setTabOrder(self.cB_Auto, self.pBtn_TakePoint)
        MainWindow.setTabOrder(self.pBtn_TakePoint, self.cB_Fast)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "He Level", None))
        self.lbl_lastResult.setText(_translate("MainWindow", "Helium Level Meter", None))
        self.groupBox_transfer.setTitle(_translate("MainWindow", "Transfer :", None))
        self.pBtn_Transfer.setText(_translate("MainWindow", "Transfer", None))
        self.cBox_ForceTransfer.setText(_translate("MainWindow", "Force", None))
        self.cB_Auto.setText(_translate("MainWindow", "Automatic", None))
        self.groupBox_Measurement.setTitle(_translate("MainWindow", "Measurement :", None))
        self.pBtn_TakePoint.setText(_translate("MainWindow", "Take point !", None))
        self.cB_Fast.setText(_translate("MainWindow", "Slow", None))
        self.lbl_speed_value.setText(_translate("MainWindow", "TextLabel", None))
        self.menuApp.setTitle(_translate("MainWindow", "Application", None))
        self.menuConfigure.setTitle(_translate("MainWindow", "Configure", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionVISA_device.setText(_translate("MainWindow", "VISA device...", None))
        self.actionVISA_device.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionEmail_alert.setText(_translate("MainWindow", "Email alert...", None))
        self.actionEmail_alert.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.actionMeasurement.setText(_translate("MainWindow", "Measurement...", None))
        self.actionMeasurement.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionA_propos.setText(_translate("MainWindow", "A propos...", None))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ", None))
        self.actionFAQ.setShortcut(_translate("MainWindow", "Ctrl+H, F1", None))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration", None))
        self.actionSave_configuration.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionJauges.setText(_translate("MainWindow", "Jauges...", None))
        self.actionJauges.setShortcut(_translate("MainWindow", "Ctrl+J", None))

