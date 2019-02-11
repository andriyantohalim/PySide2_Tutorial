##################################################
#  TUTORIAL 1_2. Window Icon
# @TODO: No Icon displayed, maybe on Mac OS only
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2 import QtGui


class Example(QWidget):

    def initUI(self):
        self.setWindowTitle("Icon")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QtGui.QIcon('web.png'))
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