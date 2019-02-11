##################################################
#  TUTORIAL 5_4. File Dialog
##################################################

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class Example(QMainWindow):

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        # openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile = QAction('Open', self)

        openFile.setShortcut('Ctrl+O')

        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/')
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()