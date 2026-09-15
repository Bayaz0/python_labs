min = int(input("Минуты: "))
MIN_PER_HOUR = 60
print(f"{min // MIN_PER_HOUR}:{(min % MIN_PER_HOUR):02d}")