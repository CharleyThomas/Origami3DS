import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the window title and size
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)

        # Create a central container area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # 🌸 Welcome Label (Clean canvas placeholder)
        welcome_label = QLabel("Welcome to Origami3DS\nYour audio panel is now hidden!")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333333; margin-top: 50px;")
        main_layout.addWidget(welcome_label)
        main_layout.addStretch()

        # 🔊 INVISIBLE BACKGROUND MUSIC ENGINE
        # The media controls are gone from the screen, but the music still plays!
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Check if bgm.mp3 exists right next to the application executable
        audio_path = os.path.abspath("bgm.mp3")
        if os.path.exists(audio_path):
            self.player.setSource(QUrl.fromLocalFile(audio_path))
            self.player.setLoops(QMediaPlayer.Loops.Infinite)
            self.audio_output.setVolume(0.25)  # Soft background volume
            self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
