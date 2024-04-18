from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Exp(QMainWindow):

    """docstring for ex"""

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(1080, 540, 400, 350)
        self.setWindowTitle('Emitting Signal')

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

    def mousePressEvent(self, event):

        self.c.closeApp.emit()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())
