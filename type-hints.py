"""Typing con Python"""

variable = 42 # int
print(f"variable: {variable}, del tipo: {type(variable)}")

variable = "" # str
print(f"variable: {variable}, del tipo: {type(variable)}")

otra_variable: int = 44
print(f"variable: {otra_variable}, del tipo: {type(otra_variable)}")

otra_variable: str = ""

user_id: int | None = None


# variable = valor
# variable: tipo = valor

def suma_clara (a: int,b: int) -> int:
  return a + b


articles: list[dict] = [
  {"title": "expample"},
  {"title": "example2"},
]

articles_dos: list[list[str]] = [
  ["title", "expample"],
  ["title", "example2"],
]

from typing import Any

articles_tre: list[list[Any]] = [
  ["title", "expample", 123],
  ["title", "example2"],
]

#int, str, list, dict, tuple. Any