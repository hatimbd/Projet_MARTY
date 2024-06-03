import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from martypy import Marty, MartyConfigException
import threading
from class_MartyControlApp import MartyControlApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControlApp()
    ex.show()
    sys.exit(app.exec())
