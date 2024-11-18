import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from Savebutton import SaveButton


# подключение к базе данных
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        self.setWindowTitle("Менеджер паролей")
        self.setGeometry(100, 100, 400, 300)

        
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

        
        self.table_widget = QTableWidget(0, 3, central_widget)
        self.table_widget.setGeometry(10, 50, 380, 180)
        self.table_widget.setHorizontalHeaderLabels(["Название", "Логин", "Пароль"])

        
        self.button_delete = QPushButton("Удалить", central_widget)
        self.button_delete.setGeometry(260, 240, 130, 30)
        

        
        self.button_save = SaveButton(self.table_widget, self.line_name, self.line_login, self.line_password, conn, cursor)
        self.button_save.setParent(central_widget)
        self.button_save.setGeometry(130, 240, 120, 30)

        
        self.button_toggle = QPushButton("Показать/Скрыть", central_widget)
        self.button_toggle.setGeometry(0, 240, 120, 30)
    

    def load_data(self):
        # Загрузка данных из базы 
        cursor.execute('SELECT name, login, password FROM passwords')
        rows = cursor.fetchall()
        for row in rows:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(row[0]))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(row[1]))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(row[2]))

    


app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())