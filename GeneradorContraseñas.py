import random
import string

contraseña = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print("Contraseña generada:", contraseña)

"""
"k" indica la longitud de la contraseña generada. 
Se puede cambiar este valor para generar contraseñas de diferentes longitudes.
"""