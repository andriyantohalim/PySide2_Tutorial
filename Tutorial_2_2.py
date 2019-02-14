##################################################
#  TUTORIAL 2_2. Menu Bar
# @TODO: No Icon displayed, maybe on Mac OS only
##################################################

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QAction


class Example(QMainWindow):

    def initUI(self):
        # exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('MenuBar')
        self.statusBar().showMessage("Ready")
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
