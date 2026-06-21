import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the window title and size
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)

        # Style the main window background (Deep dark canvas)
        self.setStyleSheet("QMainWindow { background-color: #121212; }")

        # Create a central container area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        central_widget.setLayout(main_layout)

        # ✨ THE BLUR PANEL (Frosted Glass Effect Layout)
        # Using a semi-transparent white layer over the dark background to simulate frost/blur
        self.glass_panel = QWidget()
        self.glass_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 30);
                border: 1px solid rgba(255, 255, 255, 45);
                border-radius: 15px;
            }
        """)
        
        # Add an empty layout inside the glass panel for our future screen designs
        glass_layout = QVBoxLayout()
        self.glass_panel.setLayout(glass_layout)
        
        # Add the pane into our main view window
        main_layout.addWidget(self.glass_panel)

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
