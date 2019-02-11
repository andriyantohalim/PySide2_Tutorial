##################################################
#  TUTORIAL 4_1. Signal & Slot
##################################################

import sys
from PySide2.QtWidgets import QLCDNumber, QSlider, QVBoxLayout, QWidget, QApplication, QMainWindow
from PySide2 import QtCore


class Example(QWidget):

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(QtCore.Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
