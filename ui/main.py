import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMenuBar
from ui.background import WindowEnvironmentManager
from ui.theme import Nintendo3DSWidget


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 🌌 Initialize background styles, music, and baseline windows frames
        self.environment = WindowEnvironmentManager(self)

        # 📌 1. THE TOP NAVIGATION BAR (MenuBar)
        # Replaces standard window headers with a native dark application row
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

        # Add your placeholder navigation elements matching your diagram layout
        self.menu_bar.addMenu("File")
        self.menu_bar.addMenu("fdgbdj")
        self.menu_bar.addMenu("zbhvdefjuhgie")
        self.menu_bar.addMenu("fnrjwtbghrjf")
        self.menu_bar.addMenu("nfjjirhngirf")

        # Create a container block to align layout items cleanly below the menu bar
        master_container = QWidget()
        self.setCentralWidget(master_container)
        
        # Core split layout framework configuration
        master_layout = QHBoxLayout()
        master_layout.setContentsMargins(0, 0, 45, 0)
        master_layout.setSpacing(45)
        master_container.setLayout(master_layout)

        # 📌 2. THE LEFT SECTION (Pitch Black Console Bay)
        # Pulls the black dock layout directly from our environment configuration
        master_layout.addWidget(self.environment.left_housing)

        # Inject the dual 3DS preview panels safely straight into the left black frame
        self.nintendo_screens = Nintendo3DSWidget()
        self.environment.left_layout.addWidget(self.nintendo_screens)

        # 📌 3. THE RIGHT SECTION (Your future workspace area)
        # Accesses the frosted panel from the background module for layout customization later
        master_layout.addWidget(self.environment.canvas_panel, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
