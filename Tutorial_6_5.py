##################################################
#  TUTORIAL 6_5. Calendar Widget
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel,  QCalendarWidget
from PySide2.QtCore import QDate


class Example(QWidget):

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('QProgressBar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
