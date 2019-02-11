##################################################
#  TUTORIAL 4_2. Reimplementing Event Handler
##################################################

import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel
from PySide2 import QtCore


class Example(QWidget):

    def initUI(self):
        label = QLabel("Press ESC to Quit", self)
        label.move(15,10)

        self.setToolTip("Press ESC to quit")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
