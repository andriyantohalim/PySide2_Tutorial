##################################################
#  TUTORIAL 4_4. Emitting signals
#@TODO: still unsure how this works. to figure out more
##################################################

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QObject, Signal


class Communicate(QObject):
    closeApp = Signal()


class Example(QMainWindow):

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
