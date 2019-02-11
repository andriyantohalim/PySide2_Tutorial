##################################################
#  TUTORIAL 1_5. Message Box
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Message Box")
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
