from PySide6.QtGui import QFont, QFontDatabase, QColor, QPen, QPainter, QBrush, QPainterPath, QTextOption, \
    QTextCharFormat, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect, QWidget, QVBoxLayout, QTextEdit, \
    QPushButton
from PySide6.QtCore import Qt
from TestXX1 import MenuPage
class StartingPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 590)  # Set the fixed size of the window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(800, 50)




        # Create a QLabel for the background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 300, 590)
        self.background_label.setStyleSheet("border: none;"
                                            "border-top-left-radius: 32px;"
                                            "border-top-right-radius: 32px;"
                                            "border-bottom-left-radius: 32px;"
                                            "border-bottom-right-radius: 32px;"
                                            "background-image: url('Back2.jpg');"
                                            "background-position: left;"
                                            "background-repeat: no-repeat;"
                                            )
        self.text_label1 = QLabel(self)
        self.text_label2 = QLabel(self)
        self.text_label1.setGeometry(30, 23, 263, 126)
        self.text_label2.setGeometry(35, 88, 263, 126)
        id=QFontDatabase.addApplicationFont("Gempita.ttf")

        families=QFontDatabase.applicationFontFamilies(id)

        font1 = QFont(families[0], 110,QFont.Bold)  # Specify the font and size
        self.text_label1.setFont(font1)
        self.text_label1.setStyleSheet("color: white;")  # Optionally set text color
        self.text_label1.setText("Brush ")

        font2 = QFont(families[0], 60,QFont.Bold)  # Specify the font and size
        self.text_label2.setFont(font2)
        self.text_label2.setStyleSheet("color: white;")  # Optionally set text color
        self.text_label2.setText("Magic")

        self.bottom_label = BlurLabelWidget(self)
        self.bottom_label.setGeometry(17, 390, 265, 170)#390


        id1 = QFontDatabase.addApplicationFont("PRO.otf")
        families1 = QFontDatabase.applicationFontFamilies(id1)
        font3 = QFont(families1[0], 10)
        self.text_label3 = QLabel(self)
        self.text_label3.setFont(font3)
        self.text_label3.setStyleSheet("color: white;")  # Optionally set text color
        self.text_label3.setText("Explore and Mint BrushMagic ")
        self.text_label3.setGeometry(52, 360, 230, 150)

        id2 = QFontDatabase.addApplicationFont("GlacialIndifference.otf")
        families2 = QFontDatabase.applicationFontFamilies(id2)
        font3 = QFont(families2[0], 10)  # Specify the font and size, make it bold
        self.text_label4 = QLabel(self)
        self.text_label4.setFont(font3)
        self.text_label4.setStyleSheet("color: #EBEBF5;")  # Set text color to light gray
        self.text_label4.setText("Enhance your images and unleash the \n          potential  of your photos.\n                   ")
        self.text_label4.setGeometry(43, 370, 210,200)

        id3 = QFontDatabase.addApplicationFont("Semi.ttf")
        families3 = QFontDatabase.applicationFontFamilies(id3)

        self.button = QPushButton("Get started now", self)
       # self.button.setGeometry(65, 500, 170, 37)  # Adjusted position to be at the bottom of the window
        self.button.setGeometry(50, 500, 200, 37)
        self.button.setAutoDefault(False)
        self.button.setStyleSheet("background-color: rgba(185, 149, 200, 250);"  # Background color with transparency
                                  "border-radius: 10px;"  # Rounded corner radius
                                  "border: 2px solid rgba(185, 149, 200, 150);"  
                                  #"font-family: 'SF Pro Text';"
                                 "font-family: 'Glacial Indifference';"  # Change font family
                                  "font-size: 10pt;"  # Change font size
                                   # Stroke with 50% opacity
                                 # "font-weight: bold;"
                                  "color: #FFFFFF;"
                                  )  # Text color

        self.button.setCursor(Qt.PointingHandCursor)
       # self.button.clicked.connect(self.clickme)
        self.button.clicked.connect(self.goToMenuPage)


    def goToMenuPage(self):
        # printing pressed
        self.menu_page = MenuPage()
        self.menu_page.show()
        self.hide()



class BlurLabelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(265, 170)

        # Apply blur effect to the widget
        blur_effect = QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(40)
        self.setGraphicsEffect(blur_effect)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(0, 0, 265, 170, 30, 30)
        #(185, 149, 200, 150)
        # Fill the rounded rectangle with a transparent blue color
       #brush = QBrush(QColor(152, 214, 227, 150))  # Transparent blue color
       # brush=QBrush(QColor(185, 149, 200, 150))
        brush = QBrush(QColor(152, 214, 227, 200))

        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        # Draw the stroke around the rounded rectangle
        pen = QPen(QColor(255, 255, 255, 77), 5, Qt.SolidLine)  # White color with 30% opacity
        painter.setPen(pen)
        painter.drawPath(path)

class BlurLabelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(265, 170)

        # Apply blur effect to the widget
        blur_effect = QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(40)
        self.setGraphicsEffect(blur_effect)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(0, 0, 265, 170, 30, 30)
        #(185, 149, 200, 150)
        # Fill the rounded rectangle with a transparent blue color
       #brush = QBrush(QColor(152, 214, 227, 150))  # Transparent blue color
       # brush=QBrush(QColor(185, 149, 200, 150))
        brush = QBrush(QColor(152, 214, 227, 200))

        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        # Draw the stroke around the rounded rectangle
        pen = QPen(QColor(255, 255, 255, 77), 5, Qt.SolidLine)  # White color with 30% opacity
        painter.setPen(pen)
        painter.drawPath(path)

