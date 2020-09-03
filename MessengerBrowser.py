#!/usr/bin/env python

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
import sys

def window():
    app = QApplication(sys.argv)
    view = QWebEngineView()
    # cookies = view.QWebEngineCookieStore()
    view.setWindowIcon(QtGui.QIcon('/usr/local/bin/messenger.png'))
    view.setGeometry(350, 250, 1252, 761)
    view.setWindowTitle("logo.png")
    view.show()
    view.setUrl(QUrl("""http://messenger.com"""))
    app.exec()

window()
