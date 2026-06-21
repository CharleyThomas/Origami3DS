import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.background import WindowEnvironmentManager
from ui.theme import Nintendo3DSWidget


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 🌌 Let the background manager generate the glass canvas and pitch black housing frame
        self.environment = WindowEnvironmentManager(self)

        # 🕹️ Initialize the 3DS Console screens inside the left pitch-black deck layout
        self.nintendo_screens = Nintendo3DSWidget()
        self.environment.left_layout.addWidget(self.nintendo_screens)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
