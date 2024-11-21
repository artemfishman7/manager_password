import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *

class DeleteButton(QPushButton):
    def __init__(self, table_widget, conn, cursor):
        super().__init__("Удалить")
        self.table_widget = table_widget
        self.conn = conn
        self.cursor = cursor

        self.clicked.connect(self.delete)  

    def delete(self):

        # Удаление выбранной строки
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            name_item = self.table_widget.item(selected_row, 0)
            if name_item:
                name = name_item.text()


                # Удаление из бд
                self.cursor.execute('DELETE FROM passwords WHERE name = ?', (name,))
                self.conn.commit()

                # Удаление из таблицы
                self.table_widget.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления!")