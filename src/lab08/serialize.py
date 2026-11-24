import json
from src.lab08.models import student_from_dict, format_student

def students_to_json(students : list[dict], path):
    """
    Сохраняет список записей в JSON: массив объектов, ensure_ascii=False, indent=2.
    """
    try:
        with open(path, "w",encoding="utf-8", newline='') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл json не найден {path}")
    except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Неверная кодировка при чтении: {path}")

def students_from_json(path) -> list[dict]:
    """
    читает JSON-массив
    каждую запись прогоняет через student_from_dict
    при битой записи — одна из двух политик, выбранную описать в README:
    strict: первая же ошибка → ValueError с номером записи и причиной
    skip: битые записи пропускаются, в конце в консоль — сколько пропущено и почему
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл json не найден {path}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Неверная кодировка при чтении: {path}")
    if not isinstance(data, list):
        raise ValueError(f"Файл содержит невалидные данные")
    students = list()
    try:
        for i, rec in enumerate(data):
            students.append(student_from_dict(rec))
    except ValueError as e:
        raise ValueError(f"Ошибка: {e}; \nЭлемент {i}: {rec}")
    return students

if __name__ == "__main__":
    students = [
    {"fio": "Иванов А В", "birthdate": "2006-03-14", "group": "БИВТ-26-6-1", "gpa": 4.5},
    {"fio": "Смирнова Е Д", "birthdate": "2005-09-28", "group": "БИВТ-26-6-2", "gpa": 5},
    {"fio": "Кузнецов М С", "birthdate": "2006-12-05", "group": "БИВТ-26-6-1", "gpa": 3.8},
    {"fio": "Попова А И", "birthdate": "2005-07-19", "group": "БИВТ-26-6-3", "gpa": 4.2},
    {"fio": "Соколов Д О", "birthdate": "2006-01-30", "group": "БИВТ-26-6-2", "gpa": 4}
    ]
    students_to_json(students, "data/lab08/students_input.json")
    studets = students_from_json("data/lab08/students_input.json")
    for student in students:
        print(format_student(student))