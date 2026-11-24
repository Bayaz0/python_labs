"""
модель Student 
поля (ключи словаря):
fio
birthdate
group
gpa
валидацию:
набора ключей (ровно STUDENT_FIELDS, ничего лишнего и ничего пропущенного)
формата даты (YYYY-MM-DD) и её существования (2003-02-30 — не дата)
диапазона среднего балла 0 ≤ gpa ≤ 5

Валидация:
fio и group — строки, после strip() непустые
birthdate — строка, date.fromisoformat её разбирает, дата не в будущем
gpa — число (int или float, не bool), 0 <= gpa <= 5
в validate_student дополнительно: set(rec) == set(STUDENT_FIELDS)
"""

from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

def make_student(fio, birthdate, group, gpa) -> dict:
    """
    Конструктор
    """
    #Валидация данных
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError(f"неверно указано ФИО: {fio}")
    fio = fio.strip()
    if not isinstance(group, str) or not group.strip():
        raise ValueError(f"неверно указано group: {group}")
    group = group.strip()

    if isinstance(birthdate, str):
        if len(birthdate) != 10:
            raise ValueError(f"Неверный формат даты {birthdate}")
    if not isinstance(birthdate, str):
        raise ValueError(f"неверно указано birthdate: {birthdate}")
    birthdate = date.fromisoformat(birthdate)
    if birthdate > date.today():
        raise ValueError(f"неверно указано birthdate: {birthdate.isoformat()}")

    
    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise ValueError(f"неверно указано gpa: {gpa}")
    #защита от NaN
    if not (0 <= gpa <= 5):
        raise ValueError(f"неверно указано gpa: {gpa}")
    
    return {"fio": fio, "birthdate": birthdate.isoformat(), "group": group, "gpa": gpa}
    
def validate_student(rec: dict) -> None:
    """
    проверяет готовый словарь: набор ключей и значения; 
    при ошибке — ValueError
    """
    if not isinstance(rec, dict):
        raise ValueError(f"Это не словарь {rec}")
    if set(rec) != set(STUDENT_FIELDS):
        raise ValueError(f"Неверный список ключей: {set(rec)}")
    copy_rec = make_student(rec["fio"], rec["birthdate"], rec["group"], rec["gpa"])
    if copy_rec != rec:
        raise ValueError(f"Словарь {rec} содержит неподходящие данные")

def student_age(rec: dict, today=None) -> int:
    """
    полных лет на дату today (по умолчанию date.today());
    человек, родившийся 2007-09-20, 2008-09-19
    на 2026-09-19 ещё не отметил день рождения
    2007-09-20, 2008-09-19 - меньше года 0 > -1
    2007-09-20, 2008-09-20 - ровно год 1 = -0
    2007-09-20, 2008-09-21 - больше года 1 < -0
    2007-09-20, 2008-12-30 - больше года 1 < -0
    2007-09-20, 2009-03-20 - больше года 1 > -1
    2007-09-20, 2009-09-19 - меншье 2 лет 1 > -1
    2007-09-20, 2009-09-20 - ровно 2 = -0
    """
    if today is None:
        today = date.today()
    else:
        if not isinstance(today, date):
            today = date.fromisoformat(today)
    birthday = date.fromisoformat(rec["birthdate"])
    diff_years = today.year - birthday.year
    if (birthday.month, birthday.day) > (today.month, today.day):
        diff_years -= 1
    return diff_years

def format_student(rec: dict) -> str:
    """
    красивый вывод: Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30
    """
    fio = rec["fio"]
    age = student_age(rec)
    group = rec["group"]
    gpa = rec["gpa"]
    return f"{fio:<13} | {group:<10} | {age:<2} | GPA {gpa:<4}"

def student_to_dict(rec: dict) -> dict:
    """
    копия записи (не та же самая!) для сериализации
    """
    copy_rec = dict(rec)
    return copy_rec

def student_from_dict(d: dict) -> dict:
    """
    десериализация: взять из словаря ровно нужные ключи, привести gpa к float, провалидировать
    """
    if not isinstance(d, dict):
        raise TypeError(f"Неверный тип аргумента {type(d)}")
    # является ли подмножеством
    if not set(STUDENT_FIELDS) <= set(d):
        raise ValueError(f"Неподходящий набор ключей")
    try:
        gpa = float(d["gpa"])
    except TypeError:
        raise ValueError(f"Неверный тип данных gpa {d["gpa"]}")
    rec = make_student(d["fio"], d["birthdate"], d["group"], gpa)
    return rec

if __name__ == "__main__":
    bad_student = {"fio": "Иванов Иван Иванович","group": "БИВТ-26-6-1", "gpa": 2}
    print(student_from_dict(bad_student))
    
    #assert student_age(pupil, "2008-09-20") == 0, f"{student_age(pupil, "2008-09-20")}"
    #bad_pupil = {"fio": "С С Макс", "birthdate": "20051120", "group": "БИВТ-26-6-1", "gpa": 3}
    #validate_student(bad_pupil)
    #copy_pupil = student_to_dict(pupil)
    #copy_pupil["gpa"] = 3
    #print(format_student(student_to_dict(pupil)))
    #print(format_student(student_to_dict(copy_pupil)))