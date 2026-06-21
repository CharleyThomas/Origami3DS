import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class WindowEnvironmentManager:

    def __init__(self, main_window):
        self.window = main_window
        
        # 🖥️ Style the main container window frame
        # Sets the solid background color and mimics a taller, cleaner title area
        self.window.setWindowTitle("Origami3DS Development Build")
        self.window.resize(1280, 720)
        self.window.setStyleSheet("""
            QMainWindow { 
                background-color: #111111; 
            }
        """)

        # Main horizontal master framework split
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)
        
        self.master_layout = QHBoxLayout()
        self.master_layout.setContentsMargins(0, 0, 45, 0) # Tight on left, spaced on right canvas
        self.master_layout.setSpacing(45)
        central_widget.setLayout(self.master_layout)

        # 🖤 THE PITCH BLACK LEFT SECTION (The 3DS Console Housing Area)
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
        self.left_housing.setLayout(self.left_layout)
        self.master_layout.addWidget(self.left_housing)

        # ❄️ THE FROSTED GLASS EDIT PANEL (Right side workspace)
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
        self.master_layout.addWidget(self.canvas_panel, stretch=1)

        # 🔊 BACKGROUND MUSIC AUDIO ENGINE
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        audio_path = os.path.abspath("bgm.mp3")
        if os.path.exists(audio_path):
            self.player.setSource(QUrl.fromLocalFile(audio_path))
            self.player.setLoops(QMediaPlayer.Loops.Infinite)
            self.audio_output.setVolume(0.25)
            self.player.play()
