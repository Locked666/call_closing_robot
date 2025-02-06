import sys
import os
import qdarktheme
from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt,QCoreApplication,QFile,Slot,SLOT,Signal,QRect,QObject, QTime,QAbstractTableModel,QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QDialog,QVBoxLayout,QWidgetAction,QMdiSubWindow,QMessageBox,QCheckBox,QHeaderView,QMenu
import time
from time import sleep
from pathlib import Path
from datetime import datetime,date, time

from ui.mainWindow import Ui_MainWindow
from ui.FrmConfiguracao import Ui_Form

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self = Ui_MainWindow()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())