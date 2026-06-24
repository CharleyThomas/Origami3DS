import sys
import os
import importlib

# 🧭 Path Fix: Force Python to look inside this exact folder for modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QMenuBar
from PyQt6.QtCore import Qt

# 📦 Safe relative loading for your background module
from background import WindowEnvironmentManager

# 🛠️ Safe relative loading for the "3DS" folder (bypasses Python's digit-starting naming rule)
import3ds = importlib.import_module("3DS.viewport")
ThreeDSMenuViewport = import3ds.ThreeDSMenuViewport


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 🌌 Load environment configurations matching your Figma specs down to the pixel
        self.environment = WindowEnvironmentManager(self)

        # 📌 1. HIGH-FIDELITY TOP NAVIGATION BAR (Height: 82px, Hex: #1e1e1e)
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #1e1e1e;
                color: #ffffff;
                font-size: 15px;
                font-family: 'Segoe UI', Arial, sans-serif;
                height: 82px;
                padding-left: 20px;
                border: none;
            }
            QMenuBar::item {
                background: transparent;
                padding: 30px 20px;
                color: #b3b3b3;
            }
            QMenuBar::item:selected {
                color: #ffffff;
                background-color: #2b2b2b;
            }
        """)

        # Custom header tabs mapped from your layout mockup
        self.menu_bar.addMenu("Home")
        self.menu_bar.addMenu("Preview")
        self.menu_bar.addMenu("Export")
        self.menu_bar.addMenu("Overview")
        self.menu_bar.addMenu("Colours")
        self.menu_bar.addMenu("Images")
        self.menu_bar.addMenu("Effects")
        self.menu_bar.addMenu("Settings")

        # Master layout container attachment
        master_container = QWidget()
        self.setCentralWidget(master_container)
        
        master_layout = self.environment.master_layout
        master_container.setLayout(master_layout)

        # 📌 2. INJECT CONTENT TO LEFT FRAME (672px Black Sidebar Column)
        self.menu_elements = ThreeDSMenuViewport()
        self.environment.left_layout.addWidget(self.menu_elements, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.environment.left_housing)

        # 📌 3. INJECT CONTENT TO RIGHT FRAME (Frosted Blur Panel Canvas Workspace)
        master_layout.addWidget(self.environment.canvas_panel, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
