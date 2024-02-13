# Импорт библиотек и модулей: Мы начинаем с импорта необходимых модулей Python, таких как `json`,
# `os` для работы с файлами и `datetime` для работы с датами и временем.

# Класс NotesApp: Мы создаем класс `NotesApp`, который будет управлять нашим приложением для работы с заметками.
# Он содержит методы для добавления, просмотра, редактирования и удаления заметок, а также методы для загрузки
# и сохранения заметок из/в файл.

# Методы класса NotesApp:
#    - `load_notes()`: Этот метод загружает заметки из файла JSON, если файл существует.
#    - `save_notes()`: Этот метод сохраняет текущий список заметок в файл JSON.
#    - `add_note()`: Метод для добавления новой заметки. Он создает словарь с данными о заметке, добавляет его в список заметок, сохраняет список в файл и выводит сообщение об успешном добавлении.
#    - `list_notes()`: Метод для вывода списка всех заметок.
#    - `read_note_by_id()`: Метод для чтения заметки по ее ID.
#    - `edit_note_by_id()`: Метод для редактирования заметки по ее ID.
#    - `delete_note_by_id()`: Метод для удаления заметки по ее ID.

# Основной блок кода: В основном блоке кода мы создаем экземпляр класса `NotesApp` и запускаем бесконечный цикл,
# в котором пользователь может выбирать различные команды для работы с заметками: добавление, просмотр,
# редактирование, удаление и выход из приложения.

import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, message):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'message': message,
            'timestamp': str(datetime.now())
        }
        self.notes.append(note)
        self.save_notes()
        print(f'Заметка успешно добавлена: {note}')

    def list_notes(self):
        if not self.notes:
            print('Нет доступных заметок.')
            return

        print('Список заметок:')
        for note in self.notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время: {note['timestamp']}")

    def read_note_by_id(self, note_id):
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['message']}, Дата/время: {note['timestamp']}")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def edit_note_by_id(self, note_id, new_title, new_message):
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            note['title'] = new_title
            note['message'] = new_message
            note['timestamp'] = str(datetime.now())
            self.save_notes()
            print(f"Заметка с ID {note_id} успешно отредактирована.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def delete_note_by_id(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()
        print(f"Заметка с ID {note_id} успешно удалена.")

if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nВыберите команду:")
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Прочитать заметку по ID")
        print("4. Редактировать заметку по ID")
        print("5. Удалить заметку по ID")
        print("6. Выйти")

        choice = input("Введите номер команды: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            app.add_note(title, message)
        elif choice == '2':
            app.list_notes()
        elif choice == '3':
            note_id = int(input("Введите ID заметки для чтения: "))
            app.read_note_by_id(note_id)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            app.edit_note_by_id(note_id, new_title, new_message)
        elif choice == '5':
            note_id = int(input("Введите ID заметки для удаления: "))
            app.delete_note_by_id(note_id)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректная команда. Пожалуйста, выберите существующую команду.")