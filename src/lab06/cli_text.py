import argparse
import src.lib.text as text

parser = argparse.ArgumentParser(description="Прога")
subparsers = parser.add_subparsers(dest="command")
#команда
stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
#ее аргументы
stats_parser.add_argument("--input", required=True, help="Текст")
stats_parser.add_argument("--top", type=int, default=5, help="Топ слов")

cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла построчно")
cat_parser.add_argument("--input", required=True, help="Путь к файлу")
cat_parser.add_argument("-n", action="store_true", help="Нумерация строк")
args = parser.parse_args()

if args.command == "stats":
    row = args.input
    row = text.normalize(row)
    tokens = text.tokenize(row)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")

    data = text.count_freq(tokens)
    print(f"Топ-{args.top}: ")
    text1 = "слово"
    text2 = "частота"
    print(f"{text1:<10} | {text2:<10}")
    print("-" * 20)
    for word, count in text.top_n(data, n=args.top):
        print(f"{word:<10} | {count:<10}")

if args.command == "cat":
    path = args.input
    try:
        with open(path, mode="r", encoding="utf-8", newline="") as f:
            text = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Такого файла нет: {path}")
    except UnicodeDecodeError:
         raise UnicodeDecodeError(f"Неверная кодировка при чтении: {path}")
    if args.n:
        i = 1
        for row in text:
            print(f"{i}. {row}", end="")
            i = i + 1
    else:
        for row in text:
            print(row, end="")