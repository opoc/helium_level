#!/usr/bin/python


from __future__ import division, print_function


PYQTGRAPH = True

import importlib
import sys
import traceback
import time
if PYQTGRAPH:
    from pyqtgraph import QtCore, QtGui
    import pyqtgraph as pg
    from tools.dateaxis import DateAxis
else:
    from PyQt4 import QtCore, QtGui
    from matplotlib.figure import Figure
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvasQTAgg as FigureCanvas,
        NavigationToolbar2QTAgg as NavigationToolbar)
from ui.main_ui import Ui_MainWindow
from ui.mail import Mail
from ui.measurement import Measurement
from ui.VISA import VISA
from ui.jauges import Jauges
from ui.progress_level import ProgressLevel
from tools import config


DEBUG = False


_ = lambda x: x


class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.measure)

        # Connect signals
        self.pBtn_TakePoint.clicked.connect(self.takepoint)
        self.pBtn_Transfer.clicked.connect(self.transfer)

        self.actionQuit.triggered.connect(self.quit)
        self.actionVISA_device.triggered.connect(self.dlg_VISA)
        self.actionEmail_alert.triggered.connect(self.dlg_Email)
        self.actionMeasurement.triggered.connect(self.dlg_Measurement)
        self.actionJauges.triggered.connect(self.dlg_Jauges)
        self.cB_Fast.stateChanged.connect(self.change_timer_time)

        # Helium-Level array
        self.levels = {"time": []}

        self.measurement = {
            'monitor': {
                'HeatCurr': 0.1,
                'HeatTime': 1,
                'MeasCurr': 0.055,
                'StabTime': 1.,
                'WaitTime': 30},
            'transfer': {
                'HeatCurr': 0.1,
                'HeatTime': 1.,
                'MeasCurr': 0.050,
                'StabTime': 1.,
                'WaitTime': 1.}
            }

        self.config = config.load('helium.conf')
        self.jauge_names = []
        _jauge_names = [_.strip() for _ in
                        self.config['JAUGES']['active'].split(',')]
        self.tabs = {}
        for i, jauge_name in enumerate(_jauge_names):
            cls_name = jauge_name.split('.')[1]
            if self.config.has_section(cls_name.upper()):
                self.tabs[jauge_name] = \
                    ProgressLevel(self.config[cls_name.upper()])
                self.tabWidget.addTab(self.tabs[jauge_name], cls_name)
                self.jauge_names.append(jauge_name)
                self.levels[jauge_name] = []
        self.load_jauges()

        self.transfer = False

        vbox = QtGui.QVBoxLayout()
        if PYQTGRAPH:
            xaxis = DateAxis(orientation='bottom')
            self.pw = pg.PlotWidget(name=_("Levels"),
                                    axisItems={'bottom': xaxis})
            self.pw.addLegend()
            colors = ('r', 'b', 'v', 'w')
            self.plots = {
                jauge_name: self.pw.plot(pen=c, name=jauge_name,
                                         symbolBrush=c, symbolPen='w')
                for (jauge_name, c) in zip(self.jauge_names, colors)}
            vbox.addWidget(self.pw)
            self.pw.setLabel('left', _('Level'))
            self.pw.setLabel('bottom', _('Time'), units='s')

        else:
            # Matplotlib Figure
            self.fig = Figure((5.0, 4.0), dpi=100)
            self.canvas = FigureCanvas(self.fig)
            self.canvas.setParent(self.frm_mpl)
            self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.canvas.setFocus()
            self.canvas.mpl_connect('key_press_event', self.on_key_press)

            self.mpl_toolbar = NavigationToolbar(self.canvas, self.frm_mpl)

            vbox.addWidget(self.canvas)
            vbox.addWidget(self.mpl_toolbar)

            self.axes = self.fig.add_subplot(111)
            self.plots = {
                jauge_name:
                self.axes.plot_date([], [], '-o', label=jauge_name)[0] for
                jauge_name in self.jauge_names}
            # End Figure configuration
        self.frm_mpl.setLayout(vbox)

        self.cB_Fast.setCheckState(False)
        self.change_timer_time()

        self.VISA = {}

    def dlg_VISA(self, *args, **kwargs):
        dlg_visa = VISA(self.VISA)
        ret_value = dlg_visa.exec_()
        if ret_value == 1:  # Accept
            self.VISA = dlg_visa.getVISA()

    def dlg_Email(self, *args, **kwargs):
        dlg_email = Mail(self.config['EMAIL'])
        ret_value = dlg_email.exec_()
        if ret_value == 1:  # Accept
            if DEBUG:
                print("DlgEmail accepted.")
                print("New config: ", dlg_email.config)
            self.config['EMAIL'] = dlg_email.config

    def dlg_Measurement(self, *args, **kwargs):
        dlg_measurement = Measurement(self.measurement)
        ret_value = dlg_measurement.exec_()
        if ret_value == 1:  # Accept
            self.measurement = dlg_measurement.get_measurement()
            if self.transfer:
                every = self.measurement['transfer']['WaitTime']
            else:
                every = self.measurement['monitor']['WaitTime']
            print(every)

    def dlg_Jauges(self, *args, **kwargs):
        dlg = Jauges(self.config)
        ret_value = dlg.exec_()
        if ret_value == 1:  # Accept
            if not self.config.has_section('JAUGES'):
                self.config.add_section('JAUGES')
            actives = ', '.join([mod + '.' + obj for mod, obj, name, descr in
                                 dlg.checked_jauges()])
            self.config['JAUGES']['active'] = actives

    def change_timer_time(self, *args, **kwargs):
        if self.cB_Fast.checkState():
            self.cB_Fast.setText(_('Fast'))
            period = self.config.getfloat('RATE', 'fast')
        else:
            self.cB_Fast.setText(_('Slow'))
            period = self.config.getfloat('RATE', 'slow')
        self.lbl_speed_value.setText(_('every {} min').format(period))
        self.measure()
        self.timer.start(period * 60 * 1000)

    def takepoint(self, *args, **kwargs):
        return self.measure()

    def transfer(self, state, *args, **kwargs):
        if state:
            return self.start_transfer()
        return self.stop_transfer()

    def measure(self, *args, **kwargs):
        self.levels['time'].append(time.time())
        for jauge_name, cls in self.jauges.items():
            try:
                cls.prep()
                measure = cls.measure()
                cls.post()
                self.levels[jauge_name].append(measure)
                self.tabs[jauge_name].updateProgress(measure)
            except:
                print("Error with jauge '{}'".format(jauge_name))
                traceback.print_exc()
        print(self.levels)
        self.refresh_figure()
        self.update_lbl_lastResult()
        # TODO check for every jauges

    def update_lbl_lastResult(self):
        msg = ' # '.join(["{} = {:.2f}".format(
            name.split('.')[1], lvl[-1]) for name, lvl in
            self.levels.items() if name != 'time'])
        self.lbl_lastResult.setText(time.ctime(self.levels['time'][-1]) + " " +
                                    msg)

    def refresh_figure(self):
        if PYQTGRAPH:
            for j_name in self.jauge_names:
                self.plots[j_name].setData(
                    x=self.levels['time'],
                    y=self.levels[j_name])
        else:
            for j_name in self.jauge_names:
                self.plots[j_name].set_data(
                    self.levels['time'],
                    self.levels[j_name])
            self.axes.relim()
            self.axes.autoscale_view(True)
            self.fig.autofmt_xdate()
            formatter = self.axes.xaxis.get_major_formatter()
            formatter.scaled[1 / (24. * 60.)] = '%H:%M:%S'
            self.axes.xaxis.set_major_formatter(formatter)
            self.canvas.draw()

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def start_transfer(self, auto=False):
        print("Start Transfer")
        if auto:
            print("Auto Start Transfer")
            # Auto tranfer, change button state
            self.pBtn_Transfer.setChecked(True)
        ## Switch on the compressor
        ## TODO

    def stop_transfer(self, auto=False):
        print("Stop Transfer")
        ## Switch off the compressor
        ## TODO
        if auto:
            # Auto Stop
            print("Auto Stop Transfer")
            self.pBtn_Transfer.setChecked(False)

    def load_jauges(self):
        self.jauges = {}
        for jauge_name in self.jauge_names:
            mod, cls = jauge_name.split('.')
            _mod = importlib.__import__('jauges.' + mod,
                                        fromlist=(jauge_name,))
            self.jauges[jauge_name] = getattr(_mod, cls)(
                self.config[cls.upper()])

    def quit(self, *args, **kwargs):
        config.save(self.config, 'helium.conf')
        QtGui.QApplication.quit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
