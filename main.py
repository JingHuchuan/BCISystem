import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from controller.mainWindowControl import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QIcon('src/image/Brain.png'))
    window.setWindowTitle("BCISystem")
    window.show()
    app.exec_()
