
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        self.label.setPixmap(QPixmap(600, 600))
    def circle(self):

