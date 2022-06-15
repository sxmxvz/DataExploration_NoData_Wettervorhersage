from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    App = Main()
    sys.exit(app.exec_())

uic.loadUi("app/ui/Main.ui", self)
self.show()