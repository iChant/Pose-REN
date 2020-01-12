from PySide2.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QPushButton, QWidget)
from PySide2.QtDataVisualization import QtDataVisualization
from src.Grad.MainWindow.ui_mainwindow import Ui_MainWindow
from src.Grad.HandModel.handmodel import HandModel

from src.Grad.StandardCapture.standardcapture import StandardCapture

import numpy as np
import sys
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start)
        self.standardCaptureButton.clicked.connect(self.standard_capture)
        self.exitButton.clicked.connect(self.exit)
        self.front_icon = np.load('src/Grad/MainWindow/front_icon.npy')
        self.handgraph = HandModel(self.front_icon)
        self.poseContainer = QWidget.createWindowContainer(
            self.handgraph.scatter_graph)
        self.poseLayout.addWidget(self.poseContainer)
        self.setLayout(self.poseLayout)

    def start(self):
        pass

    def standard_capture(self):
        self.sc = StandardCapture()
        self.sc.show()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
