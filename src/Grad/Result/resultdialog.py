from src.Grad.Result.ui_resultdialog import Ui_ResultDialog
from PySide2.QtWidgets import QDialog, QWidget, QApplication, QTableWidget, QTableWidgetItem
from PySide2.QtCore import QTimer

from src.Grad.utils.chaincode import get_feature
# from src.Grad.utils.dtw import dtw
from src.Grad.HandModel.handmodel import HandModel, FINGER_INDEX

from fastdtw import fastdtw


# class TABLE_INDEX:
#     TOTAL = 0
#     THUMB = 1
#     INDEX = 2
#     MIDDLE = 3
#     RING = 4
#     PINKY = 5

TABLE_INDEX = {
    'total': 0,
    'thumb': 1,
    'index': 2,
    'middle': 3,
    'ring': 4,
    'pinky': 5
}


class ResultDialog(QDialog, Ui_ResultDialog):
    def __init__(self, user_gesture, standard_gesture, parent=None):
        super(ResultDialog, self).__init__(parent=parent)
        self.setupUi(self)
        self.standard_timer = QTimer()
        self.standard_timer.timeout.connect(self.get_standard_frame)
        self.user_timer = QTimer()
        self.user_timer.timeout.connect(self.get_user_frame)
        self.user_gesture = user_gesture
        self.standard_gesture = standard_gesture
        self.standard_timer.start(int(1000 / 10))
        self.user_timer.start(int(1000 / 10))
        self.standard_it = iter(self.standard_gesture)
        self.user_it = iter(self.user_gesture)

        self.pauseButton.clicked.connect(self.start_pause)
        self.is_paused = False
        self.user_graph = HandModel()
        self.standard_graph = HandModel()

        self.user_pose_container = QWidget.createWindowContainer(
            self.user_graph.scatter_graph)
        self.userLayout.addWidget(self.user_pose_container)
        self.setLayout(self.userLayout)

        self.standard_pose_container = QWidget.createWindowContainer(
            self.standard_graph.scatter_graph)
        self.standardLayout.addWidget(self.standard_pose_container)
        self.setLayout(self.standardLayout)

        dists = self.get_dtw()

        self.set_dist(dists)
        self.tipLabel.setEnabled(True)
        self.set_tips(dists)

        # self.set_table(dists)

    def get_frame(self, graph, data):
        graph.refresh(data)

    def get_standard_frame(self):
        try:
            self.get_frame(self.standard_graph, next(self.standard_it))
            # print('standard')
        except StopIteration:
            # print('standard stopped')
            self.standard_timer.stop()

    def get_user_frame(self):
        try:
            self.get_frame(self.user_graph, next(self.user_it))
            # print('user')
        except StopIteration:
            # print('user stopped')
            self.user_timer.stop()

    def start_pause(self):
        if self.is_paused:
            self.user_timer.start(int(1000/10))
            self.standard_timer.start(int(1000/10))
            self.pauseButton.setText('Pause')
        else:
            self.user_timer.stop()
            self.standard_timer.stop()
            self.pauseButton.setText('Start')
        self.is_paused = not self.is_paused

    def get_dtw(self):
        st_feature = get_feature(self.standard_gesture)
        us_feature = get_feature(self.user_gesture)
        st_finger_feats = {
            'thumb': [st_feature[i] for i in FINGER_INDEX.THUMB_INDEX()],
            'index': [st_feature[i] for i in FINGER_INDEX.INDEX_INDEX()],
            'middle': [st_feature[i] for i in FINGER_INDEX.MIDDLE_INDEX()],
            'ring': [st_feature[i] for i in FINGER_INDEX.RING_INDEX()],
            'pinky': [st_feature[i] for i in FINGER_INDEX.PINKY_INDEX()]
        }
        us_finger_feats = {
            'thumb': [us_feature[i] for i in FINGER_INDEX.THUMB_INDEX()],
            'index': [us_feature[i] for i in FINGER_INDEX.INDEX_INDEX()],
            'middle': [us_feature[i] for i in FINGER_INDEX.MIDDLE_INDEX()],
            'ring': [us_feature[i] for i in FINGER_INDEX.RING_INDEX()],
            'pinky': [us_feature[i] for i in FINGER_INDEX.PINKY_INDEX()]
        }

        for k in st_finger_feats:
            st_finger_feats[k] = np.array(st_finger_feats[k])
        for k in us_finger_feats:
            us_finger_feats[k] = np.array(us_finger_feats[k])
        sz = len(fastdtw(st_feature.T, us_feature.T)[1])
        dists = {
            # 'total': fastdtw(st_feature.T, us_feature.T)[0] / sz,
            'thumb': fastdtw(st_finger_feats['thumb'].T, us_finger_feats['thumb'].T)[0] / sz,
            'index': fastdtw(st_finger_feats['index'].T, us_finger_feats['index'].T)[0] / sz,
            'middle': fastdtw(st_finger_feats['middle'].T, us_finger_feats['middle'].T)[0] / sz,
            'ring': fastdtw(st_finger_feats['ring'].T, us_finger_feats['ring'].T)[0] / sz,
            'pinky': fastdtw(st_finger_feats['pinky'].T, us_finger_feats['pinky'].T)[0] / sz,
        }
        dists['total'] = sum(dists.values()) / 5
        for k in dists:
            dists[k] = 100 - dists[k]
            if dists[k] < 0:
                dists[k] = 0
        return dists

    def set_dist(self, dists):
        self.totalDistLable.setText(str(int(dists['total'])))
        self.thumbDistLable.setText(str(int(dists['thumb'])))
        self.indexDistLable.setText(str(int(dists['index'])))
        self.middleDistLable.setText(str(int(dists['middle'])))
        self.ringDistLable.setText(str(int(dists['ring'])))
        self.pinkyDistLable.setText(str(int(dists['pinky'])))

    def set_tips(self, dists):
        dist_too_large = set()
        for k in dists:
            if k == 'total':
                continue
            if dists[k] <= 90:
                dist_too_large.add(k)

        if len(dist_too_large) > 2:
            self.tipLabel.setText(
                'Gesture has too large difference from the standard, maybe try once again?')

        elif len(dist_too_large) > 1:
            fingers = ', '.join(dist_too_large)
            self.tipLabel.setText(
                'Fingers {} have difference from the standard. Please pay more attention on these fingers!'.format(fingers))
        elif len(dist_too_large) == 1:
            finger = dist_too_large.pop()
            self.tipLabel.setText(
                'Finger {} has a large difference from the standard. Pay more attention on this finger!'.format(finger))
        else:
            self.tipLabel.setText(
                'Brillient! Your gesture is quite close to the standard gesture!')

    # def set_table(self, dists):
    #     for k in TABLE_INDEX:
    #         print(TABLE_INDEX[k])
    #         item = QTableWidgetItem(text=str(dists[k]))
    #         self.distanceTable.setItem(TABLE_INDEX[k], 1, item)
    #         # .setText(str(dists[k]))


if __name__ == '__main__':
    import numpy as np
    import sys
    b1 = np.load('dataset/c-1.npy')
    b2 = np.load('dataset/c-2.npy')
    app = QApplication([])
    window = ResultDialog(b1, b2)
    window.show()
    sys.exit(app.exec_())
    # pass
