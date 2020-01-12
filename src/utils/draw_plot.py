from matplotlib import pyplot as plt
import numpy as np


class Plotter():

    def __init__(self, tdist, tpath, dists, paths, test_feats, model_feats, label, handmodel='hand.npy'):
        self.tdist = tdist
        self.tpath = np.array(tpath)
        self.dists = np.array(dists)
        self.paths = paths
        self.test_feats = test_feats
        self.model_feats = model_feats
        hand = np.load(handmodel)
        self.hand = hand[:, 0:2]
        self.label = label
        self.cid = None

    def show_hand_nodetail(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(self.hand[:, 0], self.hand[:, 1])
        ax.xaxis.set_ticks_position('top')
        ax.invert_yaxis()
        ax.set_title('No match presets')
        # plt.show()

    def show_hand(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(self.hand[:, 0], self.hand[:, 1])
        ax.xaxis.set_ticks_position('top')
        ax.invert_yaxis()
        self.cid = fig.canvas.mpl_connect(
            'button_press_event', self.on_hand_click)
        # plt.show()

    def show_total_features(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(self.tpath[:, 0], self.tpath[:, 1])
        ax.set_title('Compared with {}, Distance: {}'.format(
            self.label, self.tdist))
        # plt.show()

    def on_hand_click(self, event):
        closest_point = self.get_closest_point(event.xdata, event.ydata)
        if closest_point is not None:
            self.show_point_detail(closest_point)

    def get_closest_point(self, x, y, e=2):
        _dist = np.array([self.hand[:, 0] - x, self.hand[:, 1] - y]).T
        _dist = np.linalg.norm(_dist, axis=1)
        res = _dist.argmin()
        print('index: ', res)
        return res if _dist[res] < e else None

    def show_point_detail(self, idx):
        tfeat = self.test_feats[idx]
        mfeat = self.model_feats[idx]
        dist = self.dists[idx]
        path = np.array(self.paths[idx])
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        ax1.scatter(path[:, 0], path[:, 1])
        ax1.set_title('Distance: {}'.format(dist))
        ax2 = fig.add_subplot(122)
        ax2.plot(np.arange(tfeat.shape[0]), tfeat)
        ax2.plot(np.arange(mfeat.shape[0]), mfeat, 'r--')
        plt.show()
