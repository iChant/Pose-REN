# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'standardcaptureform.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_standardCaptureForm(object):
    def setupUi(self, standardCaptureForm):
        if standardCaptureForm.objectName():
            standardCaptureForm.setObjectName(u"standardCaptureForm")
        standardCaptureForm.setWindowModality(Qt.ApplicationModal)
        standardCaptureForm.resize(838, 678)
        self.gridLayout_2 = QGridLayout(standardCaptureForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.startButton = QPushButton(standardCaptureForm)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 1)

        self.stopButton = QPushButton(standardCaptureForm)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout_2.addWidget(self.stopButton, 1, 1, 1, 1)

        self.backButton = QPushButton(standardCaptureForm)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout_2.addWidget(self.backButton, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(standardCaptureForm)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)


        self.retranslateUi(standardCaptureForm)

        QMetaObject.connectSlotsByName(standardCaptureForm)
    # setupUi

    def retranslateUi(self, standardCaptureForm):
        standardCaptureForm.setWindowTitle(QCoreApplication.translate("standardCaptureForm", u"Standard gesture capture", None))
        self.startButton.setText(QCoreApplication.translate("standardCaptureForm", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("standardCaptureForm", u"Stop", None))
        self.backButton.setText(QCoreApplication.translate("standardCaptureForm", u"Back", None))
        self.label.setText(QCoreApplication.translate("standardCaptureForm", u"LOADING...", None))
    # retranslateUi

