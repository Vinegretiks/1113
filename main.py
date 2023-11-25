import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 700)
        self.setWindowTitle('Задание 3')
        self.btn = QPushButton('Создать круг', self)
        self.btn.move(190, 580)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        x = randrange(1, 200)
        y = randrange(1, 200)
        wh = randrange(1, 200)
        qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        qp.drawEllipse(x, y, wh, wh)

def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())