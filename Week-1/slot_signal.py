import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DemoSignalSlot(QWidget):
    """
    Demo Signal Slot
    """

    def __init__(self, parent=None):
        super(DemoSignalSlot, self).__init__(parent)

        self.setMinimumSize(800, 600)

        progress = QProgressBar()
        progress.setValue(50)

        slider = QSlider(QtCore.Qt.Horizontal)
        vbox = QVBoxLayout(self)
        vbox.addWidget(progress)
        vbox.addWidget(slider)

        # Cach 1
        slider.valueChanged.connect(lambda: progress.setValue(slider.value()))

        # Cach 2: but process need intialize with self.process
        # slider.valueChanged.connect(lambda : self.changeProgress(slider.value()))

        self.show()

    def changeProgress(self, value):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signal_slot = DemoSignalSlot()
    sys.exit(app.exec_())
