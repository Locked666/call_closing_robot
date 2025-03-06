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
from ui.CadTexto import Ui_CadTexto

class CadTexto(QDialog,Ui_CadTexto):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Cadastro de Texto")



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.actionConfigura_es.triggered.connect(self.open_configuracao)
        self.actionRespostas.triggered.connect(lambda: CadTexto().exec())
        
    def open_configuracao(self):
        self.configuracao = QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.configuracao)
        self.configuracao.show()
    
    def open_texto(self):
        self.texto = CadTexto().show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())