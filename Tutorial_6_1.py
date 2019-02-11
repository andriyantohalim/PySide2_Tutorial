##################################################
#  TUTORIAL 6_1. Checkbox
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox
from PySide2.QtCore import Qt


class Example(QWidget):

    def initUI(self):
        checkbox = QCheckBox("Show Title", self)
        checkbox.move(20, 20)
        checkbox.toggle()
        checkbox.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("Checked")
        else:
            self.setWindowTitle("Unchecked")

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
