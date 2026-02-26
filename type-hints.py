"""Typing con Python"""

variable = 42 # int
print(f"variable: {variable}, del tipo: {type(variable)}")

variable = "Texto de prueba" # str
print(f"variable: {variable}, del tipo: {type(variable)}")

otra_variable: int = 44
print(f"variable: {otra_variable}, del tipo: {type(otra_variable)}")

otra_variable = ""

user_id: int | None = None


# variable = valor
# variable: tipo = valor

