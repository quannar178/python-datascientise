# Tạo 1 ứng dụng GUI đơn giản bằng PyQT hoặc tkinter.
# Phần mềm thay vì nhận 2 tham số thì dùng GUI để chọn ảnh và vị trí lưu ảnh.
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidgets):
    def __init__(self, parent = None):



def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()