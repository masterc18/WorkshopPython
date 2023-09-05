# Ejemplo 1

import os
import math
from math import pi, sqrt  # : To import specific funtions
from math import *  # to import everything



def Raiz(num):
    return sqrt(num)


def Cubo(num):
    return pow(num, 3)


def calccircule(r):
    return round(pi * pow(r, 2), 4)


def menu():
    # the best way to write a menu
    op = 0
    while op != 4:
        
        msn = """1. Calcular elarea de un circulo
2. Calcular el cubo de un numero
3. calcular la raiz cuadrada de un numero
4.salir
Digita tu opcion"""
        print(msn)
        op = int(input())
        if op == 1:
            r = float(input("Tell me the radio: "))
            print(f"The area is {calccircule(r)}")
            
        elif op == 2:
            num = int(input("Write a number: "))
            print(f"The result is {Cubo(num)}")
            
        elif op == 3:
            num = int(input("Write a number : "))
            print(f"The result is {Raiz(num)}")
            
        elif op == 4:
            print("Good bye")
           
        else:
            print("error")
        os.system("pause")


def main():
    print("Este es la funcion principal")
    menu()


main()
