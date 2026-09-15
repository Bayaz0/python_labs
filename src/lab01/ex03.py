price = float(input("price="))
discount = float(input("discount="))
vat = float(input("vat="))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:>10.2f} Р")
print(f"НДС:               {vat_amount:>10.2f} Р")
print(f"Итого к оплате:    {total:>10.2f} Р")

