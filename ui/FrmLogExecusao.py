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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 121))
        self.frame_2.setMaximumSize(QSize(16777215, 121))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 70, 75, 23))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 83, 41))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2025, 1, 10))

        self.verticalLayout_5.addWidget(self.dateEdit)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 7, 0, 0)
        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(frm_log_execusao)

        QMetaObject.connectSlotsByName(frm_log_execusao)
    # setupUi

    def retranslateUi(self, frm_log_execusao):
        frm_log_execusao.setWindowTitle(QCoreApplication.translate("frm_log_execusao", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("frm_log_execusao", u"Filtro", None))
        self.pushButton.setText(QCoreApplication.translate("frm_log_execusao", u"Pesquisar", None))
        self.label.setText(QCoreApplication.translate("frm_log_execusao", u"Data", None))
    # retranslateUi

