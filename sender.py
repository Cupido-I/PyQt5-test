from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Exp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1080, 540, 400, 350)
        self.setWindowTitle('Sender')

        btn1 = QPushButton('Hello', self)
        btn2 = QPushButton('World', self)

        btn1.move(150, 100)
        btn2.move(150, 200)

        self.statusBar()

        btn1.clicked.connect(self.btnclicked)
        btn2.clicked.connect(self.btnclicked)

    def btnclicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was clicked!')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())
