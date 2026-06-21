import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class OrigamiMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the window title and size
        self.setWindowTitle("Origami3DS Development Build")
        self.resize(1280, 720)

        # Main window frame color (Deep solid black background)
        self.setStyleSheet("QMainWindow { background-color: #111111; }")

        # Create a central container area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Split everything horizontally: Left side is the 3DS, Right side is the Edit Panel
        master_layout = QHBoxLayout()
        master_layout.setContentsMargins(30, 30, 30, 30)
        master_layout.setSpacing(30)
        central_widget.setLayout(master_layout)

        # =====================================================================
        # 🕹️ LEFT SIDE PANEL: THE 3DS CONSOLE LOOK
        # =====================================================================
        nintendo_side = QWidget()
        nintendo_layout = QVBoxLayout()
        nintendo_layout.setContentsMargins(0, 0, 0, 0)
        nintendo_layout.setSpacing(0)  # Keeps screens perfectly stacked
        nintendo_side.setLayout(nintendo_layout)

        # 📺 3DS TOP SCREEN MOCKUP (400x240 Aspect Ratio)
        # Scaled up precisely to 400x240 for crisp default dimension bounds
        self.top_screen = QWidget()
        self.top_screen.setFixedSize(400, 240)
        self.top_screen.setStyleSheet("background-color: #e2e2e2; border: 1px solid #222;")
        nintendo_layout.addWidget(self.top_screen)

        # 📱 3DS BOTTOM SCREEN MOCKUP (320x240 Aspect Ratio)
        # Centered horizontally under the top screen
        self.bottom_screen = QWidget()
        self.bottom_screen.setFixedSize(320, 240)
        self.bottom_screen.setStyleSheet("background-color: #d1d1d1; border: 1px solid #222;")
        nintendo_layout.addWidget(self.bottom_screen, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 🎛️ BOTTOM ROW BUTTONS (The small grey squares underneath)
        button_row = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 15, 0, 0)
        button_layout.setSpacing(10)
        button_row.setLayout(button_layout)

        # Generate the 6 small gray shortcut buttons from your screenshot
        for _ in range(6):
            btn = QWidget()
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("background-color: #b5b5b5; border-radius: 4px;")
            button_layout.addWidget(btn)

        nintendo_layout.addWidget(button_row, alignment=Qt.AlignmentFlag.AlignHCenter)
        nintendo_layout.addStretch()  # Keeps everything pushed nicely to the top

        # Add the 3DS layout stack to the left side of the app
        master_layout.addWidget(nintendo_side, alignment=Qt.AlignmentFlag.AlignVCenter)

        # =====================================================================
        # 🎨 RIGHT SIDE PANEL: THE WORKSPACE CANVAS
        # =====================================================================
        self.canvas_panel = QWidget()
        self.canvas_panel.setStyleSheet("""
            QWidget {
                background-color: #313131;
                border: 1px solid #3d3d3d;
                border-radius: 20px;
            }
        """)
        
        # Give the right side an empty layout for checkboxes/settings later
        canvas_layout = QVBoxLayout()
        self.canvas_panel.setLayout(canvas_layout)
        
        # Add the panel to the right side, telling it to fill the remaining space
        master_layout.addWidget(self.canvas_panel, stretch=1)

        # =====================================================================
        # 🔊 INVISIBLE BACKGROUND MUSIC ENGINE
        # =====================================================================
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
