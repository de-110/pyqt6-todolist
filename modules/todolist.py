import os
import json

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QFont, QIcon
from PyQt6 import uic

from modules.todo_popup import PopUp


ui_directory = os.path.dirname(os.path.abspath(__file__))
ui_file_path = os.path.join(ui_directory, '../ui', 'todolist_home.ui')
todolist_home_ui, classinfo = uic.loadUiType(ui_file_path)

icons_directory = os.path.dirname(os.path.abspath(__file__))
icons_file_path = os.path.join(icons_directory, '../assets', 'resources.qrc')

class TodoList(QMainWindow, todolist_home_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Home")
        self.setWindowIcon(QIcon(icons_file_path))
        
        self.db_path = None
        self.todo_list_task = None

        self.set_db_path()
        self.load_data()
        self.populate_task_view()

        self.add_task.clicked.connect(self.OpenPopUp)
        self.remove_user_task.clicked.connect(self.remove_task)

    def OpenPopUp(self):
        self.popup = PopUp(self)
        self.popup.show()

    def set_db_path(self):
        db_dirname = '../database'
        db_filename = 'todolist.json'

        db_directory = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(db_directory, db_dirname, db_filename)
    
    def load_data(self):
        try:
            with open(self.db_path, "r") as data_file:
                self.todo_list_task = json.load(data_file)
        except Exception:
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
            