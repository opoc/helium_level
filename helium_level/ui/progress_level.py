#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
import operator
from PyQt4 import QtGui
from .progress_level_ui import Ui_ProgressLevel

class ProgressLevel(QtGui.QWidget, Ui_ProgressLevel):
    def __init__(self, config, **kwargs):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.config = config
        if (self.config.getfloat('top') > self.config.getfloat('bottom')):
            self._cmp = operator.gt
        else:
            self._cmp = operator.lt
        self.colors = {'ok': QtGui.QColor(0, 255, 0),
                       'warn': QtGui.QColor(255, 255, 0),
                       'alert': QtGui.QColor(255, 0, 0)}
        self._setLabels()

    def _setLabels(self):
        self.lE_Top.setText(self.config['top'])
        self.lE_High.setText(self.config['high'])
        self.lE_Warn.setText(self.config['warn'])
        self.lE_Low.setText(self.config['low'])
        self.lE_Bottom.setText(self.config['bottom'])

    def updateProgress(self, value):
        value = max(min(value, 100), 0)
        self.progressBar.setValue(value)
        palette = self.progressBar.palette()
        if self._cmp(self.config.getfloat('low'), value):
            palette.setColor(QtGui.QPalette.Highlight,
                             self.colors['alert'])
        elif self._cmp(self.config.getfloat('warn'), value):
            palette.setColor(QtGui.QPalette.Highlight,
                             self.colors['warn'])
        else:
            palette.setColor(QtGui.QPalette.Highlight,
                             self.colors['ok'])
        self.progressBar.setPalette(palette)
