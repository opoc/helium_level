#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
from PyQt4 import QtGui
from .VISA_ui import Ui_Dlg_VISA


class VISA(QtGui.QDialog, Ui_Dlg_VISA):
    def __init__(self, VISA):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.VISA = VISA

    def get_VISA(self):
        return {}
