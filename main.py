import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, qApp, QAction
from PyQt5.QtGui import QIcon


class Exp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('donut.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.statusBar()

        tbar = self.addToolBar('Exit')
        tbar.addAction(exitAct)

        self.setGeometry(1080, 540, 400, 350)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
