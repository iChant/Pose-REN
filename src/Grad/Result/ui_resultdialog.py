# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
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

class Ui_ResultDialog(object):
    def setupUi(self, ResultDialog):
        if ResultDialog.objectName():
            ResultDialog.setObjectName(u"ResultDialog")
        ResultDialog.resize(762, 861)
        self.gridLayout_3 = QGridLayout(ResultDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pauseButton = QPushButton(ResultDialog)
        self.pauseButton.setObjectName(u"pauseButton")

        self.gridLayout_3.addWidget(self.pauseButton, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(ResultDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 6, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.standardLayout = QGridLayout()
        self.standardLayout.setObjectName(u"standardLayout")

        self.gridLayout_2.addLayout(self.standardLayout, 1, 0, 1, 1)

        self.userLayout = QGridLayout()
        self.userLayout.setObjectName(u"userLayout")

        self.gridLayout_2.addLayout(self.userLayout, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 7, 2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setContentsMargins(10, 30, 10, 10)
        self.label = QLabel(ResultDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75);
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(ResultDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.label_4 = QLabel(ResultDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.totalDistLable = QLabel(ResultDialog)
        self.totalDistLable.setObjectName(u"totalDistLable")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.totalDistLable)

        self.label_5 = QLabel(ResultDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.thumbDistLable = QLabel(ResultDialog)
        self.thumbDistLable.setObjectName(u"thumbDistLable")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.thumbDistLable)

        self.label_13 = QLabel(ResultDialog)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.indexDistLable = QLabel(ResultDialog)
        self.indexDistLable.setObjectName(u"indexDistLable")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.indexDistLable)

        self.label_15 = QLabel(ResultDialog)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.middleDistLable = QLabel(ResultDialog)
        self.middleDistLable.setObjectName(u"middleDistLable")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.middleDistLable)

        self.label_17 = QLabel(ResultDialog)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.ringDistLable = QLabel(ResultDialog)
        self.ringDistLable.setObjectName(u"ringDistLable")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ringDistLable)

        self.label_19 = QLabel(ResultDialog)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_19)

        self.pinkyDistLable = QLabel(ResultDialog)
        self.pinkyDistLable.setObjectName(u"pinkyDistLable")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pinkyDistLable)


        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 3, 1)

        self.pushButton = QPushButton(ResultDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.pushButton, 5, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.tipLabel = QLabel(ResultDialog)
        self.tipLabel.setObjectName(u"tipLabel")
        self.tipLabel.setEnabled(False)
        self.tipLabel.setMaximumSize(QSize(208, 138))
        font1 = QFont()
        font1.setPointSize(12)
        self.tipLabel.setFont(font1)
        self.tipLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.tipLabel)


        self.gridLayout_3.addLayout(self.verticalLayout, 3, 0, 1, 1)


        self.retranslateUi(ResultDialog)

        QMetaObject.connectSlotsByName(ResultDialog)
    # setupUi

    def retranslateUi(self, ResultDialog):
        ResultDialog.setWindowTitle(QCoreApplication.translate("ResultDialog", u"Result", None))
        self.pauseButton.setText(QCoreApplication.translate("ResultDialog", u"Pause", None))
        self.pushButton_2.setText(QCoreApplication.translate("ResultDialog", u"Back", None))
        self.label.setText(QCoreApplication.translate("ResultDialog", u"Fingle", None))
        self.label_2.setText(QCoreApplication.translate("ResultDialog", u"Score", None))
        self.label_4.setText(QCoreApplication.translate("ResultDialog", u"Total", None))
        self.totalDistLable.setText(QCoreApplication.translate("ResultDialog", u"Total dist", None))
        self.label_5.setText(QCoreApplication.translate("ResultDialog", u"Thumb", None))
        self.thumbDistLable.setText(QCoreApplication.translate("ResultDialog", u"Thumb dist", None))
        self.label_13.setText(QCoreApplication.translate("ResultDialog", u"Index", None))
        self.indexDistLable.setText(QCoreApplication.translate("ResultDialog", u"Index dist", None))
        self.label_15.setText(QCoreApplication.translate("ResultDialog", u"Middle", None))
        self.middleDistLable.setText(QCoreApplication.translate("ResultDialog", u"Middle dist", None))
        self.label_17.setText(QCoreApplication.translate("ResultDialog", u"Ring", None))
        self.ringDistLable.setText(QCoreApplication.translate("ResultDialog", u"Ring dist", None))
        self.label_19.setText(QCoreApplication.translate("ResultDialog", u"Pinky", None))
        self.pinkyDistLable.setText(QCoreApplication.translate("ResultDialog", u"Pinky dist", None))
        self.pushButton.setText(QCoreApplication.translate("ResultDialog", u"Time Wrapped", None))
        self.tipLabel.setText(QCoreApplication.translate("ResultDialog", u"TextLabel", None))
    # retranslateUi

