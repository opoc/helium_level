# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/progress_level.ui'
#
# Created: Mon Oct 13 21:27:15 2014
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

class Ui_ProgressLevel(object):
    def setupUi(self, ProgressLevel):
        ProgressLevel.setObjectName(_fromUtf8("ProgressLevel"))
        ProgressLevel.resize(139, 447)
        self.gridLayout_2 = QtGui.QGridLayout(ProgressLevel)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lE_Low = QtGui.QLineEdit(ProgressLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_Low.sizePolicy().hasHeightForWidth())
        self.lE_Low.setSizePolicy(sizePolicy)
        self.lE_Low.setObjectName(_fromUtf8("lE_Low"))
        self.gridLayout.addWidget(self.lE_Low, 11, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        self.label_4 = QtGui.QLabel(ProgressLevel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ProgressLevel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(ProgressLevel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ProgressLevel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        self.lE_Bottom = QtGui.QLineEdit(ProgressLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_Bottom.sizePolicy().hasHeightForWidth())
        self.lE_Bottom.setSizePolicy(sizePolicy)
        self.lE_Bottom.setObjectName(_fromUtf8("lE_Bottom"))
        self.gridLayout.addWidget(self.lE_Bottom, 14, 0, 1, 1)
        self.lE_Warn = QtGui.QLineEdit(ProgressLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_Warn.sizePolicy().hasHeightForWidth())
        self.lE_Warn.setSizePolicy(sizePolicy)
        self.lE_Warn.setObjectName(_fromUtf8("lE_Warn"))
        self.gridLayout.addWidget(self.lE_Warn, 8, 0, 1, 1)
        self.lE_Top = QtGui.QLineEdit(ProgressLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_Top.sizePolicy().hasHeightForWidth())
        self.lE_Top.setSizePolicy(sizePolicy)
        self.lE_Top.setObjectName(_fromUtf8("lE_Top"))
        self.gridLayout.addWidget(self.lE_Top, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.lE_High = QtGui.QLineEdit(ProgressLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lE_High.sizePolicy().hasHeightForWidth())
        self.lE_High.setSizePolicy(sizePolicy)
        self.lE_High.setObjectName(_fromUtf8("lE_High"))
        self.gridLayout.addWidget(self.lE_High, 5, 0, 1, 1)
        self.label = QtGui.QLabel(ProgressLevel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(ProgressLevel)
        self.progressBar.setMinimumSize(QtCore.QSize(60, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 0, 1, 1, 1)

        self.retranslateUi(ProgressLevel)
        QtCore.QMetaObject.connectSlotsByName(ProgressLevel)

    def retranslateUi(self, ProgressLevel):
        ProgressLevel.setWindowTitle(_translate("ProgressLevel", "ProgressLevel", None))
        self.label_4.setText(_translate("ProgressLevel", "Low", None))
        self.label_3.setText(_translate("ProgressLevel", "Warn", None))
        self.label_5.setText(_translate("ProgressLevel", "Bottom", None))
        self.label_2.setText(_translate("ProgressLevel", "High", None))
        self.label.setText(_translate("ProgressLevel", "Top", None))

