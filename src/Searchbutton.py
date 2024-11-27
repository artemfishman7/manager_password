from PyQt6.QtWidgets import QPushButton, QTableWidgetItem

class SearchButton(QPushButton):
    def __init__(self, table_widget, search_button, cursor):
        super().__init__("Поиск")
        self.table_widget = table_widget
        self.search_button = search_button
        self.cursor = cursor

        self.clicked.connect(self.search_by_name)

    # метод фильстрации по названию
    def search_by_name(self):
        search_text = self.search_button.text()
        # проверка на заполненность 
        if search_text: 
            self.cursor.execute(
                'SELECT name, login, password FROM passwords WHERE name LIKE ?', 
                (f"%{search_text}%",)
            )
            rows = self.cursor.fetchall() # получение всех записей найденные запросом
            self.update_table(rows)
        else:
            self.search_button.setPlaceholderText("Введите название!")

    def update_table(self, rows):
        # обновление записей таблицы
        self.table_widget.setRowCount(0)  # очистка таблицы

        for row in rows:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position) # добабвление новых строк

            for column, item in enumerate(row):
                self.table_widget.setItem(row_position, column, QTableWidgetItem(item))