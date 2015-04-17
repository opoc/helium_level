#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
from PyQt4 import QtGui
from .mail_ui import Ui_Dlg_Mail
from tools import email


class Mail(QtGui.QDialog, Ui_Dlg_Mail):
    def __init__(self, config):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.config = config

        self.lE_SMTP.setText(self.config['server'])
        self.lE_username.setText(self.config['username'])
        self.listDest.setPlainText(self.config['dest'])

        # Connect signals
        self.pB_Check.clicked.connect(self.check_email)
        self.lE_SMTP.editingFinished.connect(self.update_server)
        self.lE_username.editingFinished.connect(self.update_username)
        self.lE_password.editingFinished.connect(self.update_password)
        self.listDest.textChanged.connect(self.update_dest)

    def update_server(self, *args, **kwargs):
        self.config['server'] = self.lE_SMTP.text().strip()

    def update_username(self, *args, **kwargs):
        self.config['username'] = self.lE_username.text().strip()

    def update_password(self, *args, **kwargs):
        self.config['password'] = self.lE_password.text().strip()

    def update_dest(self, *args, **kwargs):
        self.config['dest'] = self.listDest.plainText().strip()

    def update_conf(self, *args, **kwargs):
        self.update_server(*args, **kwargs)
        self.update_username(*args, **kwargs)
        self.update_password(*args, **kwargs)
        self.update_dest(*args, **kwargs)

    def check_email(self, *args, **kwargs):
        self.update_conf()
        try:
            email.send_mail(self.config, 'test')
            # dialog for "An Email has been sent."
        except:
            # dialog for error
            pass
