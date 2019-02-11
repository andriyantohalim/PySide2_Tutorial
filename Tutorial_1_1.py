##################################################
#  TUTORIAL 1_1. Simple GUI
##################################################

import sys
from PySide2.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    wid = QWidget()
    wid.resize(300, 300)
    wid.setWindowTitle("Simple")
    wid.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



