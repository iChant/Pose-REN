from PySide2.QtWidgets import QDialog, QApplication, QWidget
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import QTimer
from src.Grad.TargetGestureLearningDialog.ui_targetgesturelearning import Ui_TargetGestureLearningDialog
from src.Grad.HandModel.handmodel import HandModel
import sys
import os
from multiprocessing import Process, Queue
from src.Grad.HandPose.HandPose import run
import time
import numpy as np


class TargetGestureLearningDialog(QDialog, Ui_TargetGestureLearningDialog):
    def __init__(self, g_type, parent=None):
        super(TargetGestureLearningDialog, self).__init__(parent=parent)
        self.setupUi(self)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.backButton.clicked.connect(self.back)

        self.startButton.setDisabled(False)
        self.backButton.setDisabled(False)
        self.stopButton.setDisabled(True)

        self.standard_gesture = g_type
        self.standard_it = iter(self.standard_gesture)

        self.is_running = False
        self.pose_timer = QTimer()
        self.model_timer = QTimer()
        self.standard_graph = HandModel()
        self.standard_pose_container = QWidget.createWindowContainer(
            self.standard_graph.scatter_graph)
        self.standardGestureLayout.addWidget(self.standard_pose_container)
        self.setLayout(self.standardGestureLayout)

        self.q = Queue()
        self.worker = Process(target=run, args=(self.q,))
        self.worker.start()
        # print('sc: ', os.getpid())
        self.pose_timer.start(int(1000 / 30))
        self.model_timer.start(int(1000 / 20))
        self.pose_timer.timeout.connect(self.get_pose)
        self.model_timer.timeout.connect(self.get_model_frame)
        self.recorded_data = []

    def start(self):
        self.is_running = True
        self.startButton.setDisabled(True)
        self.stopButton.setDisabled(False)
        self.backButton.setDisabled(True)
        # m = self.q.get()
        # print('sss')
        # self.timer.start(int(1000/30))
        # self.timer.timeout.connect(self.get_pose)

    def stop(self):
        self.is_running = False
        # self.timer.stop()
        self.q.put('exit')
        self.startButton.setDisabled(False)
        self.backButton.setDisabled(False)
        self.stopButton.setDisabled(True)
        # save_dialog = SaveDialog()
        # if save_dialog.exec_():
        #     savepath = save_dialog.get_savepath()
        #     np.save(savepath, self.recorded_data)
        #     print(savepath)

        self.recorded_data = []

        time.sleep(1)

    def back(self):
        self.worker.terminate()
        self.recorded_data = []
        self.close()

    def get_pose(self):
        try:
            res = self.q.get(False)
            assert (type(res) == dict)
            img_show = res['img_show']
            showImage = QImage(
                img_show, img_show.shape[1], img_show.shape[0], QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(showImage))
            if self.is_running:
                self.recorded_data.append(res['results'])
        except Exception as e:
            pass

    def read_standard_gesture(self, g_type):
        try:
            self.standard_gesture = np.load(os.path.join('dataset', g_type))
            self.standard_it = iter(self.standard_gesture)
        except FileNotFoundError as e:
            print(e)

    def get_model_frame(self):
        try:
            self.standard_graph.refresh(next(self.standard_it))
        except StopIteration:
            self.standard_it = iter(self.standard_gesture)


if __name__ == "__main__":
    b1 = np.load('bbb-1.npy')
    # b2 = np.load('dataset/c-2.npy')
    app = QApplication([])
    window = TargetGestureLearningDialog(b1)
    window.show()
    sys.exit(app.exec_())
