import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem
from Savebutton import SaveButton
from Deletebutton import DeleteButton
from Hidebutton import HideButton
from Searchbutton import SearchButton

# Подключение к БД
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# создание талицы базы данных
cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
    name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# Основной класс приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        self.setWindowTitle("Passwords")
        self.setGeometry(100, 100, 400, 310)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        self.line_name = QLineEdit(central_widget)
        self.line_name.setPlaceholderText('Название')
        self.line_name.setGeometry(10, 10, 120, 25)

        self.line_login = QLineEdit(central_widget)
        self.line_login.setPlaceholderText('Логин')
        self.line_login.setGeometry(140, 10, 120, 25)

        self.line_password = QLineEdit(central_widget)
        self.line_password.setPlaceholderText('Пароль')
        self.line_password.setGeometry(270, 10, 120, 25)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.table_widget = QTableWidget(0, 3, central_widget)
        self.table_widget.setGeometry(10, 50, 380, 180)
        self.table_widget.setHorizontalHeaderLabels(["Название", "Логин", "Пароль"])

        self.button_delete = DeleteButton(self.table_widget, conn, cursor)
        self.button_delete.setParent(central_widget)
        self.button_delete.setGeometry(265, 240, 130, 30)

        self.button_save = SaveButton(
            self.table_widget, 
            self.line_name, 
            self.line_login, 
            self.line_password, 
            conn, 
            cursor
        )
        self.button_save.setParent(central_widget)
        self.button_save.setGeometry(135, 240, 120, 30)

        self.button_hide = HideButton(self.line_password)
        self.button_hide.setParent(central_widget)
        self.button_hide.setGeometry(5, 240, 120, 30)

        self.search_button = QLineEdit(central_widget)
        self.search_button.setPlaceholderText('Поиск по названию')
        self.search_button.setGeometry(10, 280, 260, 25)

        self.button_search = SearchButton(self.table_widget, self.search_button, cursor)
        self.button_search.setParent(central_widget)
        self.button_search.setGeometry(280, 280, 110, 25)

    # загрузка информации из бд
    def load_data(self):
        cursor.execute('SELECT name, login, password FROM passwords')
        rows = cursor.fetchall()
        for row in rows:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(row[0]))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(row[1]))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(row[2]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())