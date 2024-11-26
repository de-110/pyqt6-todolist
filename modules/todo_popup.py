import os

from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic


ui_directory = os.path.dirname(os.path.abspath(__file__))
ui_file_path = os.path.join(ui_directory, '../ui', 'todolist_popup.ui')
todolist_popup_ui, classinfo = uic.loadUiType(ui_file_path)

class PopUp(QWidget, todolist_popup_ui):
    def __init__(self, parent=None):
        super(PopUp, self).__init__()
        self.parent = parent
        self.setWindowTitle("Task")
        self.setupUi(self)
        self.counter = []

        self.add_task.clicked.connect(self.userTask)

    def userTask(self):
        task = self.task_input.toPlainText()
        
        if task.strip() == '':
            QMessageBox.warning(self, '', 'Please enter task')
        
        else:
            self.parent.item_added(task)
            self.parent.populate_task_view()
            self.close()
