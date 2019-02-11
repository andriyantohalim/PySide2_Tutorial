##################################################
#  TUTORIAL 1_3. Tooltip
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PySide2 import QtGui


class Example(QWidget):

    def initUI(self):
        QToolTip.setFont(QtGui.QFont('SansSerif', 12))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Tooltips")
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


