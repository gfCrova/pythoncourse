import math

# NUMEROS

num_entero = 20
print(num_entero)

# Reescribir la variable
num_entero += num_entero  # num_entero = num_entero + num_entero
print(num_entero)
num_entero *= num_entero  # num_entero = num_entero * num_entero
print(num_entero)
num_entero /= num_entero  # num_entero = num_entero / num_entero
print(num_entero)
num_entero -= num_entero  # num_entero = num_entero - num_entero
print(num_entero)

precio_pan = 204.53  # -> Float
print(14000 // precio_pan)  # Division sin decimales //
print(f'{(14000 / precio_pan):0.3f}')  # Redondear a 3 cifras significativas

num_Imaginario = 2 + 2j  # -> Imaginario
print(num_Imaginario)

num_ElevadoPotencia = 3 ** 4  # Elevado a la potencia **
print(num_ElevadoPotencia)


# *** MÉTODOS ***

print(round(43.3))  # Redondear el decimal 43.3 a su entero más cercano
print(abs(-77))  # Valor absoluto del numero
print(max(311, 24, -38, 5154, 63, 0.007, 865, 9, 102, 715))  # Valor máximo
print(min(311, 24, -38, 5154, 63, 0.007, 865, 9, 102, 715))  # Valor mínimo
# print(sum()) # Suma de todos los valores

# Biblioteca Math
print(math.ceil(1.154))  # Llevar al Entero Superiór más cercano
print(math.floor(1.999999))  # Llevar al Entero Inferiór más cercano
print(math.pow(10, 3))  # Elevar 10 a la 3
print(math.isnan(23))  # Verificar si el número es falso
print(math.isinf(23))  # Verificar si el número es infinito
print(math.isfinite(23))  # Verificar si el número es finito
print(math.pi)  # Valor de Pi
print(math.e)  # Valor de Euler
print(math.degrees(math.pi))  # Convertir de radianes a grados
print(math.radians(math.pi))  # Convertir de grados a radianes
print(math.sin(math.pi/2))  # Seno de Pi/2
print(math.cos(math.pi/2))  # Coseno de Pi/2
print(math.tan(math.pi/2))  # Tangente de Pi/2
print(math.asin(1))  # Arco seno
print(math.acos(1))  # Arco coseno
print(math.atan(1))  # Arco tangente
print(math.sinh(1))  # Seno hiperbólico
print(math.cosh(1))  # Coseno hiperbólico
print(math.tanh(1))  # Tangente hiperbólico
print(math.asinh(1))  # Arco seno hiperbólico
print(math.acosh(1))  # Arco coseno hiperbólico
print(math.exp(1))  # Exponencial
print(math.log(1))  # Logaritmo natural
print(math.log10(1))  # Logaritmo base 10
print(math.log2(1))  # Logaritmo base 2
print(math.log1p(1))  # Logaritmo base 10 + 1
print(math.sqrt(1))  # Raiz cuadrada
print(math.hypot(1, 1))  # Hipotenusa


# ***CALCULADORA BÀSICA****

n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa el segundo número: '))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
potencia = n1 ** n2
raiz_cuadrada = n1 ** 0.5

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es: {suma},
el resultado de la resta es: {resta},
el resultado de la multiplicación es: {multiplicacion},
el resultado de la división es: {division},
el resultado de la potencia es: {potencia},
el resultado de la raiz cuadrada es: {raiz_cuadrada},
"""

print(mensaje)
