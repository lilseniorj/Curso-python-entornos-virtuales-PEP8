name = "Ana"
year = 2020
text = f"Hola {name}"
text2 = "Hola"
# print(text)

text_calculo = f"Hola, {name} tu edad es: {2025 - year} años"
# print(text_calculo)

text_func = f"HOLA {name.upper()}"
# print(text_func)

edad = 17
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad: "
# print(text_if)


bank_balance = 1300000
text = f"Tu saldo bancario es: {bank_balance:,}"
print(text)

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.1f}"
print(text)

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.2f}"
print(text)

user_id = 1000
text = f"Su ID de usuario es: {user_id:5d}"
print(text)


product = "Laptop"
price = 999

text = f"Product: {product:<15} | Price: ${price:>10}"
print(f"{text}\n{text}")


from datetime import datetime

date = datetime(2024, 12, 5, 20, 10)
text = f"La fecha completa es {date: %Y-%m-%d %H:%M}"
print(text)

