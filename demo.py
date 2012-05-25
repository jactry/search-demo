#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from widget import floating
from tray import icontray

class jsi():
    def __init__(self):
        self.clipboard = QtGui.QApplication.clipboard()
        self.widget = floating()
        self.clipboard.selectionChanged.connect(self.show_floating)

        self.tray = icontray()
        self.tray.show()


    def show_floating(self):
        currsor = QtGui.QCursor.pos()
        self.widget.setGeometry(currsor.x()-2, currsor.y()-2, 32, 32)
        self.widget.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    jsi = jsi()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.exit(app.exec_())
