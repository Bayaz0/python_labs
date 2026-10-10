from ..lib.text import *

row = input("Введите строку: ")
row = normalize(row)
tokens = tokenize(row)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(set(tokens))}")
print("Топ-5: ")
d = count_freq(tokens)

text1 = "слово"
text2 = "частота"
print(f"{text1:<10} | {text2:<10}")
print("-" * 20)
for word, count in top_n(d):
    print(f"{word:<10} | {count:<10}")
