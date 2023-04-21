import argparse
import json
import datetime

# Метод создания заметки, возращает словарь
def create_note(id):
    note_id = id
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": note_id, "title": title, "body": body, "date": date}

# Метод сохранения заметки, сохраняет в введенный файл
def save_notes(notes, filename):
    with open(filename, "w") as file:
        json.dump(notes, file)

# Метод загрузки заметок из файла, при отсутвии возращает пустой список
def load_notes(filename):
    try:
        with open(filename, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Метод удаления заметок, возвращает новый список без не нужной заметки
def delete_note_from_notes(notes, note_id):
    notes = [note for note in notes if note["id"] != note_id]
    return notes

# Метод изменения заметок, изменяет заметку если ид такой есть
def edit_note_in_notes(notes, note_id, title, body):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    
    return notes

# Метод вывода заметок на консоль
def print_notes(notes):
    if not notes:
        print("Заметок нет")
    for note in notes:
        print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Тело: {note["body"]}, Дата: {note["date"]}')

# Метод вывода заметок на консоль с фильтрацией по дате
def view_notes(notes, date=None):
    filtered_notes = [note for note in notes if note["date"][:10] == date]
    notes_to_display = filtered_notes

    if not notes_to_display:
        print("Заметок не найдено")
    else:
        for note in notes_to_display:
            print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Тело: {note["body"]}, Дата: {note["date"]}')

notes = []
i = 0
id = 0
while(i != 9):
    #Интерфейс пользователя
    print("-- Выберите опцию --")
    print("1. Загрузить заметки из файла notes.json")
    print("2. Создать заметку")
    print("3. Посмотреть заметку по id")
    print("4. Посмотреть все заметки")
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("7. Сохранить заметки в файл")
    print("8. Посмотреть заметки по дате")
    print("9. Выйти из программы")
    #Проверка правильности ввода
    try:
        i = int(input())
        if i < 1 or i > 9:
            raise ValueError
    except:
        print("Вы ввели некорректное значение. Введите одну цифру между 1-9")
    if i == 1:
        if notes:
            print("У вас есть не сохраненные заметки. Они будут потеряны при загрузке из файла.")
            b = input("Хотите продолжить? Введите (Да) или (Нет): ")
            if b == "Да":
                notes = load_notes("notes.json")
                print("Файл успешно загружен")
                if not notes:
                    print("Файла notes.json не существует")
            else:
                continue        
        else:
            notes = load_notes("notes.json")
            print("Файл успешно загружен")
            if not notes:
                print("Файла notes.json не существует")
    elif i == 2:
        if notes:
            last = notes[-1]
            id = last["id"]
        id += 1
        note = create_note(id)
        notes.append(note)
    elif i == 3:
        try:
            id_n = int(input("Введите id заметки: "))
            if id_n in [note["id"] for note in notes]:
                for note in notes:
                    if note["id"] == id_n:
                        print(f'ID: {note["id"]}')
                        print(f'Заголовок: {note["title"]}')
                        print(f'Тело: {note["body"]}')
                        print(f'Дата: {note["date"]}') 
            else:
                print("Заметки с таким id не существует")
        except:
            print("Вы ввели некорректное значение. Введите цифру")
    elif i == 4:
        print_notes(notes)
    elif i == 5:
        try:
            id_n = int(input("Введите id заметки: "))
            if id_n in [note["id"] for note in notes]:
                title = input("Введите заголовок заметки: ")
                body = input("Введите текст заметки: ")
                edit_note_in_notes(notes, id_n, title, body)
                print("Заметка изменена")
            else:
                print("Заметки с таким id не существует")
        except:
            print("Вы ввели некорректное значение. Введите цифру")
    elif i == 6:
        try:
            id_n = int(input("Введите id заметки: "))
            if id_n in [note["id"] for note in notes]:
                notes = delete_note_from_notes(notes, id_n)
                print("Заметка удалена")
            else:
                print("Заметки с таким id не существует")
        except:
            print("Вы ввели некорректное значение. Введите цифру")
    elif i == 7:
        save_notes(notes, "notes.json")
        print("Заметки сохранены в файл notes.json")
    elif i == 8:
        date = input("Введите дату (формат ГГГГ-ММ-ДД): ")
        view_notes(notes, date)
    elif i == 9:
        if notes != load_notes("notes.json"):
            print("У вас есть не сохраненные заметки. Продолжить?")
            b = input("Введите (Да) или (Нет): ")
            if b == "Нет":
                i = 0
            else:
                continue