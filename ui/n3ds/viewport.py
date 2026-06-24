from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt


class ThreeDSMenuViewport(QWidget):

    def __init__(self):
        super().__init__()
        
        # This layout box will soon hold our split-up modular menu components
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)
        
        # Baseline structural boundary sizing
        self.setFixedWidth(400)
