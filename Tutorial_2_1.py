##################################################
#  TUTORIAL 2_1. Status Bar
##################################################

import sys
from PySide2.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Status Bar")
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
    

