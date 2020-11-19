import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Splash screen
from ui_splash_screen import Ui_SplashScreen
from ui_main_screen import Ui_MainWindow
# Global
counter = 0


class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QTimer.singleShot(1000, lambda : self.ui.label.setText("<strong>HELLO</strong> MY APP"))
        QtCore.QTimer.singleShot(1000, lambda : self.setStyleSheet("background-color: #222; color: #FFF"))


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.DropShadowFrame.setGraphicsEffect(self.shadow)

        # QTimer => START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        
        # Timer in milisecond
        self.timer.start(45)

        # init description
        self.ui.label_description.setText("<strong>WELLCOME</strong> TO MY APPLICATION")
        # Change desctiotion
        QtCore.QTimer.singleShot(1500, lambda : self.ui.label_description.setText("<strong>LOADDING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda : self.ui.label_description.setText("<strong>LOADDING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global counter

        # set value to progress bar
        self.ui.progressBar.setValue(counter)

        # Close splash screend adn open main screen
        if counter > 100:
            # Stop timer
            self.timer.stop()

            # show main window
            self.main = MainScreen()
            self.main.show()

            # Close splash window
            self.close()

        # Increment counter

        counter += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

