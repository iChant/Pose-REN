# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gesturelearning.ui'
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

class Ui_GestureLearningDialog(object):
    def setupUi(self, GestureLearningDialog):
        if GestureLearningDialog.objectName():
            GestureLearningDialog.setObjectName(u"GestureLearningDialog")
        GestureLearningDialog.setWindowModality(Qt.ApplicationModal)
        GestureLearningDialog.resize(909, 711)
        self.gridLayout_2 = QGridLayout(GestureLearningDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.startButton = QPushButton(GestureLearningDialog)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 1)

        self.stopButton = QPushButton(GestureLearningDialog)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout_2.addWidget(self.stopButton, 1, 1, 1, 1)

        self.backButton = QPushButton(GestureLearningDialog)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout_2.addWidget(self.backButton, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(GestureLearningDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)


        self.retranslateUi(GestureLearningDialog)

        QMetaObject.connectSlotsByName(GestureLearningDialog)
    # setupUi

    def retranslateUi(self, GestureLearningDialog):
        GestureLearningDialog.setWindowTitle(QCoreApplication.translate("GestureLearningDialog", u"Gesture Learning", None))
        self.startButton.setText(QCoreApplication.translate("GestureLearningDialog", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("GestureLearningDialog", u"Stop", None))
        self.backButton.setText(QCoreApplication.translate("GestureLearningDialog", u"Back", None))
        self.label.setText(QCoreApplication.translate("GestureLearningDialog", u"LOADING...", None))
    # retranslateUi

