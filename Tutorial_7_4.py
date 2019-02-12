##################################################
#  TUTORIAL 7_4. QComboBox
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class Example(QWidget):

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        self.lbl.move(50, 150)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mac OS")
        combo.addItem("Windows")
        combo.addItem("Red Hat")
        combo.addItem("Fedora")

        combo.move(50, 50)
        combo.setGeometry(50, 50, 100, 100)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
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
