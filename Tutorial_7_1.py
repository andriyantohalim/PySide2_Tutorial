##################################################
#  TUTORIAL 7_1. QPixMap (display image)
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap


class Example(QWidget):

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("Tutorial_7_1.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(Qt.AlignCenter)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Red Rock')
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
