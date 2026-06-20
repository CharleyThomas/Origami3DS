import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the window title and size
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)

        # Create a central container area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout to center our text
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add a nice placeholder message
        label = QLabel("Welcome to Origami3DS\nYour fresh canvas starts here!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333333;")
        layout.addWidget(label)


# Start the application engine
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
