import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QPushButton, QTableWidgetItem


# Класс для кнопки сохранения
class SaveButton(QPushButton):
    def __init__(self, table_widget, line_name, line_login, line_password, conn, cursor):
        super().__init__("Сохранить")
        self.table_widget = table_widget
        self.line_name = line_name
        self.line_login = line_login
        self.line_password = line_password
        self.conn = conn
        self.cursor = cursor
        self.clicked.connect(self.add_password)

    def add_password(self):
        name = self.line_name.text()
        login = self.line_login.text()
        password = self.line_password.text()

        # Проверка на заполненность полей
        if not name or not login or not password:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        # Сохранение данных в таблицу базы данных
        self.cursor.execute(
            'INSERT INTO passwords (name, login, password) VALUES (?, ?, ?)',
            (name, login, password)
        )
        self.conn.commit()

        # Добавление данных в таблицу 
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(login))
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(password))

        
        self.line_name.clear()
        self.line_login.clear()
        self.line_password.clear()