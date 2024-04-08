
"""Los siguientes valores que tienen un nùmero fijo se 
consideran constantes y se encriben en mayùsculas"""

# Enteros
edad = 20
numero_de_casa = 4593

# Float
harina_precio = 204.5
yerba_precio = 99.87

# Elevado a la potencia **
g = 4
resultado = g ** 4
print(resultado)

print(((harina_precio + yerba_precio) + (edad*numero_de_casa)) / resultado)


def calcular(num, elevar):
    """Function printing python version."""
    elev=num**elevar
    #El método f-strings para contatenar cualquier cosa
    texto = f"El numero {num} elevado a la {elevar} da como resultado: {elev}"
    print(texto)


calcular(5, 3)
calcular(6, 2)
calcular(10, 5)
