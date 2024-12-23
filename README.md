# manager_password

Приложение «Менеджер паролей» предназначено для хранения, управления и шифрования паролей пользователей. Приложение позволяет пользователю безопасно сохранять пароли для различных ресурсов и предоставляет возможность их просмотра, добавления, удаления и редактирования.

# Структура проекта

## 📂 Папка `data`

Папка `data` используется для хранения данных приложения. В текущей версии проекта она содержит:

- **`my_database.db`** — основной файл базы данных SQLite. В этом файле хранятся:
  - Названия ресурсов.
  - Логины и пароли пользователей.
  - Любая другая информация, необходимая для работы приложения.


## 📂 Папка `src`
папка `src` содержит исходный код приложения. Она содержит в себе файлы:

-**`main.py`** - основной файл приложения, который:
  - Создает главное окно программы
  - Подключает виджеты и элемнты интерфейса


-**`project.py`** - Файл, содержит:
  
  - Класс Ui_MainWindow для настройки главного окна приложения.
  - Описание всех виджетов, их расположения, размеров и свойств.


-**`Savebutton.py`** - Файл, содержащий класс SaveButton, реализующий функциональность кнопки “Сохранить”


-**`Deletebutton.py`** - Файл, содержащий класс SaveButton, реализующий функциональность кнопки “Удалить”

 
-**`Hidebutton.py`** - Файл, содержащий класс SaveButton, реализующий функциональность кнопки “Показать/Скрыть”


 **Примечание**: Для запуска работы приложения нужно использовать файл `main.py`