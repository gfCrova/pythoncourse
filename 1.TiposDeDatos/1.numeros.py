

# NUMEROS 

edad = 20   #-> Entero
CASA = 4593  # -> Entero guardado en una Constante
precio_pan = 204.5 # -> Float

n_Imaginario = 2 + 2j # -> Imaginario
print(n_Imaginario)
print(2 ** 4) # Elevado a la potencia **
print((14000 // precio_pan) + (edad*CASA)) # // Division sin decimales


def calcular(num, elevar):
    """Function printing python version."""
    elev=num**elevar
    #El método f-strings usa literales para contatenar
    texto = f"El numero {num} elevado a la {elevar} da como resultado: {elev}"
    print(texto)


calcular(5, 3)
calcular(6, 2)
calcular(10, 5)
