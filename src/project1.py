import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Менеджер паролей")
        self.setGeometry(0, 0, 381, 290)
        
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        
        
        self.line_name = QLineEdit(central_widget)
        self.line_name.setPlaceholderText('название')
        self.line_name.setGeometry(10, 10, 113, 21)

        self.line_login = QLineEdit(central_widget)
        self.line_login.setPlaceholderText('логин')
        self.line_login.setGeometry(130, 10, 113, 21)

        self.line_password = QLineEdit(central_widget)
        self.line_password.setPlaceholderText('пароль')
        self.line_password.setGeometry(250, 10, 113, 21)

        # Таблица 
        self.table_widget = QTableWidget(0, 3, central_widget)  
        self.table_widget.setGeometry(10, 40, 361, 192)
        self.table_widget.setHorizontalHeaderLabels(["Название", "Логин", "Пароль"])

        # Кнопка удаления
        self.button_delete = QPushButton("удалить", central_widget)
        self.button_delete.setGeometry(260, 230, 121, 32)
        
        # Кнопка для сохранения
        self.button_save = QPushButton('Сохранить', central_widget)
        self.button_save.setGeometry(160, 230, 113, 32)
        
        # Кнопка Показать
        self.button_add = QPushButton("Показать/Скрыть", central_widget)
        self.button_add.setGeometry(0, 230, 171, 32)

       

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
#остановился на проверке ввода на грамотное написание