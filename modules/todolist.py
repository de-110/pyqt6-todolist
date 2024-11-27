import os
import sys
import json

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QFont, QIcon
from PyQt6 import uic

from modules.todo_popup import PopUp
from ui.todolist_home import Ui_MainWindow

class TodoList(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Home")
        
        self.db_path = None
        self.todo_list_task = None

        self.load_data()
        self.populate_task_view()

        self.add_task.clicked.connect(self.OpenPopUp)
        self.remove_user_task.clicked.connect(self.remove_task)

    def OpenPopUp(self):
        self.popup = PopUp(self)
        self.popup.show()
    
    def load_data(self):
        try:
            with open(self.db_path, "r") as data_file:
                self.todo_list_task = json.load(data_file)

        except Exception:
            db_dir = os.path.join(os.getcwd(), "database")
            os.makedirs(db_dir, exist_ok=True)
            self.db_path = os.path.join(db_dir, 'todolist.json')
            self.todo_list_task = {
                'todo_list': []
            }
            with open(self.db_path, "w") as data_file:
                json.dump(self.todo_list_task, data_file, indent=4)

    def update_json(self):
        with open(self.db_path, "w") as data_file:
            json.dump(self.todo_list_task, data_file, indent=4)

    def item_added(self, task):
        self.task_view.addItem(task)
        for x in range(self.task_view.count()):
            text = self.task_view.item(x).text()
            if text == task:
                task_id = x

        new_task = {
            task_id:
                {
                    'user_tasks': task
                }
                  
            }
        self.todo_list_task['todo_list'].append(new_task)

        self.update_json()


    def populate_task_view(self):
        self.task_view.clear()

        self.task_view.setFont(QFont("Tahoma", 16))
        self.task_view.setSpacing(8)
        
        for task in self.todo_list_task['todo_list']:
            for key in task:
                task_id = key
            user_task = task[task_id]['user_tasks']
            self.task_view.addItem(user_task)     
    
    def remove_task(self):
        current_item = self.task_view.currentItem()
        
        if not current_item:
            QMessageBox.warning(self, '', 'No task selected!')

        else:
            selected_item_text = current_item.text()
            selected_item_row = self.task_view.currentRow()

            task_to_remove = None
            for task in self.todo_list_task['todo_list']:
                task_id, details = next(iter(task.items()))
                
                if details['user_tasks'] == selected_item_text:
                    task_to_remove = task
                    break
                

            if task_to_remove:

                self.todo_list_task['todo_list'].remove(task_to_remove)
                self.update_json()

                self.task_view.takeItem(selected_item_row)

                self.populate_task_view()
            