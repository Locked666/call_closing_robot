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
bat_file_path = os.path.join(os.path.dirname(__file__), 'start_process.bat')

config_env = dotenv_values(".env")

class BatWorker(QObject):
    output_signal = Signal(str)  # Sinal para emitir a saída em tempo real

    def __init__(self, bat_file_path):
        super().__init__()
        self.bat_file_path = bat_file_path

    def run(self):
        """Executa o arquivo .bat e emite a saída em tempo real."""
        try:
            # Inicia o processo
            process = Popen(
                [self.bat_file_path],  # Caminho do arquivo .bat
                stdout=PIPE,            # Captura a saída (stdout)
                stderr=STDOUT,          # Redireciona erros para stdout
                text=True,              # Retorna a saída como string
                shell=True,             # Executa no shell do sistema
                bufsize=1,              # Buffer de linha por linha
                universal_newlines=True # Compatibilidade com novas linhas
            )

            # Lê a saída em tempo real
            for line in process.stdout:
                self.output_signal.emit(line.strip())  # Emite a saída

            # Espera o processo terminar
            process.wait()

        except Exception as e:
            self.output_signal.emit(f"Erro ao executar o arquivo .bat: {str(e)}")


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
        self.pushButton.clicked.connect(self.start_bat_thread)
        self.bnt_log.clicked.connect(self.call_save_log)
        self.bat_thread = None
        self.worker = None
        
        # self.bat_thread = QThread()  # Renomeado para evitar conflito
        # self.worker = None
        
    def open_configuracao(self):
        self.config = Configuracao().exec()
        
    def open_texto(self):
        self.texto = CadTexto().show()
    
    def start_process(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f'Iniciando processo... {datetime.now()}') 
        """
        Executa um arquivo .bat e retorna a saída (stdout) e erros (stderr).
        """
        try:
            # Executa o arquivo .bat e captura a saída
            result = subprocess.run(
                [bat_file_path],          # Caminho do arquivo .bat
                stdout=subprocess.PIPE,    # Captura a saída (stdout)
                stderr=subprocess.PIPE,   # Captura os erros (stderr)
                text=True,                # Retorna a saída como string (não bytes)
                shell=True               # Executa no shell do sistema
            )

            # Retorna a saída e os erros
            if result.stdout:
                self.plainTextEdit.appendPlainText(result.stdout)
                
            if result.stderr:
                self.plainTextEdit.appendPlainText(result.stderr)
                

        except Exception as e:
            return None, str(e)
    
    
    
    def start_bat_thread(self):
        """Inicia a thread para executar o arquivo .bat."""
        self.plainTextEdit.appendPlainText(f'Iniciando processo... {datetime.now()}')
        
        self.bat_thread = QThread()  # Renomeado para evitar conflito
        self.worker = None
        """Inicia a thread para executar o arquivo .bat."""
        # Caminho do arquivo .bat
        # bat_file_path = "caminho/para/seu/arquivo.bat"  # Substitua pelo caminho do seu arquivo .bat

        # Limpar o QPlainTextEdit antes de executar
        # self.plainTextEdit.clear()

        # Cria o Worker e move para a thread
        self.worker = BatWorker(bat_file_path)
        self.worker.moveToThread(self.bat_thread)

        # Conecta os sinais e slots
        self.worker.output_signal.connect(self.update_output)  # Atualiza a saída
        self.bat_thread.started.connect(self.worker.run)      # Inicia o Worker
        self.bat_thread.finished.connect(self.bat_thread.deleteLater)  # Limpa a thread

        # Inicia a thread
        self.bat_thread.start()

        # Desabilita o botão durante a execução
        self.pushButton.setEnabled(False)
        self.bat_thread.finished.connect(lambda: self.pushButton.setEnabled(True))  # Reabilita ao terminar

    def update_output(self, text):
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
        """Garante que a thread seja finalizada ao fechar a janela."""
        if self.bat_thread.isRunning():
            self.bat_thread.quit()
            self.bat_thread.wait()
        event.accept()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet('dark'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())