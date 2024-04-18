import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit


class Exp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setGeometry(1080, 540, 400, 350)
        self.setLayout(grid)

        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
