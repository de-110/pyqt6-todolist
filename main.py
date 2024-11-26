import sys
import os

from PyQt6.QtWidgets import QApplication, QStyleFactory
from PyQt6.QtGui import QIcon
from modules.todolist import TodoList

icons_directory = os.path.dirname(os.path.realpath(__file__), )
icons_file_path = os.path.join(icons_directory, '../assets/icons', 'app_logo.png')


app = QApplication(sys.argv)
app.setApplicationDisplayName("TodoList")
app.setApplicationName("TodoList")
app.setStyle(QStyleFactory.create("Fusion"))

window = TodoList()
window.setWindowIcon(QIcon(icons_file_path))
window.show()
sys.exit(app.exec())