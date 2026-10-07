def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio = fio.split()
    if len(fio) == 0:
        raise ValueError("ValueError")
    fio_str = fio[0][0].upper() + fio[0][1:]
    if len(fio) == 2:
        fio_str += " " + fio[1][0].upper() + "."
    if len(fio) == 3:
        fio_str += " " + fio[1][0].upper() + "." + fio[2][0].upper() + "."
    if not group:
        raise ValueError("ValueError")
    group_str = "гр. " + group.strip()
    if gpa > 5.0 or gpa < 0.0:
        raise ValueError("ValueError")
    gpa_str = "GPA " + f"{gpa:.2f}"
    return ", ".join([fio_str, group_str, gpa_str]) 

def test_format_record():
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    try:
        print(format_record(("Иванов Иван Иванович", "BIVT-25", 7)))
    except ValueError as e:
        print(e)

test_format_record()
    