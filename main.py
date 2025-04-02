import sys
import os
import subprocess
import qdarktheme
from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt,QCoreApplication,QFile,Slot,SLOT,Signal,QRect,QObject, QTime,QAbstractTableModel,QDateTime,QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog,QLineEdit, QWidget,QVBoxLayout,QWidgetAction,QMdiSubWindow,QMessageBox,QCheckBox,QHeaderView,QMenu
import time
from time import sleep
from datetime import datetime
from pathlib import Path
from datetime import datetime,date, time
from config import *
from subprocess import Popen, PIPE, STDOUT

from ui.mainWindow import Ui_MainWindow
from ui.FrmConfiguracao import Ui_Form
from ui.CadTexto import Ui_CadTexto
from dotenv import dotenv_values
from PySide6.QtCore import QObject, Signal
from execute_web import work

bat_file_path = os.path.join(os.path.dirname(__file__), 'start_process.bat')

config_env = dotenv_values(".env")

class CadTexto(QDialog,Ui_CadTexto):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Cadastro de Texto")

class Configuracao(QDialog,Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Configurações")
        self.load_config()
        
        self.check_ver_senha.stateChanged.connect(self.ver_senha)
        self.bnt_salvar.clicked.connect(self.salvar)
        
        
    def ver_senha(self):
        if self.check_ver_senha.isChecked():
            self.text_senha.setEchoMode(QLineEdit.Normal)
        else:
            self.text_senha.setEchoMode(QLineEdit.Password)

    
    
    def salvar(self):
        try:
            config_env['MY_SECRET_USERNAME'] = self.text_usuario.text().strip()
            config_env['MY_SECRET_PASSWORD'] = self.text_senha.text().strip()
            config_env['URL_INIT'] = f"'{self.text_url.text().strip()}'"
            with open('.env', 'w') as f:
                for key in config_env:
                    f.write(f"{key}={config_env[key]}\n")
            self.load_config()        
            msgBox = QMessageBox()
            msgBox.setText("Configurações salvas com sucesso!")
            msgBox.exec() 
            self.frm_central.setDisabled(True) 
            self.bnt_alterar.setDisabled(False)
            self.bnt_salvar.setDisabled(True)
            
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")
            msgBox = QMessageBox()
            msgBox.setText("Erro ao salvar configurações!\n{e}")
            msgBox.exec()
    
    def load_config(self):
        self.text_usuario.setText(config_env['MY_SECRET_USERNAME'])
        self.text_senha.setText(config_env['MY_SECRET_PASSWORD'])
        url = config_env['URL_INIT']
        url = url.replace("'","")
        self.text_url.setText(url)
        

        pass                     
        


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Call Booting")
        
        self.actionConfigura_es.triggered.connect(self.open_configuracao)
        self.actionRespostas.triggered.connect(lambda: CadTexto().exec())
        self.pushButton.clicked.connect(self.start_process)
        self.bnt_log.clicked.connect(self.call_save_log)
        self.bnt_clear_log.connect(lambda: self.plainTextEdit.clear())
        # self.bat_thread = None
        work.log_signal.connect(self.update_oupdate_logtput)
        # self.worker = None
        
        
        # self.bat_thread = QThread()  # Renomeado para evitar conflito
        # self.worker = None
        
    def open_configuracao(self):
        self.config = Configuracao().exec()
        
    def open_texto(self):
        self.texto = CadTexto().show()
    
    def start_process(self):
        """Inicia o processo diretamente (pode travar a UI)"""
        from execute_web import main
        main() 
        
    def update_oupdate_logtput(self, text):
        """Atualiza o QPlainTextEdit com a saída em tempo real."""
        if text == 'Todos os Tickets Foram Processados':
            self.plainTextEdit.appendPlainText(f'{text} {datetime.now()}')
            self.bat_thread.quit()
            self.bat_thread.wait()
        else :     
            self.plainTextEdit.appendPlainText(text)

    def call_save_log(self):
        log_file = Path("log.txt")
        if not log_file.exists():
            log_file.touch()
        try:
            with open("log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(self.plainTextEdit.toPlainText() + "\n")
            QMessageBox.information(self, "Log Salvo", "O log foi salvo com sucesso em log.txt.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar o log: {str(e)}")

    def closeEvent(self, event):

        event.accept()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet('dark'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())