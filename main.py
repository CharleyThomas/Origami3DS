import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the window title and size matching standard screen bounds
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)

        # Main window frame color (Deep solid charcoal/black background)
        self.setStyleSheet("QMainWindow { background-color: #111111; }")

        # Create a central container area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout with margins matching the spacing in your image
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(45, 45, 45, 45)
        central_widget.setLayout(main_layout)

        # 🎨 EXACT REPLICA CANVAS PANEL
        # Matches the smooth, rounded corners and dark gray coloration from your screenshot
        self.canvas_panel = QWidget()
        self.canvas_panel.setStyleSheet("""
            QWidget {
                background-color: #313131;
                border: 1px solid #3d3d3d;
                border-radius: 20px;
            }
        """)
        
        # Give it an empty layout internally so we can place modules inside later
        canvas_layout = QVBoxLayout()
        self.canvas_panel.setLayout(canvas_layout)
        
        # Load the panel directly into our display window layout
        main_layout.addWidget(self.canvas_panel)

        # 🔊 INVISIBLE BACKGROUND MUSIC ENGINE
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        audio_path = os.path.abspath("bgm.mp3")
        if os.path.exists(audio_path):
            self.player.setSource(QUrl.fromLocalFile(audio_path))
            self.player.setLoops(QMediaPlayer.Loops.Infinite)
            self.audio_output.setVolume(0.25)
            self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
