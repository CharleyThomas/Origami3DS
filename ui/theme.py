from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt


class Nintendo3DSWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        # Stacking layout for Top Screen, Bottom Screen, and Button Bar
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # 📺 3DS TOP SCREEN DISPLAY BOUNDS
        self.top_screen = QWidget()
        self.top_screen.setFixedSize(400, 240)
        self.top_screen.setStyleSheet("background-color: #e2e2e2; border: 1px solid #222;")
        layout.addWidget(self.top_screen)

        # 📱 3DS BOTTOM SCREEN DISPLAY BOUNDS
        self.bottom_screen = QWidget()
        self.bottom_screen.setFixedSize(320, 240)
        self.bottom_screen.setStyleSheet("background-color: #d1d1d1; border: 1px solid #222;")
        layout.addWidget(self.bottom_screen, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 🎛️ BUTTON ROW CAPTURE
        button_row = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 15, 0, 0)
        button_layout.setSpacing(10)
        button_row.setLayout(button_layout)

        for _ in range(6):
            btn = QWidget()
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("background-color: #b5b5b5; border-radius: 4px;")
            button_layout.addWidget(btn)

        layout.addWidget(button_row, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()
