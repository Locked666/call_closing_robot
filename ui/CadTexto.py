# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadTexto.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_CadTexto(object):
    def setupUi(self, CadTexto):
        if not CadTexto.objectName():
            CadTexto.setObjectName(u"CadTexto")
        CadTexto.resize(669, 450)
        self.verticalLayout = QVBoxLayout(CadTexto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(CadTexto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 111))
        self.frame.setMaximumSize(QSize(168000, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lcd_id = QLCDNumber(self.frame)
        self.lcd_id.setObjectName(u"lcd_id")
        self.lcd_id.setGeometry(QRect(10, 10, 64, 23))
        self.plaintext_conteudo = QPlainTextEdit(self.frame)
        self.plaintext_conteudo.setObjectName(u"plaintext_conteudo")
        self.plaintext_conteudo.setGeometry(QRect(100, 10, 511, 71))
        self.plaintext_conteudo.setTabChangesFocus(False)
        self.plaintext_conteudo.setUndoRedoEnabled(True)
        self.plaintext_conteudo.setOverwriteMode(False)
        self.plaintext_conteudo.setBackgroundVisible(False)
        self.plaintext_conteudo.setCenterOnScroll(False)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(210, 80, 401, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bnt_inserir = QPushButton(self.widget)
        self.bnt_inserir.setObjectName(u"bnt_inserir")
        self.bnt_inserir.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout.addWidget(self.bnt_inserir)

        self.bnt_gravar = QPushButton(self.widget)
        self.bnt_gravar.setObjectName(u"bnt_gravar")
        self.bnt_gravar.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.horizontalLayout.addWidget(self.bnt_gravar)

        self.bnt_cancelar = QPushButton(self.widget)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.bnt_cancelar)

        self.bnt_clear_display = QPushButton(self.widget)
        self.bnt_clear_display.setObjectName(u"bnt_clear_display")
        self.bnt_clear_display.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.horizontalLayout.addWidget(self.bnt_clear_display)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CadTexto)

        QMetaObject.connectSlotsByName(CadTexto)
    # setupUi

    def retranslateUi(self, CadTexto):
        CadTexto.setWindowTitle(QCoreApplication.translate("CadTexto", u"Form", None))
        self.plaintext_conteudo.setDocumentTitle("")
        self.plaintext_conteudo.setPlainText("")
        self.plaintext_conteudo.setPlaceholderText(QCoreApplication.translate("CadTexto", u"Insira o texto e clique em inserir para adicionar um novo ou em grava caso esteja editando.", None))
        self.bnt_inserir.setText(QCoreApplication.translate("CadTexto", u"Inserir", None))
        self.bnt_gravar.setText(QCoreApplication.translate("CadTexto", u"Gravar", None))
        self.bnt_cancelar.setText(QCoreApplication.translate("CadTexto", u"Cancelar", None))
        self.bnt_clear_display.setText(QCoreApplication.translate("CadTexto", u"Limpar Tela", None))
    # retranslateUi

