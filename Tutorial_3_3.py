##################################################
#  TUTORIAL 3_3. Grid Layout
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel


class Example(QWidget):
    def initUI(self):
        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        grid = QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3),
                (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QPushButton(i)
            if j == 2:
                grid.addWidget(QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        self.setLayout(grid)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
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
