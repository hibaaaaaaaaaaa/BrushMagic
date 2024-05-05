from PySide6.QtGui import QFont, QFontDatabase, QColor, QPen, QPainter, QBrush, QPainterPath, QTextOption, \
    QTextCharFormat, QTextCursor, QIcon, QPalette, QAction, QImageReader, QBitmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect, QWidget, QVBoxLayout, QTextEdit, \
    QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QDialog, QFrame, QGraphicsOpacityEffect, QSlider, QFileDialog
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import *
from PySide6.QtSvg import *
from PIL import Image
from Filters import *


class GalleryPage(QMainWindow):
    def __init__(self, file_path):
        super().__init__()
        self.filter = None

        self.setFixedSize(300, 590)  # Set the fixed size of the window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(800, 50)

        panel = QWidget()
        panel.setStyleSheet("background-color:white;border-radius:32px")

        image = Image.open(file_path)
        resized_image = image.resize((293, 440))

        # Enregistrer l'image redimensionnée
        self.natural_image = "resized_image.jpg"
        self.filtred_image = "filtred_image.jpg"

        resized_image.save(self.natural_image)

        self.main_label1 = QLabel(panel)
        self.main_label1.setFixedSize(293, 440)
        self.main_label1.setGeometry(3, 3, 293, 440)
        self.main_label1.setStyleSheet(f"""
                                border-radius: 32px;
                                border: 1px solid rgba(255, 255, 255, 150);
                                background-image: url('{self.natural_image}');
                          """)

        self.icon_label = QLabel(panel)
        self.icon_label.setGeometry(260, 25, 16, 16)
        pixmap = QPixmap("down4.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label.setPixmap(pixmap)
        self.icon_label.setStyleSheet("background-color: transparent;");
        # self.setCentralWidget(panel)

        self.icon_label2 = QLabel(panel)
        self.icon_label2.setGeometry(15, 382, 24, 24)
        pixmap2 = QPixmap("click24.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label2.setPixmap(pixmap2)
        self.icon_label2.setStyleSheet("background-color: transparent;");

        self.icon_label3 = QLabel(panel)
        self.icon_label3.setGeometry(260, 382, 24, 24)
        pixmap3 = QPixmap("para.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label3.setPixmap(pixmap3)
        self.icon_label3.setStyleSheet("background-color: transparent;");

        self.label2 = QLabel(panel)
        self.label2.setFixedSize(293, 170)
        self.label2.setGeometry(3, 420, 293, 170)
        self.label2.setStyleSheet("""
                                            background-color: white;
                                            border: none;
                                            border-top-left-radius: 0px;
                                            border-top-right-radius: 0px;
                                            border-bottom-left-radius: 32px;
                                            border-bottom-right-radius: 32px;
                                       
                                 """)

        self.icon_label3 = QLabel(panel)
        self.icon_label3.setGeometry(245, 433, 16, 16)
        pixmap3 = QPixmap("return1.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label3.setPixmap(pixmap3)
        self.icon_label3.setStyleSheet("background-color: transparent;");

        self.icon_label4 = QLabel(panel)
        self.icon_label4.setGeometry(270, 432, 16, 16)
        pixmap4 = QPixmap("save1.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label4.setPixmap(pixmap4)
        self.icon_label4.setStyleSheet("background-color: transparent;");

        self.icon_label3.mousePressEvent = self.on_return_clicked
        self.icon_label4.mousePressEvent = self.on_register_clicked

        self.filter_button = QPushButton("Filter", panel)
        self.filter_button.setCheckable(True)
        self.filter_button.clicked.connect(self.on_button_clicked)
        self.filter_button.setStyleSheet(  # Background color with transparency
            "border-radius: 10px;"
            "color: white;"
            "font-family: 'Glacial Indifference';"  # Change font family
            "font-size: 9pt;"
            "background-color: rgba(185, 149, 200, 250);")  # Change font size
        # Stroke with 50% opacity
        self.filter_button.setGeometry(19, 433, 75, 20)
        self.natural_button = QPushButton("Natural", panel)
        self.natural_button.setCheckable(True)
        self.natural_button.clicked.connect(self.on_button_clicked)
        self.natural_button.setStyleSheet(  # Background color with transparency
            "border-radius: 10px;"
            "background-color: rgba(185, 149, 200, 50);"
            "font-family: 'Glacial Indifference';"  # Change font family
            "font-size: 9pt;")  # Change font size
        self.natural_button.setGeometry(80, 433, 75, 20)

        IntensityBar(panel, self)

        viewModel(panel, self)
        self.setCentralWidget(panel)

    def on_return_clicked(self, event):
        from TestXX1 import MenuPage
        self.menu_page = MenuPage()
        self.menu_page.show()
        self.close()

    def on_register_clicked(self, event):
        # Enregistrer l'image dans le chemin spécifié par l'utilisateur
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = self.main_label1.pixmap()
            pixmap.save(file_path, "PNG")

    def update_main_label(self, path):

        self.main_label1.setStyleSheet(f"""
                                        border-radius: 32px;
                                        border: 1px solid rgba(185, 149, 200, 250);
                                        background-image: url('{path}');
                                        
                                     """)

    def on_button_clicked(self):
        sender = self.sender()
        self.image = None
        if sender.isChecked():
            sender.setStyleSheet(
                "background-color: rgba(185, 149, 200, 250); color: white; border-radius: 10px; font-family: 'Glacial Indifference'; font-size: 9pt;")
            other_button = self.filter_button if sender == self.natural_button else self.natural_button
            other_button.setChecked(False)
            other_button.setStyleSheet("background-color: rgba(185, 149, 200, 50); color: black; "
                                       "border-top-left-radius: 10px;"
                                       "border-top-right-radius: 10px;"
                                       "border-bottom-left-radius: 10px;"
                                       "border-bottom-right-radius: 10px;"
                                       "font-family: 'Glacial Indifference'; "
                                       "font-size: 9pt;")

        if sender == self.natural_button:
            self.image = self.natural_image

        else:
            self.image = self.filtred_image

        self.update_main_label(self.image)

    def apply_filter(self, fit):
        self.filter = fit
        self.filtred_image = "filtred_image.jpg"
        filtred_image = None
        print(self.filter)
        print(self.natural_image)
        if self.filter == "vintage":
            filtred_image = apply_vintage_filter(self.natural_image)
        elif self.filter == "Pixel":
            filtred_image = dot_pixel_effect(self.natural_image)
        elif self.filter == "Light":
            filtred_image = apply_light_leak(self.natural_image)
        elif self.filter == "Vignette":
            filtred_image = apply_vignette_filter(self.natural_image)
        elif self.filter == "gray":
            filtred_image = classic_monochrome(self.natural_image)
        elif self.filter == "colorful":
            filtred_image = rainbow_radiance_filter(self.natural_image)
        elif self.filter == "art":
            filtred_image = create_pencil_sketch(self.natural_image)
       


        if filtred_image is not None :
            print("is not None")
            cv2.imwrite(self.filtred_image, filtred_image)
            print(self.filtred_image)
            self.update_main_label(self.filtred_image)


class IntensityBar(QWidget):
    def __init__(self, parent, pere):
        super().__init__(parent)
        self.v = 20  # vintage
        self.p = 1  # pixel
        self.g=1.5
        self.seuil_v = 80
        self.seuil_p = 5
        self.seuil_g=0.4
        self.pere = pere
        # Position et taille de la barre d'intensité
        # self.setGeometry(48, 395, 200, 40)
        self.setGeometry(48, 380, 200, 30)
        self.line = QFrame(self)
        self.line.setGeometry(0, 13, 200, 2)  # Position et taille de la ligne
        self.line.setFrameShape(QFrame.HLine)
        self.line.setStyleSheet("border: 2px solid rgba(255, 255, 255, 30);"
                                "background-color: transparent;")
        # "border-radius:4px ;")

        self.point = QLabel("●", self)
        self.point.setGeometry(-1, 0, 20, 25)  # Position et taille du point
        self.point.setStyleSheet("font-size: 20px; color: rgba(255, 255, 255, 255);"
                                 "background-color: transparent;")
        self.point.raise_()

        self.point_position = 0

    def mousePressEvent(self, event):
        self.move_point(event.pos().x())
        print("le point est deplace")
        if self.pere.filter == "vintage":
            if self.v < self.seuil_v - 10:
                self.v = self.v + 10

            else:
                self.v = self.seuil_v
            i = apply_vintage_filter(self.pere.natural_image, self.v)
            cv2.imwrite(self.pere.filtred_image, i)
            self.pere.update_main_label(self.pere.filtred_image)


        elif self.pere.filter == "Pixel":
            if self.p < self.seuil_p - 2:
                self.p = self.p + 1
            else:
                self.p = self.seuil_p

            i = dot_pixel_effect(self.pere.natural_image, self.p)
            cv2.imwrite(self.pere.filtred_image, i)
            self.pere.update_main_label(self.pere.filtred_image)

        elif self.pere.filter == "gray":
            if self.g > self.seuil_g+0.2:
               self.g = self.g - 0.2
            else:
               self.g = self.seuil_g
            print(self.g)

            i =  classic_monochrome(self.pere.natural_image, self.g)
            cv2.imwrite(self.pere.filtred_image, i)
            self.pere.update_main_label(self.pere.filtred_image)




    def mouseMoveEvent(self, event):
        self.move_point(event.pos().x())

    def move_point(self, x):
        x = min(max(8, x), self.width())  # Limit position between 8 and width
        self.point.move(x - self.point.width() // 2, 0)  # Move the point

        # Update the point position
        self.point_position = x

        if self.point_position >= self.width():
            self.point_position = 0
            self.point.setGeometry(-1, 0, 20, 25)
            self.v = 20  # vintage
            self.p = 1
            self.g=2
            self.pere.update_main_label(self.pere.natural_image)


            # Redessine le widget

        # Redraw the widget
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(255, 255, 255, 250), 2)
        painter.setPen(pen)

        # Draw the line segment before the point
        if self.point_position > 0:
            painter.drawLine(0, 15, self.point_position, 15)

        # Draw the rest of the line
        pen.setColor(QColor(255, 255, 255, 30))
        painter.setPen(pen)
        painter.drawLine(self.point_position, 15, self.width(), 15)


class Container1(QWidget):
    previous_clicked = None

    def __init__(self, filtername, image2, title, parent):
        super().__init__()
        self.setFixedSize(105, 105)
        self.clicked = False
        self.filter = filtername
        self.parent = parent

        # Créer un bouton rond avec une icône
        self.label1 = QLabel(self)
        self.label1.setFixedSize(100, 86)
        self.label1.move(2, 2)
        self.label1.setStyleSheet("""
                       border-radius: 16px;
                       border: 2px solid rgba (152, 214, 227, 250);
                       background-color: transparent;
                    """)

        self.svg_widget = QSvgWidget(image2, self.label1)
        self.svg_widget.setGeometry(0, 0, 100, 86)
        self.svg_widget.move(0, 0)
        self.svg_widget.setParent(self.label1)

        self.label2 = QLabel(title, self)
        self.label2.setGeometry(18, 93, 80, 13)
        self.label2.setStyleSheet("color: #B0B0B0;"
                                  "font-family: 'Glacial Indifference';"  # Change font family
                                  "font-size: 8pt;"
                                  "background-color: transparent;"
                                  # "font-weight: bold;"
                                  # Change font size
                                  )  # Optionally set text color

        # Set rounded mask for SVG widget
        rounded_mask = self.createRoundedMask(self.svg_widget.size(), 16)
        self.svg_widget.setMask(rounded_mask)

        self.label1.mousePressEvent = lambda event: self.on_label_clicked(event, self.filter, self.parent)

        # Créer une étiquette avec le texte passé en paramètre

    def on_label_clicked(self, event, filter_name, parent):
        print("Image clicked")
        print("True")
        if Container1.previous_clicked:
            # Restore previous clicked container's properties
            Container1.previous_clicked.clicked = False
            Container1.previous_clicked.update()

            Container1.previous_clicked.label2.setStyleSheet(
                "color: #B0B0B0; font-family: 'Glacial Indifference'; font-size: 8pt; background-color: transparent; ")

            # Change the title color
        self.label2.setStyleSheet("color: rgba(185, 149, 200, 250);"
                                  "font-family: 'Glacial Indifference';"  # Change font family
                                  "font-size: 8pt;"
                                  "background-color: transparent;"
                                  "font-weight: bold;")  #
        self.clicked = True  # Set the flag to True
        self.update()
        Container1.previous_clicked = self
        # print(filter_name)
        parent.apply_filter(filter_name)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(0, 0, 104, 90, 18, 18)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        if self.clicked:
            brush = QBrush(QColor(185, 149, 200, 250))
            pen = QPen(QColor(185, 149, 200, 250), 3, Qt.SolidLine)
            # brush=QBrush(QColor(152, 214, 227, 50))

        else:
            brush = QBrush(QColor(185, 149, 200, 0))
            pen = QPen(QColor(185, 149, 200, 0), 0, Qt.SolidLine)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawPath(path)

        # Draw the stroke around the rounded rectangle
        # pen = QPen(QColor(185, 149, 200, 250), 4, Qt.SolidLine)
        # pen = QPen(QColor(152, 214, 227, 50), 3, Qt.SolidLine)
        # painter.setPen(pen)
        # painter.drawPath(path)

    def createRoundedMask(self, size, radius):
        mask = QBitmap(size)
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(QRect(0, 0, size.width(), size.height()), radius, radius)
        painter.end()
        return mask


class viewModel(QWidget):
    def __init__(self, parent, pere):
        super().__init__(parent)
        # self.setFixedSize(300, 800)
        # self.setStyleSheet("background-color:blue")
        self.pere = pere

        # Change font size
        defile_scrol = QScrollArea(parent)
        defile_scrol.setWidgetResizable(True)
        defile_scrol.setGeometry(0, 465, 300, 110)
        defile_scrol.setStyleSheet(
            "QScrollBar:vertical {"
            "    background: transparent;"
            "    width: 0px;"  # Set the width to 0 to hide the vertical scrollbar
            "}"
            "QScrollBar:horizontal {"
            "    background: transparent;"
            "    height: 0px;"  # Set the height to 0 to hide the horizontal scrollbar
            "}"
            "QScrollBar::handle:vertical {"
            "    background: rgba(0, 0, 0, 0);"
            "}"
            "QScrollBar::handle:horizontal {"
            "    background: rgba(0, 0, 0, 0);"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
            "    width: 0px;"
            "}"
            "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {"
            "    height: 0px;"
            "}"
        )

        defile_layout = QHBoxLayout()
        defile_layout.setContentsMargins(5, 5, 5, 5)

        defile = QWidget()
        defile.setContentsMargins(0, 0, 0, 0)
        defile.setAutoFillBackground(False)
        defile.setStyleSheet(f"border: none;background-color:transparent;")
        defile_layout.addWidget(Container1("vintage", "vintage.svg", "     Vintage", self.pere))

        # defile_layout.addWidget(Container("Light", "Light Leak", "lightl1.svg"))
        defile_layout.addWidget(Container1("Pixel", "pic.svg", "    Pixel Pop", self.pere))
        defile_layout.addWidget(Container1("Light", "lightl1.svg", "    Light Leak", self.pere))
        defile_layout.addWidget(Container1("Vignette", "sha.svg", "  Shadow Veil", self.pere))

        defile_layout.addWidget(Container1("gray", "leaves.svg", "Monochrome", self.pere))
        defile_layout.addWidget(Container1("colorful", "image3.svg", "     Rainbow", self.pere))
        # defile_layout.addWidget(Container2("", "image2.svg",filtername="art"))
        defile_layout.addWidget(Container1("art", "draw.svg", "      Artistic", self.pere))

        # defile_layout.addWidget(Container("Pixel", "Pixel Pop", "sw.svg"))

        defile_layout.addWidget(Container1("Van Gogh", "van.svg", "     Strokes", self.pere))
        defile_layout.addWidget(Container1("Old", "old.svg", "     Timeless", self.pere))
        defile_layout.addWidget(Container1("Color", "color1.svg", "      Revive", self.pere))
        # defile_layout.addWidget(Container1("Color","color.svg"))

        defile.setLayout(defile_layout)
        defile_scrol.setWidget(defile)
