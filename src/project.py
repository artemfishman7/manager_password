# Form implementation generated from reading ui file '/Users/artemf/Desktop/manager_password/src/project.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 462)
        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.central_widget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 130, 361, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.button_delete = QtWidgets.QPushButton(parent=self.central_widget)
        self.button_delete.setGeometry(QtCore.QRect(470, 320, 121, 32))
        self.button_delete.setObjectName("button_delete")
        self.button_save = QtWidgets.QPushButton(parent=self.central_widget)
        self.button_save.setGeometry(QtCore.QRect(370, 320, 113, 32))
        self.button_save.setObjectName("button_save")
        self.button_add = QtWidgets.QPushButton(parent=self.central_widget)
        self.button_add.setGeometry(QtCore.QRect(210, 320, 171, 32))
        self.button_add.setObjectName("button_add")
        self.line_name = QtWidgets.QLineEdit(parent=self.central_widget)
        self.line_name.setGeometry(QtCore.QRect(220, 100, 113, 21))
        self.line_name.setObjectName("line_name")
        self.line_login = QtWidgets.QLineEdit(parent=self.central_widget)
        self.line_login.setGeometry(QtCore.QRect(340, 100, 113, 21))
        self.line_login.setObjectName("line_login")
        self.line_password = QtWidgets.QLineEdit(parent=self.central_widget)
        self.line_password.setGeometry(QtCore.QRect(460, 100, 113, 21))
        self.line_password.setObjectName("line_password")
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Пароль"))
        self.button_delete.setText(_translate("MainWindow", "удалить"))
        self.button_save.setText(_translate("MainWindow", "сохранить"))
        self.button_add.setText(_translate("MainWindow", "Показать/Скрыть"))
        self.line_name.setText(_translate("MainWindow", "название"))
        self.line_login.setText(_translate("MainWindow", "логин"))
        self.line_password.setText(_translate("MainWindow", "пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
