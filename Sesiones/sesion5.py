# #Uso de variables globales

# x = 5 #Variable global

# def modificar():
#     global x #Para poder cambiar la variable global
#     x = 3 #Se cambia el valor de la variable global
#     x = x+1
#     print(f"Estoy dentro de la funcio y x es igual a {x}")
    
# print(f"Valor de x antes de entrar a la funcion {x}")
# modificar()
# print(f"Valor despues de salir {x}")

#------------------------------------------------------------------------

#Uso de parametros

# import os
# os.system("cls")
# os.system("Color 02")

# def getFullName(firstName, secondName):
#     return f"{firstName} {secondName}"#Da el orden de las variables

# def main():
#     firstName = input("Write your name :")
#     secondName = input("Write your last name: ")
#     print(f"Your full name is: {getFullName(firstName, secondName)}")

# if __name__ == "__main__": #Llamar la funcion main
#     main()

#-------------------------------------------------------------------------

# """Introduccion a lista"""
# lista = list()
# print(lista)
# lista.append(1)
# print(lista)
# lista.append("Diego")
# print(lista)
# lista.append(99.99)
# print(lista)
# cont = 0
# #Imprimir lista con while
# while cont < len(lista):
#     print(cont, lista[cont])
#     cont += 1
# #Imprimir lista con for
# for item in lista:
#     print(item)
    
#-------------------------------------------------------------------------


