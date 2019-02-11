##################################################
#  TUTORIAL 7_2. QLineEdit (display image)
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class Example(QWidget):

    def initUI(self):
        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()   # This is needed to update the label as the textedit got updated

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
