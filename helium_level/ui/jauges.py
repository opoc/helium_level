#!/usr/bin/python3
# -*- coding: utf-8 -*-


from __future__ import division, print_function
from PyQt4 import QtGui, QtCore
from .jauges_ui import Ui_Dlg_Jauges
import jauges


class Jauges(QtGui.QDialog, Ui_Dlg_Jauges):
    def __init__(self, config):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.config = config
        checked = [_.strip() for _ in
                   self.config['JAUGES']['active'].split(',')]

        self.model = QtGui.QStandardItemModel(self.listView)
        self.jauges = jauges.scan_jauge()

        for (mod, obj, name, descr) in self.jauges:
            item = QtGui.QStandardItem(name + ": " + descr)
            item.setCheckable(True)
            if mod + '.' + obj in checked:
                item.setCheckState(QtCore.Qt.Checked)
            self.model.appendRow(item)
        self.listView.setModel(self.model)

    def checked_jauges(self):
        return [jauge for i, jauge in enumerate(self.jauges)
                if self.model.item(i).checkState()]
