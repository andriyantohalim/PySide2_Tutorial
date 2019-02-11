##################################################
#  TUTORIAL 2_3. Toolbar
# @TODO: No Icon displayed, maybe on Mac OS only
##################################################

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QAction
from PySide2.QtGui import QIcon


class Example(QMainWindow):

    def initUI(self):
        # exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction = QAction('Exit', self)

        exitAction.setShortcut('Ctrl+Q') # CMD + Q in Mac OS
        exitAction.triggered.connect(self.close)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toolbar')
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
