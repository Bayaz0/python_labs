from pathlib import Path
import sys
import csv
from src.lib.matrix import is_matrix

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Открыть файл на чтение в указанной кодировке 
            и вернуть содержимое как одну строку"""
    try:
        with open(path, mode="r", encoding=encoding) as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Такого файла нет: {path}")
    except UnicodeDecodeError:
         raise UnicodeDecodeError(f"Неверная кодировка при чтении: {path}")
    return text

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создать/перезаписать CSV с разделителем ,"""
    if not is_matrix(rows):
        raise ValueError("Строки разной длины")
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header:
           writer.writerow(header)
        writer.writerows(rows)
               
def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории,
      если их нет (для удобства перед записью)"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    
if __name__ == "__main__":
    #ensure_parent_dir("data/lab04/input.txt")
    assert(read_text("data/lab04/input.txt") == "")
    write_csv(list(), "data/lab04/check.csv", header=("a","b"))  # создаст CSV
