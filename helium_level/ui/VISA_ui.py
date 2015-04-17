# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VISA.ui'
#
# Created: Fri Dec  6 18:47:09 2013
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

class Ui_Dlg_VISA(object):
    def setupUi(self, Dlg_VISA):
        Dlg_VISA.setObjectName(_fromUtf8("Dlg_VISA"))
        Dlg_VISA.resize(755, 360)
        self.gridLayout_3 = QtGui.QGridLayout(Dlg_VISA)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridGroupBox = QtGui.QGroupBox(Dlg_VISA)
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setMargin(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.gridGroupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridGroupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridGroupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridGroupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridGroupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.gridGroupBox)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.gridGroupBox)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.gridGroupBox)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 2, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridGroupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridGroupBox)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.gridGroupBox)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridGroupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gridGroupBox, 0, 0, 1, 1)
        self.gridGroupBox_2 = QtGui.QGroupBox(Dlg_VISA)
        self.gridGroupBox_2.setObjectName(_fromUtf8("gridGroupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.gridGroupBox_2)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.gridLayout_2.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridGroupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridGroupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.gridGroupBox_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.pB_Send = QtGui.QPushButton(self.gridGroupBox_2)
        self.pB_Send.setObjectName(_fromUtf8("pB_Send"))
        self.gridLayout_2.addWidget(self.pB_Send, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.gridGroupBox_2, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dlg_VISA)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(Dlg_VISA)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dlg_VISA.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dlg_VISA.reject)
        QtCore.QMetaObject.connectSlotsByName(Dlg_VISA)

    def retranslateUi(self, Dlg_VISA):
        Dlg_VISA.setWindowTitle(_translate("Dlg_VISA", "Dialog", None))
        self.gridGroupBox.setTitle(_translate("Dlg_VISA", "Device settings:", None))
        self.label_6.setText(_translate("Dlg_VISA", "Output OFF :", None))
        self.label.setText(_translate("Dlg_VISA", "VISA address :", None))
        self.label_3.setText(_translate("Dlg_VISA", "Ask voltage :", None))
        self.label_5.setText(_translate("Dlg_VISA", "Output ON :", None))
        self.label_4.setText(_translate("Dlg_VISA", "Initialisation :", None))
        self.label_2.setText(_translate("Dlg_VISA", "Set current :", None))
        self.gridGroupBox_2.setTitle(_translate("Dlg_VISA", "Check the device:", None))
        self.label_8.setText(_translate("Dlg_VISA", "Read :", None))
        self.label_7.setText(_translate("Dlg_VISA", "Write :", None))
        self.pB_Send.setText(_translate("Dlg_VISA", "Send", None))

