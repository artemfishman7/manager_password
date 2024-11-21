from PyQt6.QtWidgets import QPushButton, QLineEdit

class HideButton(QPushButton):
    def __init__(self, passwords: QLineEdit):
        super().__init__()

        self.setText("Показать")
        self.passwords = passwords

        # установка скрытия символов
        self.passwords.setEchoMode(QLineEdit.EchoMode.Password)

        
        self.clicked.connect(self.button_hide)
# проверка режима отображения текста
    def button_hide(self):
        if self.passwords.echoMode() == QLineEdit.EchoMode.Password:
            # Показываем пароль
            self.passwords.setEchoMode(QLineEdit.EchoMode.Normal)
            self.setText("Скрыть")

        else:
            self.passwords.setEchoMode(QLineEdit.EchoMode.Password)
            self.setText('Показать')
        