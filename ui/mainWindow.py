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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateEdit,
    QFrame, QGroupBox, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 510)
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
        self.frame_2.setMinimumSize(QSize(712, 161))
        self.frame_2.setMaximumSize(QSize(16777215, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 461, 131))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 10, 241, 111))
        self.check_sys_contabil = QCheckBox(self.groupBox_2)
        self.check_sys_contabil.setObjectName(u"check_sys_contabil")
        self.check_sys_contabil.setGeometry(QRect(10, 20, 111, 17))
        self.check_sys_contabil.setChecked(True)
        self.check_sys_compras = QCheckBox(self.groupBox_2)
        self.check_sys_compras.setObjectName(u"check_sys_compras")
        self.check_sys_compras.setGeometry(QRect(10, 40, 111, 17))
        self.check_sys_compras.setChecked(True)
        self.check_sys_licitacao = QCheckBox(self.groupBox_2)
        self.check_sys_licitacao.setObjectName(u"check_sys_licitacao")
        self.check_sys_licitacao.setGeometry(QRect(10, 60, 111, 17))
        self.check_sys_licitacao.setChecked(True)
        self.check_sys_arh = QCheckBox(self.groupBox_2)
        self.check_sys_arh.setObjectName(u"check_sys_arh")
        self.check_sys_arh.setGeometry(QRect(10, 80, 111, 17))
        self.check_sys_arh.setChecked(True)
        self.check_sys_solicitaoweb = QCheckBox(self.groupBox_2)
        self.check_sys_solicitaoweb.setObjectName(u"check_sys_solicitaoweb")
        self.check_sys_solicitaoweb.setGeometry(QRect(110, 60, 111, 17))
        self.check_sys_solicitaoweb.setChecked(True)
        self.check_sys_gecom = QCheckBox(self.groupBox_2)
        self.check_sys_gecom.setObjectName(u"check_sys_gecom")
        self.check_sys_gecom.setGeometry(QRect(110, 80, 111, 17))
        self.check_sys_gecom.setChecked(True)
        self.check_sys_siart = QCheckBox(self.groupBox_2)
        self.check_sys_siart.setObjectName(u"check_sys_siart")
        self.check_sys_siart.setGeometry(QRect(110, 20, 111, 17))
        self.check_sys_siart.setChecked(True)
        self.check_sys_docfacil = QCheckBox(self.groupBox_2)
        self.check_sys_docfacil.setObjectName(u"check_sys_docfacil")
        self.check_sys_docfacil.setGeometry(QRect(110, 40, 111, 17))
        self.check_sys_docfacil.setChecked(True)
        self.check_param_browser = QCheckBox(self.groupBox)
        self.check_param_browser.setObjectName(u"check_param_browser")
        self.check_param_browser.setGeometry(QRect(10, 70, 111, 17))
        self.check_param_browser.setChecked(True)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 111, 41))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.date_execucao = QDateEdit(self.widget)
        self.date_execucao.setObjectName(u"date_execucao")
        self.date_execucao.setWrapping(False)
        self.date_execucao.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_execucao.setAccelerated(False)
        self.date_execucao.setCalendarPopup(True)
        self.date_execucao.setDate(QDate(2025, 1, 10))

        self.verticalLayout_4.addWidget(self.date_execucao)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 10, 181, 91))
        self.label.setStyleSheet(u"font: 87 italic 16pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 100, 201, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 255, 0);")

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView = QListView(self.frame_3)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_3.addWidget(self.listView)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 21))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Round com os sistemas. ", None))
        self.check_sys_contabil.setText(QCoreApplication.translate("MainWindow", u"Contabilidade ", None))
        self.check_sys_compras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.check_sys_licitacao.setText(QCoreApplication.translate("MainWindow", u"Licita\u00e7\u00e3o", None))
        self.check_sys_arh.setText(QCoreApplication.translate("MainWindow", u"ARH", None))
        self.check_sys_solicitaoweb.setText(QCoreApplication.translate("MainWindow", u"Solicita\u00e7\u00e3o Web", None))
        self.check_sys_gecom.setText(QCoreApplication.translate("MainWindow", u"Gecom", None))
        self.check_sys_siart.setText(QCoreApplication.translate("MainWindow", u"Siart", None))
        self.check_sys_docfacil.setText(QCoreApplication.translate("MainWindow", u"DocF\u00e1cil", None))
        self.check_param_browser.setText(QCoreApplication.translate("MainWindow", u"Ocultar Navegador", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data de Fechamento", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Execute com consci\u00eancia, lebresse, n\u00e3o existe retorno. ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.menuSistema.setTitle(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.menuExecus_o.setTitle(QCoreApplication.translate("MainWindow", u"Execus\u00e3o", None))
    # retranslateUi

