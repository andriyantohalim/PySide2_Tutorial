##################################################
#  TUTORIAL 4_3. Event Sender
#@TODO: callback function effect only once.
##################################################

import sys
from PySide2.QtWidgets import QApplication, QPushButton, QMainWindow


class Example(QMainWindow):

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        # self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def release(self):
        sender = self.sender()
        # self.statusBar().showMessage(sender.text() + ' was pressed')
        self.statusBar().showMessage("Ready")

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
