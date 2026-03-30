from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QApplication,
    QWidget,
    QLineEdit,
    QComboBox)
from PyQt5.QtCore import Qt


app = QApplication([])
w = QWidget()

w.setFixedSize(900, 400)
w.setWindowTitle('Конвертер')










w.show()
app.exec()