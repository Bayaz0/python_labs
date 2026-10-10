from re import findall

#нормализация
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    copy_text = text
    if casefold == True:
        copy_text = copy_text.casefold()
    if  yo2e == True:
        copy_text = copy_text.replace("ё", "е").replace("Ё", "Е")
    return " ".join(copy_text.split())

#из строки в список слов по шаблону
def tokenize(text: str) -> list[str]:
    template = r"\w+(?:-\w+)*"
    return findall(template, text)

#счетчик слов
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = dict()
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

#сортировка счеткика слов
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_freq = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return sorted_freq[0:n]

if __name__ == "__main__":

    def test_normalize():
        print(normalize("ПрИвЕт\nМИр\t"))
        print(normalize("ёжик, Ёлка", yo2e=True))
        print(normalize("Hello\r\nWorld"))
        print(normalize("  двойные   пробелы  "))

    def test_tokenize():
        print(tokenize("привет мир"))
        print(tokenize("hello,world!!!"))
        print(tokenize("по-настоящему круто"))
        print(tokenize("2025 год"))
        print(tokenize("emoji 😀 не слово"))

    def test_freq():
        print(count_freq(["a","b","a","c","b","a"]))
        print(top_n(count_freq(["a","b","a","c","b","a"]), n=2))
        print("\n")
        print(count_freq(["bb","aa","bb","aa","cc"]))
        print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2))

    
    test_normalize()
    test_tokenize()
    test_freq()
