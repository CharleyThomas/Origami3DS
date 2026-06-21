import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class WindowEnvironmentManager:

    def __init__(self, main_window):
        self.window = main_window
        
        # 🖥️ Basic frame window styling
        self.window.setWindowTitle("Origami3DS Development Build")
        self.window.resize(1280, 720)
        self.window.setStyleSheet("""
            QMainWindow { 
                background-color: #111111; 
            }
        """)

        # Master layout container for splitting Left and Right zones
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)
        
        self.master_layout = QHBoxLayout()
        self.master_layout.setContentsMargins(0, 0, 45, 45) # Padding on right and bottom
        self.master_layout.setSpacing(45)
        central_widget.setLayout(self.master_layout)

        # 🖤 THE PITCH BLACK LEFT SECTION (Houses your 3DS package screens + controls)
        self.left_housing = QWidget()
        self.left_housing.setFixedWidth(460)
        self.left_housing.setStyleSheet("""
            QWidget {
                background-color: #000000;
                border-right: 1px solid #222222;
            }
        """)
        self.left_layout = QVBoxLayout()
        self.left_layout.setContentsMargins(30, 45, 30, 45)
        self.left_layout.setSpacing(20) # Clean gaps between screens and controls
        self.left_housing.setLayout(self.left_layout)

        # ❄️ THE FROSTED GLASS EDIT PANEL (The empty right workspace canvas)
        self.canvas_panel = QWidget()
        self.canvas_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(49, 49, 49, 220);
                border: 1px solid rgba(255, 255, 255, 30);
                border-radius: 20px;
            }
        """)
        self.canvas_layout = QVBoxLayout()
        self.canvas_panel.setLayout(self.canvas_layout)

        # 🔊 APPS ENGINE MUSIC PLAYER (Plays your main app layout track)
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Target your root folder track
        audio_path = os.path.abspath("bgm.mp3")
        if os.path.exists(audio_path):
            self.player.setSource(QUrl.fromLocalFile(audio_path))
            self.player.setLoops(QMediaPlayer.Loops.Infinite)
            self.audio_output.setVolume(0.25)
            self.player.play()
