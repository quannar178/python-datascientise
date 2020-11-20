import sys
import time

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

        self.progress = QProgressBar()
        self.progress.setValue(0)
        button = QPushButton("Start")
        button.setFixedSize(200, 60)
    
        slider = QSlider()
        lcd = QLCDNumber()

        hbox = QHBoxLayout()
        hbox.addWidget(slider)
        hbox.addWidget(lcd)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.progress)
        vbox.addWidget(button, 0, QtCore.Qt.AlignCenter)
        vbox.addLayout(hbox)

        # Slot Signal slider and lcd
        slider.valueChanged.connect(lambda: lcd.display(slider.value()))

        self.setLayout(vbox)

        # Cach 1
        button.clicked.connect(self.event_button_clicked)

        self.show()

    def event_button_clicked(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.event_woker_finished)
        self.worker.update_process.connect(self.updata_progress)

    def event_woker_finished(self):
        QMessageBox.information(self, "Process done", "Worker thread finished")

    def updata_progress(self, value):
        self.progress.setValue(value)


class WorkerThread(QThread):
    update_process = pyqtSignal(int)

    def run(self):
        for x in range(20, 101, 10):
            print(x)
            time.sleep(0.5)
            self.update_process.emit(x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signal_slot = DemoSignalSlot()
    sys.exit(app.exec_())
