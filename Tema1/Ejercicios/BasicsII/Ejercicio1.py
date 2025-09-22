# Crear dos variables numéricas
num_int = 5
num_float = 3.2

# Comprobar sus tipos
print(type(num_int))    # <class 'int'>
print(type(num_float))  # <class 'float'>

# Sumarlas en otra nueva
suma = num_int + num_float

# ¿De qué tipo es la nueva variable?
print(type(suma))       # <class 'float'>

# Eliminar las variables creadas
del num_int
del num_float
del suma
'''
print(num_int)  # NameError: name 'num_int' is not defined
print(num_float)  # NameError: name 'num_float' is not defined          
print(suma)  # NameError: name 'suma' is not defined
# Las variables han sido eliminadas y ya no existen
'''