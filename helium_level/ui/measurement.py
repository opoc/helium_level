#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import division, print_function
from PyQt4 import QtGui
from .measurement_ui import Ui_Dlg_Measurement


class Measurement(QtGui.QDialog, Ui_Dlg_Measurement):
    def __init__(self, measurement={}):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.set_measurement(measurement)
        self.columns = ['HeatCurr', 'HeatTime', 'MeasCurr', 'StabTime',
                        'WaitTime']

    def set_measurement(self, measurement):
        for col, value in measurement['monitor'].items():
            getattr(self, 'lE_M_' + col).setText(str(value))
        for col, value in measurement['transfer'].items():
            getattr(self, 'lE_T_' + col).setText(str(value))

    def get_measurement(self):
        return {
            'monitor': {name: float(getattr(self, 'lE_M_' + name).text())
                        for name in self.columns},
            'transfer': {name: float(getattr(self, 'lE_T_' + name).text())
                         for name in self.columns}}
