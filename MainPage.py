from PySide6.QtGui import QFont, QFontDatabase, QColor, QPen, QPainter, QBrush, QPainterPath, QTextOption, \
    QTextCharFormat, QTextCursor, QIcon, QPalette, QAction, QImageReader, QBitmap, QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsBlurEffect, QWidget, QVBoxLayout, QTextEdit, \
    QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QDialog, QFrame, QGraphicsOpacityEffect, QFileDialog
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import *
from PySide6.QtSvg import *



class MiniWindow(QWidget):
    def __init__(self, main_window, k):
        super().__init__(main_window)
        self.main_window = main_window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: transparent;")

        main_rect = main_window.rect()
        mini_width = 300
        mini_height = 300
        mini_x = main_rect.x() + (main_rect.width() - mini_width) // 2
        mini_y = main_rect.bottom() - mini_height

        self.setGeometry(mini_x, mini_y, mini_width, mini_height + 2)

        container = QFrame(self)
        container.setGeometry(0, 0, mini_width, mini_height + 2)
        container.setStyleSheet("background-color: white; border-radius: 32px;")

        if k == 1:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Classic Monochrome", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 30pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(40, 15)
            self.label = QLabel(
                "The Classic Monochrome filter transforms your photos \n into timeless black-and-white images. If you're looking \n   for a touch of nostalgia, the Classic Monochrome \n                    filter is the perfect choice.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)


        elif k == 2:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Rainbow Radiance", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(50, 15)
            self.label = QLabel(
                "The Rainbow Radiance filter adds a burst of vibrant \n colors to your images, creating a stunning and artistic \n     effect. This filter enhances the colors, making them \n                       more vivid and dynamic.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)

        elif k == 3:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Artistic Aura", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(50, 15)
            self.label = QLabel(
                "The Artistic Aura filter transforms your images into mes-\n   merizing work of art with an enchanting aura. This\n   filter applies a hand-drawn effect to your  photos\n                      giving them an artistic flair.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)

        elif k == 4:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Vintage Essence", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(60, 15)
            self.label = QLabel(
                "The Vintage Essence filter imbues your photos with the \n  essence of a bygone era. This filter adds warmth, and a\n                  hint of nostalgia to your photos.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)
        elif k == 5:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Light Leak", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(55, 10)
            self.label = QLabel(
                "Light Leak adds a charm to your photos, simulating light\n        leaks from old film cameras. It creates subtle\n       bursts of light around edges, adding a dreamy, \n                                nostalgic vibe.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)

        elif k == 6:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Shadow Veil", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(60, 10)
            self.label = QLabel(
                "The Shadow Veil filter artistically darkens the edges of \n       your image, gently guiding the viewer's gaze\n               towards the beautifully highlighted \n                                     center. ",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)

        elif k == 7:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Pixel Pop", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(80, 10)
            self.label = QLabel(
                " Pixel Pop is a fun filter that adds a  pixelated  effect\n     to your photos, giving them a vibrant and edgy \n    look. This effect creates a unique aesthetic vibe.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(20, 90)
        elif k == 8:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Starry Strokes", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(56, 10)
            self.label = QLabel(
                "    Starry Strokes transforms your photos into artworks\ninspired by the iconic style of Vincent Van Gogh.It applies  \n  dynamic brush strokes and vibrant colors to recreate \n      the mesmerizing beauty of his famous paintings.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(14, 90)

        elif k == 9:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Timeless Revival", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(58, 10)
            self.label = QLabel(
                "    Timeless Revival breathes new life into old images,\nrestoring their colors and details to vivid clarity. This filter \n    revitalizes your old photos, transforming them  into \n                              vibrant memories.",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(16, 90)

        elif k == 10:
            id = QFontDatabase.addApplicationFont("Demo.otf")
            families2 = QFontDatabase.applicationFontFamilies(id)
            self.label = QLabel("Selfie To Scene", container)
            self.label.setStyleSheet("color: black;"
                                     "font-family: 'Creattion Demo';"  # Change font family
                                     "font-size: 32pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(48, 10)
            self.label = QLabel(
                "Selfie to Scene filter is a transformative tool that takes a \nsimple selfie and expands it into a vibrant, detailed scene.\n      This filter analyzes the selfie's features and context \n              to create a complete visual narrative. ",
                container)
            self.label.setStyleSheet("color: #999999;"
                                     "font-family: 'Glacial Indifference';"  # Change font family
                                     "font-size: 8pt;"
                                     # "font-weight: bold;"
                                     "background-color: transparent;")
            self.label.move(14, 90)

        self.return_button = QPushButton("Dismiss", container)
        self.return_button.setStyleSheet("background-color: rgba(185, 149, 200, 250);"
                                         "border-radius: 10px;"
                                         "border: 2px solid rgba(185, 149, 200, 150);"
                                         "font-family: 'Glacial Indifference';"
                                         "font-size: 10pt;"
                                         "color: #FFFFFF;")

        # self.button.setGeometry(65, 500, 170, 37)  # Adjusted position to be at the bottom of the window
        self.return_button.setGeometry(30, 220, 240, 30)
        self.return_button.setAutoDefault(False)
        self.return_button.setCursor(Qt.PointingHandCursor)
        self.return_button.clicked.connect(self.close)

        self.apply_button = QPushButton("Apply", container)
        self.apply_button.setStyleSheet("background-color: rgba(152, 214, 227, 200);"
                                        "border-radius: 10px;"
                                        "border: 2px solid rgba(152, 214, 227, 150);;"
                                        "font-family: 'Glacial Indifference';"
                                        "font-size: 10pt;"
                                        "color: #FFFFFF;")

        # self.button.setGeometry(65, 500, 170, 37)  # Adjusted position to be at the bottom of the window
        self.apply_button.setGeometry(30, 180, 240, 30)
        self.apply_button.setAutoDefault(False)
        self.apply_button.setCursor(Qt.PointingHandCursor)
        self.apply_button.clicked.connect(self.goToGalleryPage)

    def showEvent(self, event):
        super().showEvent(event)
        self.opacity_effect = QGraphicsOpacityEffect(self.main_window.centralWidget())
        self.opacity_effect.setOpacity(0.5)  # Set the opacity to darken the main window
        self.main_window.centralWidget().setGraphicsEffect(self.opacity_effect)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.main_window.centralWidget().setGraphicsEffect(None)  # Remove the opacity effect

    def goToGalleryPage(self):
        file_dialog = QFileDialog()
        file_dialog.setDirectory(r"C:\Users\DELL\Desktop\TraitementImage")
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")

        file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")

        if file_path:
            from TestXX2 import GalleryPage
            event = QCloseEvent()
            self.closeEvent(event)
            self.gallery_page = GalleryPage(file_path)  # Pass the file path to the GalleryPage constructor
            self.gallery_page.show()
            self.main_window.hide()


class viewModel(QWidget):
    def __init__(self, title, k):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color:white;")

        labelr = QLabel(title, self)

        if k == 0:
            labelr.setStyleSheet("color: black;"
                                 "font-family: 'Glacial Indifference';"  # Change font family
                                 "font-size: 10pt;"

                                 # "font-weight: bold;"
                                 "background-color: transparent;"

                                 # Change font size
                                 )  # Optionally set text color
            labelr.setGeometry(56, 3, 180, 20)

        else:
            labelr.setStyleSheet("color: black;"
                                 "font-family: 'Glacial Indifference';"  # Change font family
                                 "font-size: 12pt;"
                                 "font-weight: bold;"
                                 "background-color: transparent;")
            labelr.setGeometry(10, 5, 110, 20)
            # Change font size
        defile_scrol = QScrollArea(self)
        defile_scrol.setGeometry(0, 25, 295, 178)
        defile_scrol.setWidgetResizable(True)
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

        if k == 0:
            defile_layout.addWidget(Container2("", "leaves.svg", filtername="gray"))
            defile_layout.addWidget(Container2("", "image3.svg", filtername="colorful"))
            # defile_layout.addWidget(Container2("", "image2.svg",filtername="art"))
            defile_layout.addWidget(Container2("", "draw.svg", filtername="art"))
            defile_layout.addWidget(Container2("", "vintage.svg", filtername="vintage"))
        elif k == 1:
            # defile_layout.addWidget(Container("Light", "Light Leak", "lightl1.svg"))
            defile_layout.addWidget(Container("Pixel", "Pixel Pop", "pic.svg"))
            defile_layout.addWidget(Container("Light", "Light Leak", "lightl1.svg"))
            defile_layout.addWidget(Container("Vignette", "Shadow Veil ", "sha.svg"))
            # defile_layout.addWidget(Container("Pixel", "Pixel Pop", "sw.svg"))


        else:
            defile_layout.addWidget(Container1("Old", "old.svg"))
            defile_layout.addWidget(Container1("Color", "color1.svg"))
            defile_layout.addWidget(Container1("Van Gogh", "van.svg"))
        # defile_layout.addWidget(Container1("Color","color.svg"))

        defile.setLayout(defile_layout)
        defile_scrol.setWidget(defile)


class MenuPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 590)  # Set the fixed size of the window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(800, 50)

        panel = QWidget()
        panel.setStyleSheet("background-color:white;border-radius:32px")
        self.create_elements(panel)

        self.text_label1 = QLabel("Explore ", panel)

        self.text_label1.setGeometry(15, 27, 50, 20)
        id = QFontDatabase.addApplicationFont("GlacialIndifference.otf")
        families = QFontDatabase.applicationFontFamilies(id)
        self.text_label1.setStyleSheet("color: black;"
                                       "font-family: 'Glacial Indifference';"  # Change font family
                                       "font-size: 10pt;"  # Change font size
                                       )  # Optionally set text color

        self.text_label2 = QLabel(panel)
        self.text_label2.setGeometry(15, 45, 125, 30)
        id = QFontDatabase.addApplicationFont("GlacialIndifference.otf")
        families = QFontDatabase.applicationFontFamilies(id)
        self.text_label2.setStyleSheet("color: black;"
                                       "font-family: 'Glacial Indifference';"  # Change font family
                                       "font-size: 18pt;"
                                       "font-weight: bold;"
                                       # Change font size
                                       )  # Optionally set text color
        self.text_label2.setText("BrushMagic ")

        self.icon_label = QLabel(panel)
        self.icon_label.setGeometry(216, 27, 16, 16)
        pixmap = QPixmap("loc.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label.setPixmap(pixmap)

        self.text_label3 = QLabel(panel)
        self.text_label3.setGeometry(234, 23, 80, 30)
        id = QFontDatabase.addApplicationFont("GlacialIndifference.otf")
        families = QFontDatabase.applicationFontFamilies(id)
        self.text_label3.setStyleSheet("color: #606060;"
                                       "font-family: 'Glacial Indifference';"  # Change font family
                                       "font-size: 6pt;"
                                       # "font-weight: bold;"
                                       # Change font size
                                       )  # Optionally set text color
        self.text_label3.setText("Fez, Morocco ")

        self.search_bar = SearchBar(panel)
        self.search_bar.setGeometry(15, 100, 263, 150)

        self.setCentralWidget(panel)

    def create_elements(self, panel):
        central = QWidget()
        central.setContentsMargins(0, 0, 0, 0)
        central.setAutoFillBackground(False)
        central.setStyleSheet("border: none;background-color:transparent;")

        scrol_area = QScrollArea(panel)
        scrol_area.setGeometry(8, 150, 290, 590 - 180)
        scrol_area.setWidgetResizable(True)

        vertical_layout = QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        scrol_area.setStyleSheet(
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

        # j'ajoute les view model a layout vertical :
        view_model1 = viewModel("Chromatic Palette Collection", 0)
        view_model2 = viewModel("Popular", 1)
        view_model3 = viewModel("AI tools", 2)

        vertical_layout.addWidget(view_model1)
        vertical_layout.addWidget(view_model2)
        vertical_layout.addWidget(view_model3)

        central.setLayout(vertical_layout)
        scrol_area.setWidget(central)


class SearchBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)  # Adjust height as needed
        self.setPlaceholderText("Find your filter")
        id = QFontDatabase.addApplicationFont("GlacialIndifference.otf")
        families = QFontDatabase.applicationFontFamilies(id)
        # Apply stylesheet to set rounded corners and other styles
        self.setStyleSheet("""
            QLineEdit {
                border-radius: 10px;  /* Adjust the radius as needed */
                padding-left: 30px;  /* Space for the large icon */
                font-family: 'Glacial Indifference';
                font-size: 10px;  /* Adjust font size as needed */
                background-color: rgba(185, 149, 200, 50);
            }
        """)

        # Create a layout to hold the icon and the QLineEdit
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 235, 0)
        layout.setSpacing(0)

        # Create a label for the icon
        icon_label = QLabel(self)
        icon_label.setPixmap(QIcon("search.png").pixmap(16, 16))
        icon_label.setStyleSheet("background-color: transparent;")  # Adjust size as needed
        layout.addWidget(icon_label)

        # Set background color and text color using QPalette
        palette = self.palette()
        # palette.setColor(QPalette.Base, QColor(185, 149, 200, 200))  # Set the background color
        palette.setColor(QPalette.Text, QColor(96, 96, 96))  # Set the text color
        self.setPalette(palette)


class Container(QWidget):
    def __init__(self, filtername, labeltext, image2, parent=None):
        super().__init__(parent)
        self.setFixedSize(158, 164)

        # Créer un bouton rond avec une icône
        self.label1 = QLabel(self)
        self.label1.setFixedSize(120, 115)
        self.label1.move(10, 10)
        self.label1.setStyleSheet("""
                       border-radius: 20px;
                       border: 1px solid rgba(185, 149, 200, 150);
                       background-color: transparent;
                    """)

        self.svg_widget = QSvgWidget(image2, self.label1)
        self.svg_widget.setGeometry(10, 10, 120, 115)
        self.svg_widget.move(0, 0)
        self.svg_widget.setParent(self.label1)

        # Set rounded mask for SVG widget
        rounded_mask = self.createRoundedMask(self.svg_widget.size(), 20)
        self.svg_widget.setMask(rounded_mask)
        self.filter = filtername
        # Ajouter un gestionnaire d'événements de clic de souris au label
        self.label1.mousePressEvent = lambda event: self.on_label_clicked(event, self.filter)

        # Créer une étiquette avec le texte passé en paramètre
        self.label2 = QLabel(labeltext, self)
        self.label2.setGeometry(15, 132, 100, 15)
        self.label2.setStyleSheet("color: black;"
                                  "font-family: 'Glacial Indifference';"  # Change font family
                                  "font-size: 10pt;"
                                  "background-color: transparent;"
                                  # "font-weight: bold;"
                                  # Change font size
                                  )  # Optionally set text color

        self.icon_label = QLabel(self)
        self.icon_label.setGeometry(105, 122, 32, 32)
        pixmap = QPixmap("heart.png")  # Replace "path_to_your_icon_file.png" with the path to your icon file
        self.icon_label.setPixmap(pixmap)
        self.icon_label.setStyleSheet("background-color: transparent;");

        self.label3 = QLabel("220", self)
        self.label3.setGeometry(133, 132, 100, 15)
        self.label3.setStyleSheet("color: gray;"
                                  "font-family: 'Glacial Indifference';"  # Change font family
                                  "font-size: 7pt;"
                                  "background-color: transparent;"
                                  # "font-weight: bold;"
                                  # Change font size
                                  )  # Optionally set text color

    def on_label_clicked(self, event, filter_name):
        print("Image clicked")
        if filter_name == "Light":
            self.mini_window = MiniWindow(self.window(), 5)
            self.mini_window.show()
        elif filter_name == "Vignette":
            self.mini_window = MiniWindow(self.window(), 6)
            self.mini_window.show()
        elif filter_name == "Pixel":
            self.mini_window = MiniWindow(self.window(), 7)
            self.mini_window.show()
        print("True")
        return filter_name

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(0, 0, 158, 164, 32, 32)

        # brush = QBrush(QColor(185, 149, 200, 13))
        # brush = QBrush(QColor(152, 214, 227, 15))
        brush = QBrush(QColor(185, 149, 200, 30))

        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        # Draw the stroke around the rounded rectangle
        pen = QPen(QColor(185, 149, 200, 50), 2, Qt.SolidLine)  # White color with 30% opacity
        painter.setPen(pen)
        painter.drawPath(path)

    def createRoundedMask(self, size, radius):
        mask = QBitmap(size)
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(QRect(0, 0, size.width(), size.height()), radius, radius)
        painter.end()
        return mask


class Container1(QWidget):
    def __init__(self, filtername, image2, parent=None):
        super().__init__(parent)
        self.setFixedSize(158, 164)

        # Créer un bouton rond avec une icône
        self.label1 = QLabel(self)
        self.label1.setFixedSize(158, 164)
        self.label1.move(0, 0)
        self.label1.setStyleSheet("""
                       border-radius: 32px;
                       border: 1px solid rgba(185, 149, 200, 150);
                       background-color: transparent;
                    """)

        self.svg_widget = QSvgWidget(image2, self.label1)
        self.svg_widget.setGeometry(0, 0, 158, 164)
        self.svg_widget.move(0, 0)
        self.svg_widget.setParent(self.label1)

        # Set rounded mask for SVG widget
        rounded_mask = self.createRoundedMask(self.svg_widget.size(), 32)
        self.svg_widget.setMask(rounded_mask)
        self.filter = filtername
        self.label1.mousePressEvent = lambda event: self.on_label_clicked(event, self.filter)

        # Créer une étiquette avec le texte passé en paramètre

    def on_label_clicked(self, event, filter_name):
        print("Image clicked")
        if filter_name == "Van Gogh":
            self.mini_window = MiniWindow(self.window(), 8)
            self.mini_window.show()
        elif filter_name == "Old":
            self.mini_window = MiniWindow(self.window(), 9)
            self.mini_window.show()
        elif filter_name == "Color":
            self.mini_window = MiniWindow(self.window(), 10)
            self.mini_window.show()
        print("True")
        return filter_name

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rounded rectangle
        path = QPainterPath()
        path.addRoundedRect(0, 0, 158, 164, 32, 32)

        brush = QBrush(QColor(185, 149, 200, 13))
        # brush = QBrush(QColor(152, 214, 227, 15))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)

        # Draw the stroke around the rounded rectangle
        pen = QPen(QColor(185, 149, 200, 150), 1, Qt.SolidLine)  # White color with 30% opacity
        painter.setPen(pen)
        painter.drawPath(path)

    def createRoundedMask(self, size, radius):
        mask = QBitmap(size)
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(QRect(0, 0, size.width(), size.height()), radius, radius)
        painter.end()
        return mask


class Container2(QWidget):
    def __init__(self, labeltext, image1, filtername, parent=None):
        super().__init__(parent)
        self.setFixedSize(220, 147)

        self.svg_widget = QSvgWidget(image1, self)
        self.svg_widget.setGeometry(0, 0, 220, 147)

        # Créer un bouton rond avec une icône

        self.label1 = QLabel(self)
        self.label1.setFixedSize(220, 147)
        self.label1.move(0, 0)
        self.label1.setStyleSheet("""
                       border-radius: 25px;
                       border: 1px solid rgba(185, 149, 200, 150);
                       background-position: transparent;
                   """)

        self.svg_widget.move(0, 0)
        self.svg_widget.setParent(self.label1)

        # Set rounded mask for SVG widget
        rounded_mask = self.createRoundedMask(self.svg_widget.size(), 25)
        self.svg_widget.setMask(rounded_mask)
        self.filter = filtername
        self.label1.mousePressEvent = lambda event: self.on_label_clicked(event, self.filter)

        id = QFontDatabase.addApplicationFont("Gempita.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        self.label2 = QLabel(labeltext, self)
        self.label2.setGeometry(58, 100, 114, 50)
        self.label2.setStyleSheet("color: white;"
                                  "font-family: 'Gempita Brush';"  # Change font family
                                  "font-size: 26pt;"
                                  "background-color: transparent;"
                                  "font-weight: bold;"
                                  # Change font size
                                  )  # Optionally set text color

    def createRoundedMask(self, size, radius):
        mask = QBitmap(size)
        mask.fill(Qt.white)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(QRect(0, 0, size.width(), size.height()), radius, radius)
        painter.end()
        return mask

    def on_label_clicked(self, event, filter_name):
        print("Image clicked")
        if filter_name == "gray":
            self.mini_window = MiniWindow(self.window(), 1)
            self.mini_window.show()
        elif filter_name == "colorful":
            self.mini_window = MiniWindow(self.window(), 2)
            self.mini_window.show()
        elif filter_name == "art":
            self.mini_window = MiniWindow(self.window(), 3)
            self.mini_window.show()
        elif filter_name == "vintage":
            self.mini_window = MiniWindow(self.window(), 4)
            self.mini_window.show()
        print("True")
        return filter_name
