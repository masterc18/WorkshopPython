"""Leer x cantidad de numeros reales y mostrar la raiz cuadrada de cada numero"""

from math import sqrt

cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))

for i in range(cantidad):
    numero = eval(input("Ingrese un número real: "))
    raiz_cuadrada = sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")