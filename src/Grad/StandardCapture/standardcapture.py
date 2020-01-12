from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap, QImage
from src.Grad.StandardCapture.ui_standardcaptureform import Ui_standardCaptureForm
from src.Grad.StandardCapture.standardsave import SaveDialog
import sys
from multiprocessing import Process, Queue
from src.Grad.HandPose.HandPose import run
import time
# import pyrealsense2 as rs
import os
import numpy as np


class StandardCapture(QWidget, Ui_standardCaptureForm):
    def __init__(self):
        super(StandardCapture, self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.backButton.clicked.connect(self.back)

        self.startButton.setDisabled(False)
        self.backButton.setDisabled(False)
        self.stopButton.setDisabled(True)

        self.is_running = False
        self.timer = QTimer()
        self.q = Queue()
        self.worker = Process(target=run, args=(self.q,))
        self.worker.start()
        print('sc: ', os.getpid())
        self.timer.start(int(1000/30))
        self.timer.timeout.connect(self.get_pose)
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
        save_dialog = SaveDialog()
        if save_dialog.exec_():
            savepath = save_dialog.get_savepath()
            np.save(savepath, self.recorded_data)
            print(savepath)

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


if __name__ == '__main__':
    # import os
    # # import sys
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ROOT_DIR = os.path.dirname(BASE_DIR)
    # # sys.path.append(ROOT_DIR)  # config
    # ROOT_DIR = os.path.dirname(ROOT_DIR)
    # sys.path.append(ROOT_DIR)  # config
    # sys.path.append(os.path.join(ROOT_DIR, 'utils'))  # utils
    # sys.path.append(os.path.join(ROOT_DIR, 'libs'))
    app = QApplication([])
    window = StandardCapture()
    window.show()
    sys.exit(app.exec_())
