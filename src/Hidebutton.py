from PyQt6.QtWidgets import QPushButton, QLineEdit


# класс кнопки для скрытия/показа пароля
class HideButton(QPushButton):

    def __init__(self, passwords: QLineEdit):
        super().__init__()

        self.setText("Показать")
        self.passwords = passwords

        # Установка скрытия символов по умолчанию
        self.passwords.setEchoMode(QLineEdit.EchoMode.Password)

        # Привязка  к кнопке
        self.clicked.connect(self.toggle_password_visibility)

    def toggle_password_visibility(self):
        if self.passwords.echoMode() == QLineEdit.EchoMode.Password:
            # Показ пароля
            self.passwords.setEchoMode(QLineEdit.EchoMode.Normal)
            self.setText("Скрыть")
        else:
            # Скрытие пароля
            self.passwords.setEchoMode(QLineEdit.EchoMode.Password)
            self.setText("Показать")