import argparse
import src.lib.json_csv as json_csv
import src.lib.csv_xlsx as csv_xlsx

parser = argparse.ArgumentParser(description="Конвертация файлов")
subparser = parser.add_subparsers(dest="command", help="Команды")

json2csv_parser = subparser.add_parser("json2csv", help="Перевод из json в csv")
json2csv_parser.add_argument("--in", required=True, help="json файл")
json2csv_parser.add_argument("--out", required=True, help="csv файл")


csv2json_parser = subparser.add_parser("csv2json", help="Конвертация из csv в json")
csv2json_parser.add_argument("--in", required=True, help="csv файл")
csv2json_parser.add_argument("--out", required=True, help="json файл")

csv2xlsx_parser = subparser.add_parser("csv2xlsx", help="Конвертация из csv в xlsx")
csv2xlsx_parser.add_argument("--in", required=True, help="csv файл")
csv2xlsx_parser.add_argument("--out", required=True, help="xlsx файл")

args = parser.parse_args()

path_input = getattr(args, "in")
path_output = getattr(args, "out")

if args.command == "json2csv":
    json_csv.json_to_csv(path_input, path_output)
elif args.command == "csv2json":
    json_csv.csv_to_json(path_input, path_output)
elif args.command == "csv2xlsx":
    csv_xlsx.csv_to_xlsx(path_input, path_output)