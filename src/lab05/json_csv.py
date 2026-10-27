import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл json не найден {json_path}")
    except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Неверная кодировка при чтении: {json_path}")

    #Если файл пуст
    if not data:
        raise ValueError(f"Файл json {json_path} пуст")

    
    #файл содержит один словарь
    if isinstance(data, dict):
       data = [data]

    #проверка содержимого файла
    if not isinstance(data, list):
        raise ValueError("Файл содержит не подходящие данные")

    #все элементы списка - словарь?
    for x in data:
        if not isinstance(x, dict):
             raise ValueError("Файл содержит не подходящие данные")

    #список словарей
    header = []
    for d in data:
        for key in d.keys():
            if key not in header:
                header.append(key)
    
    with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, restval="")
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    try:
        with open(csv_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл csv не найден {csv_path}")
    except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Неверная кодировка при чтении: {csv_path}")

    #Если файл пуст
    if not data:
        raise ValueError(f"Файл json {csv_path} пуст")
    
    try:
        with open(json_path, "w", encoding="utf-8") as jsonfile:
           json.dump(data, jsonfile, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл json не найден {json_path}")
    except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Неверная кодировка при чтении: {json_path}")

    
    

if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people.csv")
    csv_to_json("data/samples/cities.csv", "data/out/cities.json")