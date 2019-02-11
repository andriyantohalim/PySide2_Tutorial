##################################################
#  TUTORIAL 3_1. Absolute Positioning
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):
    def initUI(self):
        label1 = QLabel("Halim", self)
        label1.move(15, 10)

        label2 = QLabel("PySide2 Tutorials", self)
        label2.move(35, 40)

        label3 = QLabel("for Qt GUI", self)
        label3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolute")
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