import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, qApp, QAction, QMainWindow, QTextEdit
from PyQt5.QtGui import QCloseEvent, QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Exp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()

        exitAction = QAction(QIcon('donut.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exitoo')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b>')
        btn = QPushButton('Push', self)
        btn.setToolTip('Press and Push')
        btn.resize(btn.sizeHint())
        btn.move(150, 150)

        qtn = QPushButton('Quit', self)
        qtn.resize(qtn.sizeHint())
        qtn.clicked.connect(QCoreApplication.instance().quit)
        qtn.move(150, 200)

        self.setGeometry(1080, 540, 400, 350)
        self.setWindowTitle('MyWindow')
        self.setWindowIcon(QIcon('donut.png'))

        self.show()

    def closeEvent(self, a0: QCloseEvent) -> None:
        reply = QMessageBox.question(self, 'Message', "You sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()
        # return super().closeEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
