# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mail.ui'
#
# Created: Fri Oct 10 08:52:45 2014
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

class Ui_Dlg_Mail(object):
    def setupUi(self, Dlg_Mail):
        Dlg_Mail.setObjectName(_fromUtf8("Dlg_Mail"))
        Dlg_Mail.resize(398, 365)
        Dlg_Mail.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dlg_Mail)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dlg_Mail)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lE_SMTP = QtGui.QLineEdit(Dlg_Mail)
        self.lE_SMTP.setObjectName(_fromUtf8("lE_SMTP"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lE_SMTP)
        self.label_2 = QtGui.QLabel(Dlg_Mail)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lE_username = QtGui.QLineEdit(Dlg_Mail)
        self.lE_username.setText(_fromUtf8(""))
        self.lE_username.setObjectName(_fromUtf8("lE_username"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lE_username)
        self.label_3 = QtGui.QLabel(Dlg_Mail)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lE_password = QtGui.QLineEdit(Dlg_Mail)
        self.lE_password.setText(_fromUtf8(""))
        self.lE_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lE_password.setObjectName(_fromUtf8("lE_password"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lE_password)
        self.label_4 = QtGui.QLabel(Dlg_Mail)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.listDest = QtGui.QPlainTextEdit(Dlg_Mail)
        self.listDest.setPlainText(_fromUtf8(""))
        self.listDest.setObjectName(_fromUtf8("listDest"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.listDest)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pB_Check = QtGui.QPushButton(Dlg_Mail)
        self.pB_Check.setObjectName(_fromUtf8("pB_Check"))
        self.horizontalLayout.addWidget(self.pB_Check)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(Dlg_Mail)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Dlg_Mail)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dlg_Mail.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dlg_Mail.reject)
        QtCore.QMetaObject.connectSlotsByName(Dlg_Mail)

    def retranslateUi(self, Dlg_Mail):
        Dlg_Mail.setWindowTitle(_translate("Dlg_Mail", "Configure mail alert", None))
        self.label.setText(_translate("Dlg_Mail", "SMTP server :", None))
        self.label_2.setText(_translate("Dlg_Mail", "Username :", None))
        self.label_3.setText(_translate("Dlg_Mail", "Password :", None))
        self.label_4.setText(_translate("Dlg_Mail", "Recipients :", None))
        self.pB_Check.setText(_translate("Dlg_Mail", "Send test mail", None))

