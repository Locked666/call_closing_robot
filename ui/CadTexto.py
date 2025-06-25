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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLCDNumber, QPlainTextEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_CadTexto(object):
    def setupUi(self, CadTexto):
        if not CadTexto.objectName():
            CadTexto.setObjectName(u"CadTexto")
        CadTexto.resize(805, 455)
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
        self.plaintext_conteudo.setGeometry(QRect(100, 0, 511, 71))
        self.plaintext_conteudo.setTabChangesFocus(False)
        self.plaintext_conteudo.setUndoRedoEnabled(True)
        self.plaintext_conteudo.setOverwriteMode(False)
        self.plaintext_conteudo.setBackgroundVisible(False)
        self.plaintext_conteudo.setCenterOnScroll(False)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 80, 511, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bnt_inserir = QPushButton(self.layoutWidget)
        self.bnt_inserir.setObjectName(u"bnt_inserir")
        self.bnt_inserir.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bnt_inserir)

        self.bnt_editar = QPushButton(self.layoutWidget)
        self.bnt_editar.setObjectName(u"bnt_editar")
        self.bnt_editar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bnt_editar)

        self.bnt_excluir = QPushButton(self.layoutWidget)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_clear_display = QPushButton(self.layoutWidget)
        self.bnt_clear_display.setObjectName(u"bnt_clear_display")
        self.bnt_clear_display.setStyleSheet(u"")

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
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty(u"showDropIndicator", False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)

        self.verticalLayout_3.addWidget(self.tableWidget)


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
        self.bnt_editar.setText(QCoreApplication.translate("CadTexto", u"Editar", None))
        self.bnt_excluir.setText(QCoreApplication.translate("CadTexto", u"Excluir", None))
        self.bnt_clear_display.setText(QCoreApplication.translate("CadTexto", u"Limpar Tela", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CadTexto", u"Index", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CadTexto", u"Texto", None));
    # retranslateUi

