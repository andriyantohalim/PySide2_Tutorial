##################################################
#  TUTORIAL 8_1. Simple Drag and Drop
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel


class Button(QPushButton):

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)


class Example(QWidget):

    def initUI(self):
        lbl = QLabel("1. Type some string on the QLineEdit\n2. Drag & Drop the string on to the button", self)
        lbl.setGeometry(35, 1, 300, 100)

        qe = QLineEdit('', self)
        qe.setDragEnabled(True)
        qe.move(30, 80)

        button = Button("Button", self)
        button.move(190, 80)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Simple Drag and Drop')
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
