#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import ui
import CNBChart as Chart
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib
matplotlib.use('Qt4Agg') # overrule configuration
matplotlib.rc('font', family='Arial')
from PyQt4 import QtGui
from PyQt4 import QtCore

class CChart(QtGui.QMainWindow, ui.Ui_Currencies):
    def __init__(self, Currency):
        super(CChart, self).__init__()
        self.setupUi(self)        
        
        
        self.cm = Chart.ChartMaker()
        self.mplwidget.figure = self.cm.get_fig()
        self.cm.draw(Currency)
        self.toolBar.addWidget(NavigationToolbar(self.mplwidget, self))
        [self.CSel_CB.addItem(e) for e in self.cm.get_currencies()]
        self.connect(self.CSel_CB, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.Curr_changed)
        self.activateWindow()
        self.show()
        
    def Curr_changed(self, t):
        self.cm.draw(t)
        self.cm.fig.canvas.draw()

def main():
    app = QtGui.QApplication(sys.argv)
    CC = CChart("RUB")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
