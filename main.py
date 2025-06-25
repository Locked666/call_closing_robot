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

from PySide6.QtCore import Signal,QThread, QSize, QCoreApplication,Slot#, QModelIndex#,SLOT,Qt,QFile,QRect,QObject, QTime,QAbstractTableModel,QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog,QLineEdit, QMessageBox, QTableWidgetItem,QHeaderView#,QWidget,QVBoxLayout,QWidgetAction,QMdiSubWindow,QCheckBox,QHeaderView,QMenu
from PySide6.QtGui import QIcon #, QKeySequence, QPixmap, QFont, QAction, QCursor#, QStandardItemModel, QStandardItem
from datetime import datetime
from pathlib import Path
from datetime import datetime#,date, time

from text_for_close import get_text_and_row, insert_text_row, edit_text_row, delete_text_row

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
    def __init__(self,icon:QIcon) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Cadastro de Texto")
        self.load_texts()
        self.setWindowIcon(icon)
        self.tableWidget.cellClicked.connect(self.on_row_clicked)
        self.bnt_inserir.clicked.connect(self.callback_insert)
        self.bnt_editar.clicked.connect(self.callback_edit_row)
        self.bnt_excluir.clicked.connect(self.callback_delete_row)
        self.bnt_clear_display.clicked.connect(lambda: self.plaintext_conteudo.clear())  # Limpa o conteúdo do QPlainTextEdit e reseta o LCD
        self.bnt_clear_display.clicked.connect(lambda: self.lcd_id.display(0))  # Limpa o conteúdo do QPlainTextEdit e reseta o LCD
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    def load_texts(self):
        self.tableWidget.setDisabled(False)
        texts = get_text_and_row()

        self.tableWidget.setRowCount(len(texts))
        self.tableWidget.setColumnCount(len(texts[0]) if texts else 0)

        for row_index, row_data in enumerate(texts):
            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_index, col_index, item)
        
    def on_row_clicked(self, row, column):
        row_data = {}  # Inicializa o dicionário com valores padrão
        self.plaintext_conteudo.clear()  # Limpa o conteúdo anterior
        for col in range(self.tableWidget.columnCount()):            
            item = self.tableWidget.item(row, col)
            if item:
                row_data[self.tableWidget.horizontalHeaderItem(col).text()] = item.text()
      
        # Atualiza o conteúdo do QPlainTextEdit
        self.plaintext_conteudo.setPlainText(row_data.get('Texto', ''))  # Usa o valor do dicionário ou uma string vazia se não existir

        # Atualiza o valor no QLCDNumber
        self.lcd_id.display(row_data.get('Index', 0))  # Usa o valor do dicionário ou 0 se não existir

    def callback_insert(self):
        """Callback para inserir um novo texto na tabela."""
        try:
            text = self.plaintext_conteudo.toPlainText().strip()
            if not text:
                raise ValueError("O texto não pode ser vazio.")
            insert_text_row(text)
            self.load_texts()
            self.plaintext_conteudo.clear()
            reply =  QMessageBox.information(self, "Sucesso", "Texto inserido com sucesso!", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.lcd_id.display(0)  # Reseta o LCD para 0 após a exclusão
                self.tableWidget.setDisabled(False)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao inserir texto: {str(e)}")

    def callback_edit_row(self):
        """Callback para editar o texto selecionado na tabela."""
        try:
            row = self.lcd_id.value()
            text = self.plaintext_conteudo.toPlainText().strip()
            if not text:
                raise ValueError("O texto não pode ser vazio.")
            edit_text_row(int(row), text)
            self.load_texts()
            self.plaintext_conteudo.clear()
            reply = QMessageBox.information(self, "Sucesso", "Texto editado com sucesso!", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.tableWidget.setDisabled(False)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao editar texto: {str(e)}")

    def callback_delete_row(self):
        """Callback para deletar o texto selecionado na tabela."""
        try:
            row = self.lcd_id.value()
            delete_text_row(int(row))
            self.load_texts()
            self.plaintext_conteudo.clear()
            reply = QMessageBox.information(self, "Sucesso", "Texto deletado com sucesso!", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                #self.tableWidget.setDisabled(False)
                pass
                self.lcd_id.display(0)  # Reseta o LCD para 0 após a exclusão
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao deletar texto: {str(e)}")

class Configuracao(QDialog,Ui_Form):
    def __init__(self, icon:QIcon) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Configurações")
        self.setWindowIcon(icon)
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
    def __init__(self,icon:QIcon) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Log de Execução")
        self.read_log()
        self.setWindowIcon(icon)
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
        icon = QIcon()
        icon.addFile(u"ico.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        self.actionConfigura_es.triggered.connect(lambda: self.open_configuracao(icon=icon))
        self.actionRespostas.triggered.connect(lambda: CadTexto(icon=icon).exec())
        self.pushButton.clicked.connect(self.start_process)
        self.bnt_log.clicked.connect(self.call_save_log)
        self.bnt_clear_log.clicked.connect(self._clear_display_log)
        
        self.actionLog_de_Execus_o.triggered.connect(lambda: FrmLogExecusao(icon=icon).exec())
    
    @Slot() 
    def _clear_display_log(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText("Log de Execução")
        
    @Slot()
    def open_configuracao(self,icon:QIcon):
        self.config = Configuracao(icon=icon).exec()
     
    @Slot()   
    def open_texto(self):
        self.texto = CadTexto().show()
    
    @Slot()
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
    
    @Slot()    
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

    @Slot()
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
            try:
                self.thread_log.terminate()  # Termina a thread se estiver em execução
                self.thread_log.quit()
            except Exception as e:
                pass
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