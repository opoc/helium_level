# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/jauges.ui'
#
# Created: Sat Oct 11 17:09:05 2014
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

class Ui_Dlg_Jauges(object):
    def setupUi(self, Dlg_Jauges):
        Dlg_Jauges.setObjectName(_fromUtf8("Dlg_Jauges"))
        Dlg_Jauges.resize(310, 278)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dlg_Jauges)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listView = QtGui.QListView(Dlg_Jauges)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dlg_Jauges)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dlg_Jauges)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dlg_Jauges.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dlg_Jauges.reject)
        QtCore.QMetaObject.connectSlotsByName(Dlg_Jauges)

    def retranslateUi(self, Dlg_Jauges):
        Dlg_Jauges.setWindowTitle(_translate("Dlg_Jauges", "Jauges", None))

