import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class WindowEnvironmentManager:

    def __init__(self, main_window):
        self.window = main_window
        
        # Lock down window bounds to match your high-res design frame exactly
        self.window.setWindowTitle("Origami3DS Development Build")
        self.window.resize(1917, 1078)
        self.window.setStyleSheet("""
            QMainWindow { 
                background-color: #1e1e1e; 
            }
        """)

        # Master application frame structure
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)
        
        self.master_layout = QHBoxLayout()
        self.master_layout.setContentsMargins(0, 0, 0, 0) # Running flush against outer screen bounds
        self.master_layout.setSpacing(0)
        central_widget.setLayout(self.master_layout)

        # 🖤 LEFT PITCH BLACK SIDEBAR (Exact width: 672px)
        self.left_housing = QWidget()
        self.left_housing.setFixedWidth(672)
        self.left_housing.setStyleSheet("""
            QWidget {
                background-color: #000000;
            }
        """)
        self.left_layout = QVBoxLayout()
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(0)
        self.left_housing.setLayout(self.left_layout)

        # ❄️ RIGHT FROSTED GLASS WORKSPACE (75% tint-overlay emulation)
        self.canvas_panel = QWidget()
        self.canvas_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(43, 43, 43, 190); /* #2b2b2b at roughly 75% opacity */
                border: none;
            }
        """)
        self.canvas_layout = QVBoxLayout()
        self.canvas_panel.setLayout(self.canvas_layout)

        # 🔊 BACKSTAGE MUSIC DATA ENGINE
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        audio_path = os.path.abspath("bgm.mp3")
        if os.path.exists(audio_path):
            self.player.setSource(QUrl.fromLocalFile(audio_path))
            self.player.setLoops(QMediaPlayer.Loops.Infinite)
            self.audio_output.setVolume(0.25)
            self.player.play()
