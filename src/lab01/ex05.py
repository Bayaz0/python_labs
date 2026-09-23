str = input("ФИО: ")
str = str.strip()
full_name = str.split()
surname = full_name[0]
name = full_name[1]
father_name = full_name[2]
print(f"Инициалы: {surname[0]}{name[0]}{father_name[0]}.")
new_str =" ".join(full_name)
print(f"Длина (символов): {len(new_str)}")


