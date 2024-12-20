# Form implementation generated from reading ui file 'todolist_home.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 569)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: black;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.remove_user_task = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.remove_user_task.sizePolicy().hasHeightForWidth())
        self.remove_user_task.setSizePolicy(sizePolicy)
        self.remove_user_task.setStyleSheet("    QPushButton {\n"
"    border-radius: 20px;\n"
"    font: 700 25pt \"Tahoma\";\n"
"    color: white;\n"
"    background-color: red;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: red;\n"
"    background-color: white;\n"
"}\n"
"")
        self.remove_user_task.setObjectName("remove_user_task")
        self.gridLayout.addWidget(self.remove_user_task, 0, 3, 1, 1)
        self.add_task = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.add_task.sizePolicy().hasHeightForWidth())
        self.add_task.setSizePolicy(sizePolicy)
        self.add_task.setStyleSheet("    QPushButton {\n"
"    border-radius: 20px;\n"
"    font: 700 25pt \"Tahoma\";\n"
"    color: white;\n"
"    background-color: #00ff00;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: #00ff00;\n"
"    background-color: white;\n"
"}\n"
"")
        self.add_task.setObjectName("add_task")
        self.gridLayout.addWidget(self.add_task, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.task_view = QtWidgets.QListWidget(parent=self.centralwidget)
        self.task_view.setStyleSheet("QListWidget::item:selected {\n"
"    color: black;\n"
"    border-left:5px solid red;\n"
"    background-color: rgb(173, 150, 150);\n"
"}")
        self.task_view.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.task_view.setAlternatingRowColors(False)
        self.task_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.task_view.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.task_view.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.task_view.setObjectName("task_view")
        self.gridLayout_2.addWidget(self.task_view, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.remove_user_task.setText(_translate("MainWindow", "X"))
        self.add_task.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
