##################################################
#  TUTORIAL 2_5. ToolBar + SubMenu
##################################################

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit


class Example(QMainWindow):

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        newAction = QAction('New', self)
        exitAction = QAction('Exit', self)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newAction)
        # fileMenu.addAction(exitAction)    # Added in the toolbar.addAction() below. Somewhat can't duplicate

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    def __init__(self):
        super().__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()