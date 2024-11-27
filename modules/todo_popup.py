import os

from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

from ui.todolist_popup import Ui_Form

class PopUp(QWidget, Ui_Form):
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
