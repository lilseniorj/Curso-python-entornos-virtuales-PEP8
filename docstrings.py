"""
Explicación de docstrings en Python.

En esta clase puedo explicar cómo son los docstrings en Python

"""

def ejemplo_sin_docstring():
  return "Hola Mundo!"

def ejemplo_con_docstring() -> str:
  """
  Descripcion
  Args
  Returns
  Exceptions
  Examples
  """
  return "Hola Mundo!"

# print(ejemplo_con_docstring.__doc__)
help(ejemplo_con_docstring)