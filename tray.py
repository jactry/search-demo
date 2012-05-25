#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys

class icontray(QtGui.QSystemTrayIcon):
    def __init__(self,parent = None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.icon = QtGui.QIcon("./google.png")
        self.setIcon(self.icon)
        self.quit_action = QtGui.QAction(u'退出', self, triggered = sys.exit)
        self.menu = QtGui.QMenu()
        self.menu.addAction(self.quit_action)
        self.setContextMenu(self.menu)
