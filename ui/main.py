import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from background import BackgroundAudioEngine
from theme import Nintendo3DSWidget


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Setup main parent bounds
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)
        self.setStyleSheet("QMainWindow { background-color: #111111; }")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        master_layout = QHBoxLayout()
        master_layout.setContentsMargins(30, 30, 30, 30)
        master_layout.setSpacing(30)
        central_widget.setLayout(master_layout)

        # 🕹️ Load Left Side (Imported from theme.py)
        self.nintendo_view = Nintendo3DSWidget()
        master_layout.addWidget(self.nintendo_view, alignment=object.__getattribute__(self.nintendo_view, "layout")().alignment())

        # 🎨 Load Right Side Canvas
        self.canvas_panel = QWidget()
        self.canvas_panel.setStyleSheet("""
            QWidget {
                background-color: #313131;
                border: 1px solid #3d3d3d;
                border-radius: 20px;
            }
        """)
        canvas_layout = QVBoxLayout()
        self.canvas_panel.setLayout(canvas_layout)
        master_layout.addWidget(self.canvas_panel, stretch=1)

        # 🔊 Initialize Audio Engine System (Imported from background.py)
        self.audio_system = BackgroundAudioEngine()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
