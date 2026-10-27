import csv
import openpyxl

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
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
    #data список словарей

    if not data:
        raise ValueError("Файл csv пуст {csv_path}")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(list(data[0].keys()))
    for d in data:
         ws.append(list(d.values()))

    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")