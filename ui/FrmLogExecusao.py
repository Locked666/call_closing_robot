# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmLogExecusao.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_frm_log_execusao(object):
    def setupUi(self, frm_log_execusao):
        if not frm_log_execusao.objectName():
            frm_log_execusao.setObjectName(u"frm_log_execusao")
        frm_log_execusao.resize(751, 438)
        self.verticalLayout = QVBoxLayout(frm_log_execusao)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(frm_log_execusao)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setCenterOnScroll(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bnt_clear_file = QPushButton(self.frame_3)
        self.bnt_clear_file.setObjectName(u"bnt_clear_file")

        self.horizontalLayout.addWidget(self.bnt_clear_file)

        self.bnt_copy_file = QPushButton(self.frame_3)
        self.bnt_copy_file.setObjectName(u"bnt_copy_file")

        self.horizontalLayout.addWidget(self.bnt_copy_file)

        self.bnt_quit = QPushButton(self.frame_3)
        self.bnt_quit.setObjectName(u"bnt_quit")

        self.horizontalLayout.addWidget(self.bnt_quit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(frm_log_execusao)

        QMetaObject.connectSlotsByName(frm_log_execusao)
    # setupUi

    def retranslateUi(self, frm_log_execusao):
        frm_log_execusao.setWindowTitle(QCoreApplication.translate("frm_log_execusao", u"Form", None))
        self.bnt_clear_file.setText(QCoreApplication.translate("frm_log_execusao", u"Apagar Arquivo de Log.", None))
        self.bnt_copy_file.setText(QCoreApplication.translate("frm_log_execusao", u"Fazer uma Copia", None))
        self.bnt_quit.setText(QCoreApplication.translate("frm_log_execusao", u"Sair", None))
    # retranslateUi

