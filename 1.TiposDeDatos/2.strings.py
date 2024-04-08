nombre_curso = "Python desde 0"

descripcion_curso = """
Este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador.
"""

print(nombre_curso + "\n" + descripcion_curso)

# Longitud total del texto
print(len(descripcion_curso))

# ***SLICING***
# 1- Cortar el texto desde la pos:6 hasta la pos:21
# 2- Cortar el texto desde la pos40: hasta el final del texto
# 3- Cortar el texto desde el inicio hasta la pos:12
# 4- Cortar el texto desde la pos:0 hasta la pos:4 cada 2 caracteres

print(descripcion_curso[6:21])
print(descripcion_curso[40:])
print(descripcion_curso[:12])
print(nombre_curso[0:10:2])
