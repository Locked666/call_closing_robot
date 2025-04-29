# from config import *
# from subprocess import Popen, PIPE, STDOUT
# from PySide6.QtGui import QKeyEvent
# import subprocess
# import time
# from time import sleep
# from PySide6 import QtCore
# from execute_web import work

import os
import sys
import qdarktheme

from PySide6.QtCore import Signal,QThread,QCoreApplication,Slot#,SLOT,Qt,QFile,QRect,QObject, QTime,QAbstractTableModel,QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog,QLineEdit, QMessageBox#,QWidget,QVBoxLayout,QWidgetAction,QMdiSubWindow,QCheckBox,QHeaderView,QMenu
from datetime import datetime
from pathlib import Path
from datetime import datetime#,date, time


from ui.mainWindow import Ui_MainWindow
from ui.FrmConfiguracao import Ui_Form
from ui.CadTexto import Ui_CadTexto
from ui.FrmLogExecusao import Ui_frm_log_execusao

from dotenv import dotenv_values



config_env = dotenv_values(".env")

class WorkProcessThread(QThread):
    finished_signal = Signal()
    error_signal = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Conecta o logger da thread ao sinal de log
        from execute_web import work
        work.log_signal.connect(self.parent().update_oupdate_logtput)  # Assumindo que o parent é MainWindow
        
    def run(self):
        try:
            # Importa e executa o código principal
            from execute_web import main  # Supondo que você tem uma função principal
            main()
            self.finished_signal.emit()
        except Exception as e:
            self.finished_signal.emit(str(e))

    
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
        
class FrmLogExecusao(QDialog,Ui_frm_log_execusao):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Log de Execução")
        self.read_log()
        self.bnt_quit.clicked.connect(self.close)
        self.bnt_clear_file.clicked.connect(self.clear_log_file)
        self.bnt_copy_file.clicked.connect(self.copy_log_file)
    
    @Slot()
    def clear_log_file(self):
        try:
            with open("log.txt", "w", encoding="utf-8") as log_file:
                log_file.write("")
            self.plainTextEdit.clear()
            self.plainTextEdit.setPlainText("Log de Execução")
            QMessageBox.information(self, "Log Limpo", "O log foi limpo com sucesso.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao limpar o log: {str(e)}")    
    
    def copy_log_file(self):
        try:
            if os.path.exists("log.txt"):
                os.rename("log.txt", f"log_{datetime.now().strftime("%d%m%Y%H%M")}.txt")
                QMessageBox.information(self, "Cópia do Log", "O log foi copiado com sucesso.")
                
                
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao copiar o log: {str(e)}")
        
    def read_log(self):
        try:
            with open("log.txt", "r", encoding="utf-8") as log_file:
                log_content = log_file.read()
            self.plainTextEdit.setPlainText(log_content)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao ler o log: {str(e)}")    
        
        # self.bnt_fechar.clicked.connect(self.close)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Call Booting")
        
        self.actionConfigura_es.triggered.connect(self.open_configuracao)
        self.actionRespostas.triggered.connect(lambda: CadTexto().exec())
        self.pushButton.clicked.connect(self.start_process)
        self.bnt_log.clicked.connect(self.call_save_log)
        self.bnt_clear_log.clicked.connect(self._clear_display_log)
        
        self.actionLog_de_Execus_o.triggered.connect(lambda: FrmLogExecusao().exec())
        # self.bat_thread = None
        # work.log_signal.connect(self.update_oupdate_logtput)
        # self.worker = None
        
        
        # self.bat_thread = QThread()  # Renomeado para evitar conflito
        # self.worker = None
    
    def _clear_display_log(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText("Log de Execução")
        
    def open_configuracao(self):
        self.config = Configuracao().exec()
        
    def open_texto(self):
        self.texto = CadTexto().show()
    
    def start_process(self):
        """Inicia o processo em uma thread separada"""
        self.pushButton.setDisabled(True)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Processando, por favor aguarde... ", None))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"font: 75 italic 10pt \"Sitka Subheading\";\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText("Log de Execução")
        self.plainTextEdit.appendPlainText("Iniciando o processo...")
        try:
            self.thread_log = WorkProcessThread(self)
            self.thread_log.finished_signal.connect(self.update_oupdate_logtput)
            # self.thread_log.error_signal.connect(self.on_process_error)
            self.thread_log.start()
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Erro ao iniciar o processo: {str(e)}")
            self.pushButton.setDisabled(False)
            self.label.setText(QCoreApplication.translate("MainWindow", u"Erro ao iniciar o processo.", None))
            self.pushButton.setStyleSheet(u"QPushButton{\n"
"font: 75 italic 10pt \"Sitka Subheading\";\n"
"background-color: rgb(170, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"	font: 10pt \"Nirmala UI\";\n"
"\n"
"}\n"
"")
              
        
    # def on_process_finished(self):
    #     self.ui.statusbar.showMessage("Processo concluído com sucesso!")
        
    # def on_process_error(self, error_msg):
    #     self.ui.statusbar.showMessage(f"Erro: {error_msg}")
    #     self.log_message(f"ERRO: {error_msg}")
        
    def update_oupdate_logtput(self, text):
        """Atualiza o QPlainTextEdit com a saída em tempo real."""
        if text == 'Todos os Tickets Foram Processados':
            self.plainTextEdit.appendPlainText(f'{text} {datetime.now()}')
            self.pushButton.setDisabled(False)
            
            self.thread_log.quit()
            self.label.setText(QCoreApplication.translate("MainWindow", u"Execute com consci\u00eancia, lebresse, n\u00e3o existe retorno. ", None))
            self.pushButton.setStyleSheet(u"QPushButton{\n"
"font: 75 italic 10pt \"Sitka Subheading\";\n"
"background-color: rgb(170, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"	font: 10pt \"Nirmala UI\";\n"
"\n"
"}\n"
"")
            
 
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
        """Override close event to confirm exit."""
        reply = QMessageBox.question(self, 'Confirmação', 'Você realmente deseja sair?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.thread_log.terminate()  # Termina a thread se estiver em execução
            self.thread_log.quit()
        else:
            # Cancel the close event
            event.ignore()
            # Optionally, you can show a message box or perform other actions here
            # QMessageBox.information(self, 'Atenção', 'A aplicação não será fechada.')
            # If you want to ignore the close event, just call event.ignore()
            # or you can call event.accept() to close the application
        # if event.key() == Qt.Key_Escape:
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet('dark'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())