# Tạo 1 ứng dụng GUI đơn giản bằng PyQT hoặc tkinter.
# Phần mềm thay vì nhận 2 tham số thì dùng GUI để chọn ảnh và vị trí lưu ảnh.

import sys
import os
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)

        btnChoose = QPushButton("Choose Button")
        btnChoose.clicked.connect(self.getImg)
        # btnChoose.setShortcut("Ctr+O")

        btnSave = QPushButton("Save Button")
        btnSave.clicked.connect(self.saveImg)
        # btnSave.setShortcut("Ctrl+S")

        btnConvert = QPushButton("Conver Image")
        btnConvert.clicked.connect(self.showConvert)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnConvert)
        hbox.addWidget(btnChoose)
        hbox.addWidget(btnSave)

        self.label = QLabel("Image")
        self.label.setFixedSize(800, 600)
        self.label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')

    def getImg(self):
        self.img, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                  None, "Image files (*.jpg *.gif *png)")
                                                
        if self.img and os.path.exists(self.img):
            pixmap = QPixmap(self.img)
            print(pixmap.width())
            print(pixmap.height())
            pixmap.scaled(800, 600)
            self.label.setPixmap(pixmap)

    def saveImg(self):
        img_black_white = self.convertImg()
        print(img_black_white)
        if(hasattr(self, "img") and self.img != ""):
            # Lưu ảnh
            pathSave, _ = QFileDialog.getSaveFileName(self, "Save image", None, "Image files (*.jpg *.gif *png)" )
            print("pathSave", pathSave)
            if pathSave and os.path.exists(pathSave):
                cv2.imwrite(pathSave, img_black_white)
            else:
                self.label.setText("")

        else:
            self.label.setText(
                "<b style=\"color: red;\">Please choose image</b>")
    def showConvert(self):
        pass
    def convertImg(self):
        if(hasattr(self, "img") and self.img != ""):
            img = cv2.imread(self.img)
            heights, widths, channels = img.shape  # if read gray
            # Giảm kích thước ảnh còn 1 nửa
            heights //= 2
            widths //= 2
            img_resize = cv2.resize(img, (widths, heights))
            # Xoay ảnh ngược chiều kim đồng hồ
            img_rotate = cv2.rotate(img_resize, cv2.ROTATE_90_COUNTERCLOCKWISE)
            # cv2.imshow("Rotate", img_rotate)

            # Chuyển ảnh sang sạng gray
            img_gray = cv2.cvtColor(img_rotate, cv2.COLOR_BGR2GRAY)

            # Chuyển ảnh dạng đen trắng
            (thresh, img_black_white) = cv2.threshold(
                img_gray, 127, 255, cv2.THRESH_BINARY)
            return img_black_white
        else:
            return None



def main():
    app = QApplication(sys.argv)
    myWindow = window()
    myWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
