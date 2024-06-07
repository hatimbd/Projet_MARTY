import sys
from PyQt6.QtWidgets import QApplication
from class_marty_cntrl_app import MartyControlApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControlApp()
    ex.show()
    sys.exit(app.exec())