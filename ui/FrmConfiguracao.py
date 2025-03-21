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
        Form.resize(401, 387)
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
        self.verticalLayout_7 = QVBoxLayout(self.frm_central)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.frm_central)
        self.groupBox.setObjectName(u"groupBox")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 21, 341, 102))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.text_usuario = QLineEdit(self.widget)
        self.text_usuario.setObjectName(u"text_usuario")

        self.verticalLayout_3.addWidget(self.text_usuario)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, -1, -1, -1)
        self.text_senha = QLineEdit(self.widget)
        self.text_senha.setObjectName(u"text_senha")
        self.text_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.text_senha)

        self.check_ver_senha = QCheckBox(self.widget)
        self.check_ver_senha.setObjectName(u"check_ver_senha")

        self.horizontalLayout_3.addWidget(self.check_ver_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frm_central)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 23, 341, 54))
        self.verticalLayout_5 = QVBoxLayout(self.widget1)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.text_url = QLineEdit(self.widget1)
        self.text_url.setObjectName(u"text_url")

        self.verticalLayout_5.addWidget(self.text_url)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.verticalLayout_2.addWidget(self.frm_central)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 41))
        self.frame_2.setMaximumSize(QSize(16777215, 69))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.bnt_salvar = QPushButton(self.frame_2)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_alterar = QPushButton(self.frame_2)
        self.bnt_alterar.setObjectName(u"bnt_alterar")

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.bnt_cancelar = QPushButton(self.frame_2)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


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
        self.label.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Senha :", None))
        self.check_ver_senha.setText(QCoreApplication.translate("Form", u"Ver Senha.", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Configura\u00e7\u00f5es Site", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"url padr\u00e3o :", None))
        self.bnt_salvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.bnt_alterar.setText(QCoreApplication.translate("Form", u"Alterar", None))
        self.bnt_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

