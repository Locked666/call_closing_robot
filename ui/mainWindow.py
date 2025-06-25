# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 551)
        self.actionRespostas = QAction(MainWindow)
        self.actionRespostas.setObjectName(u"actionRespostas")
        self.actionSistemas = QAction(MainWindow)
        self.actionSistemas.setObjectName(u"actionSistemas")
        self.actionConfigura_es = QAction(MainWindow)
        self.actionConfigura_es.setObjectName(u"actionConfigura_es")
        self.actionLog_de_Execus_o = QAction(MainWindow)
        self.actionLog_de_Execus_o.setObjectName(u"actionLog_de_Execus_o")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(712, 176))
        self.frame_2.setMaximumSize(QSize(16777215, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(10, 0, 461, 161))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 121, 41))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.check_param_browser = QCheckBox(self.layoutWidget)
        self.check_param_browser.setObjectName(u"check_param_browser")
        self.check_param_browser.setChecked(True)

        self.verticalLayout_5.addWidget(self.check_param_browser)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 0, 241, 101))
        self.label.setStyleSheet(u"font: 87 italic 16pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 100, 201, 51))
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

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setCenterOnScroll(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bnt_log = QPushButton(self.frame_3)
        self.bnt_log.setObjectName(u"bnt_log")
        self.bnt_log.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.bnt_log)

        self.bnt_clear_log = QPushButton(self.frame_3)
        self.bnt_clear_log.setObjectName(u"bnt_clear_log")
        self.bnt_clear_log.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.bnt_clear_log)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 763, 21))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuSistema = QMenu(self.menubar)
        self.menuSistema.setObjectName(u"menuSistema")
        self.menuExecus_o = QMenu(self.menubar)
        self.menuExecus_o.setObjectName(u"menuExecus_o")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuExecus_o.menuAction())
        self.menuCadastro.addAction(self.actionRespostas)
        self.menuSistema.addAction(self.actionConfigura_es)
        self.menuExecus_o.addAction(self.actionLog_de_Execus_o)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRespostas.setText(QCoreApplication.translate("MainWindow", u"Respostas", None))
        self.actionSistemas.setText(QCoreApplication.translate("MainWindow", u"Sistemas", None))
        self.actionConfigura_es.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.actionLog_de_Execus_o.setText(QCoreApplication.translate("MainWindow", u"Log de Execus\u00e3o", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parametros de Execu\u00e7\u00e3o", None))
        self.check_param_browser.setText(QCoreApplication.translate("MainWindow", u"Ocultar Navegador", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Execute com consci\u00eancia, lebresse, n\u00e3o existe retorno. ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.bnt_log.setText(QCoreApplication.translate("MainWindow", u"Salvar Log", None))
        self.bnt_clear_log.setText(QCoreApplication.translate("MainWindow", u"Apagar Log", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.menuSistema.setTitle(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.menuExecus_o.setTitle(QCoreApplication.translate("MainWindow", u"Execus\u00e3o", None))
    # retranslateUi

