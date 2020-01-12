# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'targetgesturelearning.ui'
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

class Ui_TargetGestureLearningDialog(object):
    def setupUi(self, TargetGestureLearningDialog):
        if TargetGestureLearningDialog.objectName():
            TargetGestureLearningDialog.setObjectName(u"TargetGestureLearningDialog")
        TargetGestureLearningDialog.resize(952, 510)
        self.gridLayout_3 = QGridLayout(TargetGestureLearningDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.startButton = QPushButton(TargetGestureLearningDialog)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout_3.addWidget(self.startButton, 1, 0, 1, 1)

        self.stopButton = QPushButton(TargetGestureLearningDialog)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout_3.addWidget(self.stopButton, 1, 1, 1, 1)

        self.backButton = QPushButton(TargetGestureLearningDialog)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout_3.addWidget(self.backButton, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.standardGestureLayout = QGridLayout()
        self.standardGestureLayout.setObjectName(u"standardGestureLayout")

        self.gridLayout.addLayout(self.standardGestureLayout, 1, 0, 1, 1)

        self.userGestureLayout = QGridLayout()
        self.userGestureLayout.setObjectName(u"userGestureLayout")
        self.label = QLabel(TargetGestureLearningDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.userGestureLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.userGestureLayout, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 3)


        self.retranslateUi(TargetGestureLearningDialog)

        QMetaObject.connectSlotsByName(TargetGestureLearningDialog)
    # setupUi

    def retranslateUi(self, TargetGestureLearningDialog):
        TargetGestureLearningDialog.setWindowTitle(QCoreApplication.translate("TargetGestureLearningDialog", u"Target Gesture Learning", None))
        self.startButton.setText(QCoreApplication.translate("TargetGestureLearningDialog", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("TargetGestureLearningDialog", u"Stop", None))
        self.backButton.setText(QCoreApplication.translate("TargetGestureLearningDialog", u"Back", None))
        self.label.setText(QCoreApplication.translate("TargetGestureLearningDialog", u"INITING CAMERA...", None))
    # retranslateUi

