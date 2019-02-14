import sys
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow):

    def initUI(self, ui_file):
        uifile = QtCore.QFile(ui_file)
        # uifile.open(QtCore.QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(uifile)
        # uifile.close()

        self.window.calc_tax_button.clicked.connect(self.CalculateTax)
        self.window.setWindowTitle("Halim")
        self.window.show()

    def CalculateTax(self):
        price = int(self.window.price_box.toPlainText())
        tax = (self.window.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.window.result_window.setText(total_price_string)

    def __init__(self, ui_file):
        super(MyApp, self).__init__()
        self.initUI(ui_file)


def main():
    app = QtWidgets.QApplication(sys.argv)
    myappl = MyApp("Tax_Calc.ui")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
