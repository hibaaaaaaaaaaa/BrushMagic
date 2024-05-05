# This is a sample Python script.
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore, QtGui
from PySide6.QtGui import QFontDatabase
import sys
import TestXX as T
import TestXX1 as T1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Check available fonts on your system
    app = QApplication(sys.argv)

    widget1 = T.StartingPage()
    #widget2 = T1.MenuPage()
    widget1.show()
    sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
