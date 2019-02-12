##################################################
#  TUTORIAL 8_2. Drag & Drop a Button Widget
# @TODO: Drag and drop is not working.
##################################################

import sys
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtGui import QMouseEvent, QDrag
from PySide2.QtCore import Qt, QMimeData


class Button(QPushButton):

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(Qt.MoveAction)

    def mousePressEvent(self, e: PySide2.QtGui.QMouseEvent):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print("Press")

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)


class Example(QWidget):

    def initUI(self):
        self.setAcceptDrops(True)
        self.btn = Button("Button", self)
        self.btn.move(100, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Click or Move')
        self.show()

    def dragEnterEvent(self, event:PySide2.QtGui.QDragEnterEvent):
        event.accept()

    def dropEvent(self, event:PySide2.QtGui.QDropEvent):
        position = event.pos()
        self.btn.move(position)

        event.setDropAction(Qt.MoveAction)
        event.accept()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
