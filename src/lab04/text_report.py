from src.lib.text import *
from src.lab04.io_txt_csv import *

path = "data/lab04/input.txt"
text = read_text(path, encoding="cp1251")
text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
freq_n = top_n(freq, len(freq))
write_csv(freq_n, "data/lab04/out.csv", header=("word", "count"))

#Вывод в консоль
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5: ")
text1 = "word"
text2 = "count"
print(f"{text1:<10} | {text2:<10}")
print("-" * 20)
for word, count in freq_n[:5]:
    print(f"{word:<10} | {count:<10}")
