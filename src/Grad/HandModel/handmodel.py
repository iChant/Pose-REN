from PySide2.QtDataVisualization import QtDataVisualization
from PySide2.QtGui import QVector3D

if __name__ == '__main__':
    import sys
    import numpy as np
    from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget


class FINGER_INDEX:
    WRIST = 0
    THUMB_ROOT = 1
    THUMB_ROOT_MIDDLE = 6
    THUMB_MIDDLE_TIP = 7
    THUMB_TIP = 8
    INDEX_ROOT = 2
    INDEX_ROOT_MIDDLE = 9
    INDEX_MIDDLE_TIP = 10
    INDEX_TIP = 11
    MIDDLE_ROOT = 3
    MIDDLE_ROOT_MIDDLE = 12
    MIDDLE_MIDDLE_TIP = 12
    MIDDLE_TIP = 14
    RING_ROOT = 4
    RING_ROOT_MIDDLE = 15
    RING_MIDDLE_TIP = 16
    RING_TIP = 17
    PINKY_ROOT = 5
    PINKY_ROOT_MIDDLE = 18
    PINKY_MIDDLE_TIP = 19
    PINKY_TIP = 20

    # @property
    @classmethod
    def THUMB_INDEX(cls):
        return cls.THUMB_ROOT, cls.THUMB_ROOT_MIDDLE, cls.THUMB_MIDDLE_TIP, cls.THUMB_TIP

    # @property
    @classmethod
    def INDEX_INDEX(cls):
        return cls.INDEX_ROOT, cls.INDEX_ROOT_MIDDLE, cls.INDEX_MIDDLE_TIP, cls.INDEX_TIP

    # @property
    @classmethod
    def MIDDLE_INDEX(cls):
        return cls.MIDDLE_ROOT, cls.MIDDLE_ROOT_MIDDLE, cls.MIDDLE_MIDDLE_TIP, cls.MIDDLE_TIP

    # @property
    @classmethod
    def RING_INDEX(cls):
        return cls.RING_ROOT, cls.RING_ROOT_MIDDLE, cls.RING_MIDDLE_TIP, cls.RING_TIP

    # @property
    @classmethod
    def PINKY_INDEX(cls):
        return cls.PINKY_ROOT, cls.PINKY_ROOT_MIDDLE, cls.PINKY_MIDDLE_TIP, cls.PINKY_TIP


class HandModel:
    def __init__(self, data=None):
        self.scatter_graph = QtDataVisualization.Q3DScatter()
        self.scatter_graph.activeTheme().setType(
            QtDataVisualization.Q3DTheme.ThemeEbony)
        self.scatter_graph.setShadowQuality(
            QtDataVisualization.QAbstract3DGraph.ShadowQualitySoftHigh)
        self.scatter_graph.scene().activeCamera().setCameraPreset(
            QtDataVisualization.Q3DCamera.CameraPresetNone)
        # self.scatter_graph.scene().activeCamera().setXRotation(180)
        # self.scatter_graph.scene().activeCamera().setYRotation(100)
        self.proxy = QtDataVisualization.QScatterDataProxy()
        self.series = QtDataVisualization.QScatter3DSeries(self.proxy)
        self.series.setItemLabelFormat(
            '@xTitle: @xLabel @yTitle: @yLabel @zTitle: @zLabel')
        self.series.setMeshSmooth(True)
        self.scatter_graph.addSeries(self.series)
        self.scatter_graph.axisX().setTitle('X')
        self.scatter_graph.axisY().setTitle('Y')
        self.scatter_graph.axisZ().setTitle('Z')
        self.scatter_graph.axisX().setReversed(True)
        self.scatter_graph.axisY().setReversed(True)
        self.scatter_graph.axisZ().setReversed(True)
        if data is not None:
            self.refresh(data)
        # self.test()

    def refresh(self, pose, color=None):
        # self.scatter_graph.seriesList()[0].dataProxy()
        count = self.proxy.itemCount()
        if count == 0:
            for p in pose:
                item = QtDataVisualization.QScatterDataItem()
                item.setPosition(QVector3D(*p))
                self.scatter_graph.seriesList()[0].dataProxy().addItem(item)
        else:
            index = 0
            for p in pose:
                item = QtDataVisualization.QScatterDataItem()
                item.setPosition(QVector3D(*p))
                self.scatter_graph.seriesList(
                )[0].dataProxy().setItem(index, item)
                index += 1
        # data_array = []
        # for p in pose:
        #     item = QtDataVisualization.QScatterDataItem()
        #     item.setPosition(QVector3D(*p))
        #     data_array.append(item)
        # self.scatter_graph.seriesList()[0].dataProxy().resetArray(data_array)

    def test(self):
        pose = np.array([[259.36813, 234.74612, 620.96576],
                         [269.89847, 197.45969, 607.99384],
                         [274.0073, 179.50319, 602.55896],
                         [276.91644, 165.90048, 598.4678],
                         [279.47473, 153.22821, 593.83624],
                         [257.6054, 192.82268, 604.02454],
                         [257.55304, 173.03976, 596.3222],
                         [257.80832, 161.16463, 593.77875],
                         [258.62637, 150.1128, 592.20966],
                         [246.32387, 192.95654, 601.9747],
                         [242.55571, 177.95456, 591.7625],
                         [239.87152, 167.9041, 586.59357],
                         [237.50287, 157.02663, 582.63715],
                         [232.94322, 199.07051, 597.001],
                         [226.309, 187.66035, 592.5064],
                         [221.27753, 180.27943, 589.84106],
                         [215.51993, 172.23232, 586.6943],
                         [272.7272, 227.59906, 613.0349],
                         [285.7954, 217.38445, 608.2296],
                         [296.74142, 207.88226, 603.6965],
                         [308.86798, 198.94102, 599.0626]])
        self.refresh(pose)


if __name__ == '__main__':
    class MainWindow(QWidget):
        """
        for test
        """

        def __init__(self):
            QWidget.__init__(self)
            self.resize(1440, 900)
            # 设置主窗口标题
            self.setWindowTitle('Test')
            self.layout = QGridLayout()
            self.handgraph = HandModel()
            self.container = QWidget.createWindowContainer(
                self.handgraph.scatter_graph)
            self.layout.addWidget(self.container)
            self.btn = QPushButton('sss')
            self.layout.addWidget(self.btn)
            self.setLayout(self.layout)
            self.handgraph.test()
            pass


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
