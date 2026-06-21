import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QMenuBar
from PyQt6.QtCore import Qt
from background import WindowEnvironmentManager
from 3DS.viewport import ThreeDSMenuViewport


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 🌌 Initialize background styles, music, and baseline window frames
        self.environment = WindowEnvironmentManager(self)

        # 📌 1. THE TOP NAVIGATION BAR (MenuBar)
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #111111;
                color: #ffffff;
                font-size: 14px;
                padding: 5px;
                border-bottom: 1px solid #222222;
            }
            QMenuBar::item {
                background: transparent;
                padding: 4px 10px;
                margin-right: 5px;
            }
            QMenuBar::item:selected {
                background-color: #313131;
                border-radius: 4px;
            }
        """)

        # Add your placeholder navigation elements matching your layout sketch
        self.menu_bar.addMenu("File")
        self.menu_bar.addMenu("fdgbdj")
        self.menu_bar.addMenu("zbhvdefjuhgie")
        self.menu_bar.addMenu("fnrjwtbghrjf")
        self.menu_bar.addMenu("nfjjirhngirf")

        # Create a clean container block to align layout items below the menu bar
        master_container = QWidget()
        self.setCentralWidget(master_container)
        
        # Pull the core layout framework directly from the environment module
        master_layout = self.environment.master_layout
        master_container.setLayout(master_layout)

        # 📌 2. THE LEFT SECTION (Injecting the 3DS Viewport directly into the housing)
        self.menu_elements = ThreeDSMenuViewport()
        self.environment.left_layout.addWidget(self.menu_elements, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Add the left black column explicitly to our master layout view
        master_layout.addWidget(self.environment.left_housing)

        # 📌 3. THE RIGHT SECTION (Injecting the frosted canvas panel)
        master_layout.addWidget(self.environment.canvas_panel, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
