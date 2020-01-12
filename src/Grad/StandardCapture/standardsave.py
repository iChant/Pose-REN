from src.Grad.StandardCapture.ui_standardsavedialog import Ui_Dialog

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog
import os
# import numpy as np


DATASET_DIR = 'dataset'


class SaveDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SaveDialog, self).__init__(parent=parent)
        self.setupUi(self)
        # self.buttonBox.accepted()
        # self.save_selected = Signal(str)
        # self.cancel_selected = Signal()

    def get_savepath(self):
        count = 1
        typename = self.lineEdit.text()
        for name in os.listdir(DATASET_DIR):
            t = name.split('-')[0]
            if t == typename:
                count += 1

        print(DATASET_DIR, typename + '-' + str(count))
        return os.path.join(DATASET_DIR, typename + '-' + str(count))
        # self.save_selected.emit(os.path.join(
        #     DATASET_DIR, typename + '-' + str(count)))
        # np.save()

    # def cancel(self):
    #     self.cancel_selected.emit()


# class SaveDialog(QDialog, Ui_Dialog):
#     def __init__(self, parent=None, f=Default(Qt.WindowFlags)):
#         super().__init__(parent=parent, f=f)
