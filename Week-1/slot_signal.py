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
        progress.setValue(0)

        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setValue(0)

        label = QLabel()
        label.setText(str(0))
        vbox = QVBoxLayout(self)
        vbox.addWidget(progress)
        vbox.addWidget(slider)
        vbox.addWidget(label, 0, QtCore.Qt.AlignCenter)



        # Cach 1
        slider.valueChanged.connect(lambda: progress.setValue(slider.value()))
        slider.valueChanged.connect(lambda: label.setText(str(slider.value())))

        # Cach 2: but process need intialize with self.process
        # slider.valueChanged.connect(lambda : self.changeProgress(slider.value()))

        self.setLayout(vbox)
        self.show()

    def changeProgress(self, value):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signal_slot = DemoSignalSlot()
    sys.exit(app.exec_())
