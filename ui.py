# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN.ui'
#
# Created: Wed Dec 30 13:41:55 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Currencies(object):
    def setupUi(self, Currencies):
        Currencies.setObjectName(_fromUtf8("Currencies"))
        Currencies.resize(845, 453)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Currencies.sizePolicy().hasHeightForWidth())
        Currencies.setSizePolicy(sizePolicy)
        Currencies.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(Currencies)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.verticalLayout.addWidget(self.mplwidget)
        Currencies.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Currencies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        Currencies.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Currencies)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Currencies.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Currencies)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Currencies.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Options_DW_2 = QtGui.QDockWidget(Currencies)
        self.Options_DW_2.setObjectName(_fromUtf8("Options_DW_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.formLayout = QtGui.QFormLayout(self.dockWidgetContents_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.CSel_CB = QtGui.QComboBox(self.dockWidgetContents_2)
        self.CSel_CB.setObjectName(_fromUtf8("CSel_CB"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.CSel_CB)
        self.Options_DW_2.setWidget(self.dockWidgetContents_2)
        Currencies.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.Options_DW_2)
        self.actionShow_Options = QtGui.QAction(Currencies)
        self.actionShow_Options.setObjectName(_fromUtf8("actionShow_Options"))
        self.menuView.addAction(self.actionShow_Options)
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(Currencies)
        QtCore.QMetaObject.connectSlotsByName(Currencies)

    def retranslateUi(self, Currencies):
        Currencies.setWindowTitle(_translate("Currencies", "Currencies", None))
        self.menuView.setTitle(_translate("Currencies", "View", None))
        self.toolBar.setWindowTitle(_translate("Currencies", "toolBar", None))
        self.Options_DW_2.setWindowTitle(_translate("Currencies", "Options", None))
        self.actionShow_Options.setText(_translate("Currencies", "Show Options", None))

from matplotlibwidget import MatplotlibWidget
