#Ejemplo 1
"""Leet un nombre y mostrarlo en mayuscula"""
# import os
# os.system("cls")
# vocals = ['a','e','i','o','u']
# name = input("Write your name: ")
# print(f"Your name in high leter is {name.upper()}")
# print(f"Ypur name in short letter is {name.lower()}")
# print(f"Ypur name with the first high first letter is {name.capitalize()}")
# print(f"Removing spaces {name.strip()}.")
# print(f"Replace {name.replace(' ',' ')}")
# #Para cambiar letra por letra
# cont = 0
# newName = ""
# while cont < len(name):
#     if(cont == 0):
#         newName = name.replace('a','*')
#         newName = name.replace('e','*')
#         newName = name.replace('i','*')
#         newName = name.replace('o','*')
#         newName = name.replace('u','*')
#         cont+=1

# print(f"Your new name is {newName}")
#-----------------------------------------------------------------------
# """Leer x cantidad de numeros e imprimirlos de forma ordenada"""
# numbers = list()

# op = 'si'
# while (op.upper() != 'NO'):
#     num = int(input("Write a number: "))
#     numbers.append(num)
#     op = input("You want add another: ")
    
# #funcion para odernar
# numbers.sort()

# print(numbers)
# #Funcion para revertir el orden
# numbers.sort(reverse=True)
# print(numbers)
#-------------------------------------------------------------------------
"""Leer nombres, ordenarlos alfabeticamente"""
# names = list()

# op = 'si'
# while (op.upper() != 'NO'):
#     name = input("Write the name: ")
#     names.append(name.upper())
#     op = input("Do you want to add another: ")

# names.sort()
# print(f"Your name in alphabetic order {name}")

# names.sort(reverse=True)
# print(f"Your name in descendent order {name}")
#-----------------------------------------------------------------------
#Leer un palabra o frase y ocultar las vocales: minusculas, mayusculas, aceptuadas y no acentuadas.
from os import system

system("cls")
system("Color A1")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó', 'ú']
name = input("Dime una palabra o frase: ")
newName = name
for vocal in vocales:
    newName = newName.replace(vocal, '*')

print(newName)