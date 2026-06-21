import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                             QHBoxLayout, QWidget, QPushButton, QSlider, QStyle)
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

        # 🌸 Welcome Label
        welcome_label = QLabel("Welcome to Origami3DS")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333333; margin-top: 20px;")
        main_layout.addWidget(welcome_label)

        # 🎵 AUDIO CONTROLS PANEL
        audio_panel = QWidget()
        audio_panel.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 15px;")
        audio_layout = QVBoxLayout()
        audio_panel.setLayout(audio_layout)

        audio_title = QLabel("🎵 Theme Background Music (BGM)")
        audio_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #555555;")
        audio_layout.addWidget(audio_title)

        control_row = QHBoxLayout()
        
        # Play/Pause Button
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        self.play_button.setFixedWidth(50)
        control_row.addWidget(self.play_button)

        # Stop Button
        self.stop_button = QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        self.stop_button.setFixedWidth(50)
        control_row.addWidget(self.stop_button)

        # Audio Track Timeline Slider
        self.timeline_slider = QSlider(Qt.Orientation.Horizontal)
        self.timeline_slider.setRange(0, 100)
        control_row.addWidget(self.timeline_slider)

        # File Status Text
        self.status_label = QLabel("Streaming System Environment Music...")
        self.status_label.setStyleSheet("color: #4CAF50; font-style: italic; font-weight: bold;")
        control_row.addWidget(self.status_label)

        audio_layout.addLayout(control_row)

        main_layout.addStretch()
        main_layout.addWidget(audio_panel)

        # 🔊 BACKGROUND MUSIC ENGINE INTAKE
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Link buttons to the player controls
        self.play_button.clicked.connect(self.toggle_play)
        self.stop_button.clicked.connect(self.stop_music)
        
        # Set up an open, direct server stream url for development
        music_url = "https://ia801402.us.archive.org/24/items/wii-system-soundtrack-flac/Wii%20Shop%20Channel.mp3"
        self.player.setSource(QUrl(music_url))
        
        # Enable automated playlist looping logic
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        
        # Set a soft volume and start playing immediately!
        self.audio_output.setVolume(0.25)
        self.player.play()

    def toggle_play(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
            self.status_label.setText("Music Paused")
        else:
            self.player.play()
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
            self.status_label.setText("Streaming Ambient System Music...")

    def stop_music(self):
        self.player.stop()
        self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.status_label.setText("Music Stopped")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrigamiMainWindow()
    window.show()
    sys.exit(app.exec())
