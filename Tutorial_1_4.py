##################################################
#  TUTORIAL 1_4. Close Window
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import QCoreApplication


class Example(QWidget):

    def initUI(self):
        qbtn = QPushButton("Quit", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Quit Button")
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

