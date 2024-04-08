
nombre_curso = "Python desde 0"

descripcion_curso = """
Este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador.
"""

print(nombre_curso + "\n" + descripcion_curso)

# Longitud total del texto
print(len(descripcion_curso))

# *** SLICING (Cortar el texto)***
# 1- Desde la pos: 6 hasta la pos: 21
# 2- Desde la pos: 40 hasta el final del texto
# 3- Desde el inicio hasta la pos: 12
# 4- Desde la pos: 0 hasta la pos: 4 cada 2 letras

print(descripcion_curso[6:21])
print(descripcion_curso[40:])
print(descripcion_curso[:12])
print(nombre_curso[0:10:2])

# *** MÈTODOS ***

saludo = '  hola mundo  '
print(saludo.upper())
print(saludo.lower())
print(saludo.capitalize())
print(saludo.title())
print(saludo.strip())
print(saludo.strip().capitalize())

print(saludo.split())
print(saludo.split('o'))

print(saludo.find('un'))

print(saludo.replace('hola', 'chau').strip())

# ***Modificar strings inmutables****
# Cambiar el nombre de usuario 'David' a 'Dario'

usuario = 'David' #usuario[2:] = 'rio' ---> Inmutable
usuarioEditado2 = usuario.replace(usuario[2:], 'rio')
print(f'Se modifico el nombre del usuario {usuario} a {usuarioEditado2}')

# Verificar (Boolean) si se encuentra o no, el string en la variable
print('un' in saludo)
print('un' not in saludo)
