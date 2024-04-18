import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okbtn = QPushButton('Ok')
        cancelbtn = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(1080, 540, 400, 350)
        self.setWindowTitle('Layout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
