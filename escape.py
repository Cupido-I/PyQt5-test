from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Event object')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Alt:
            self.setWindowTitle('Alt pressed')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Exp()
    ex.show()
    sys.exit(app.exec_())
