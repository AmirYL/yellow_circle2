import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 546, 607)
        self.label = QLabel(self)
        self.label.setGeometry(20, 10, 501, 501)
        self.pushButton = QPushButton("Нажми!", self)
        self.pushButton.move(220, 520)
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(500, 500)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = [randint(10, 400) for i in range(2)]
        a = randint(10, 80)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(x, y, a, a)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
