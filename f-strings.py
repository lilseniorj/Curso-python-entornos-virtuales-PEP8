name = "Ana"
year = 2020
text = f"Hola {name}"
text2 = "Hola"
print(text)

text_calculo = f"Hola, {name} tu edad es: {2025 - year} años"
print(text_calculo)

text_func = f"HOLA {name.upper()}"
print(text_func)

edad = 17
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad: "
print(text_if)