import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QCursor

class MousePositionDisplay(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mouse Position Display')

        self.position_label = QLabel('', self)
        self.position_label.move(100, 100)

        self.click_btn = QPushButton('Show Position', self)
        self.click_btn.move(100, 130)
        self.click_btn.clicked.connect(self.show_position)

    def show_position(self):
        x, y = QCursor.pos().x(), QCursor.pos().y()
        self.position_label.setText(f'Mouse position: ({x}, {y})')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mouse_position_display = MousePositionDisplay()
    mouse_position_display.show()
    sys.exit(app.exec_())
