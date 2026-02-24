a = 0
b = 0

try:
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))
    resultado = a / b
    print(f"El resultado: {resultado}")
except ValueError:
    print("El valor que digitó no es un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Print con finally")

print("Este es otro print")