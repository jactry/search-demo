#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import *

import webbrowser

class floating(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_X11DoNotAcceptFocus, True)
        pic = QPixmap('./google.png')
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(pic))
        self.setPalette(palette)
        
    def search(self):
        text = str(QtGui.QApplication.clipboard().text("plain", QtGui.QClipboard.Selection))
        webbrowser.open('http://www.google.com/search?hl=zh-CN&q=' + text)

    def mousePressEvent(self, event):
        self.search()
        
    def leaveEvent(self, event):
        self.hide()
