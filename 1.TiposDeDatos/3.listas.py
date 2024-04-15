
lista_numeros = [31, 24, 1, 52, 973, 78, 6, 10]
lista_numeros2 = [452123, 7852]
lista_nombres = ["Juan", "Maria", "Dario", "Karem"]

# *** SLICING con Listas ***
print(lista_numeros[1])
print(lista_numeros[:3])
print(lista_numeros[0:7:2])

# Concatenar 2 listas
nueva_lista_numeros = lista_numeros + lista_numeros2
print(nueva_lista_numeros)

# *** MÉTODOS PARA LISTAS ***
lista_nombres.append("Pedro") # Añadir nuevo nombre al final de la lista
print(lista_nombres)

lista_nombres.remove("Maria") # Quitar un elemento especìfico de la lista
print(lista_nombres)

lista_nombres.insert(0, "Eduardo") # Añadir un elemento al inicio de la lista
print(lista_nombres)

lista_nombres.pop()  # Quitar el elemento final de la lista
print(lista_nombres)

lista_numeros.sort() # Ordenar la lista
print(lista_numeros)

lista_numeros.reverse() # Invertir el orden de la lista
print(lista_numeros)

lista_nombres.clear() # Limpiar la lista
print(lista_nombres)

