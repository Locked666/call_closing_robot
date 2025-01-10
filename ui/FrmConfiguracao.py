# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmConfiguracao.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(628, 357)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_central = QFrame(self.frame)
        self.frm_central.setObjectName(u"frm_central")
        self.frm_central.setEnabled(False)
        self.frm_central.setFrameShape(QFrame.StyledPanel)
        self.frm_central.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frm_central)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 321, 121))
        self.check_ver_senha = QCheckBox(self.groupBox)
        self.check_ver_senha.setObjectName(u"check_ver_senha")
        self.check_ver_senha.setGeometry(QRect(220, 80, 81, 17))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 181, 41))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.text_usuario = QLineEdit(self.widget)
        self.text_usuario.setObjectName(u"text_usuario")

        self.verticalLayout_3.addWidget(self.text_usuario)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 60, 181, 41))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.text_senha = QLineEdit(self.widget1)
        self.text_senha.setObjectName(u"text_senha")
        self.text_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.text_senha)

        self.groupBox_2 = QGroupBox(self.frm_central)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 140, 321, 121))
        self.widget2 = QWidget(self.groupBox_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 20, 301, 41))
        self.verticalLayout_5 = QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.text_url = QLineEdit(self.widget2)
        self.text_url.setObjectName(u"text_url")

        self.verticalLayout_5.addWidget(self.text_url)


        self.verticalLayout_2.addWidget(self.frm_central)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 41))
        self.frame_2.setMaximumSize(QSize(16777215, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.widget3 = QWidget(self.frame_2)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(330, 10, 239, 25))
        self.horizontalLayout = QHBoxLayout(self.widget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bnt_salvar = QPushButton(self.widget3)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_alterar = QPushButton(self.widget3)
        self.bnt_alterar.setObjectName(u"bnt_alterar")

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.bnt_cancelar = QPushButton(self.widget3)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)
        self.bnt_alterar.clicked["bool"].connect(self.frm_central.setDisabled)
        self.bnt_alterar.clicked["bool"].connect(self.bnt_salvar.setDisabled)
        self.bnt_alterar.clicked["bool"].connect(self.bnt_alterar.setEnabled)
        self.bnt_cancelar.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Senha de Usu\u00e1rio", None))
        self.check_ver_senha.setText(QCoreApplication.translate("Form", u"Ver Senha.", None))
        self.label.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Senha :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Configura\u00e7\u00f5es Site", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"url padr\u00e3o :", None))
        self.bnt_salvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.bnt_alterar.setText(QCoreApplication.translate("Form", u"Alterar", None))
        self.bnt_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

