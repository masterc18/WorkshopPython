#copiar lista
from os import system
# lista1 = list()
# lista2 = list()

# lista1.append("Diego")
# lista1.append("Carlos")
# lista1.append("Maria")
# lista1.append("Xochlilt")
# lista1.append("Carolina")

system("cls")
# print(lista1)
# lista2.append("Fernando")
# print(lista2)
# lista3 = list()
# lista3 = lista1#Toma los valores de lista1 y los comparte o copia en lista3
# print(lista3)

# print("Agregar managua")
# lista1.append("Managua")
# print(lista1)

# print("Agregar Granada a la lista 3")
# lista3.append("Granada")
# print("Imprimir listas")
# print(f"Lista 3 = {lista3}")
# print(f"Lista 1 = {lista1}")
# print(f"Lista 2 = {lista2}")

# lista1 = lista2
# lista2.append(150)
# lista3.append("Carro")
# print("Nuevos valores")
# print(f"Lista 3 = {lista3}")
# print(f"Lista 1 = {lista1}")
# print(f"Lista 2 = {lista2}")

# print(type(lista1))
# print(type(lista2))
# print(type(lista3))
#=======================================================================
#Forma con funcion
# fruits = list()
# fruits.append("Mandarina")
# fruits.append("Sandia")
# fruits.append("Limon")
# fruits.append("Naranja")
# fruits.append("Manzana")

# x = fruits.copy()
# print(x)

# fruits.append("Mango")

# print(f"Lista de frutas: {fruits}")
# print(f"Lista de X: {x}")
#=========================================================================
#pilas

# miPila = list()

# def apilar(nombre):
#     miPila.append(nombre)

# def desapilar():
#     return miPila.pop()

# apilar("Sofia del Sofia de los Presagios")
# apilar("Historia de una muerte anunciada")
# apilar("El principito")
# apilar("Cien year de soledad")
# apilar("El alquimista")
# apilar("Romeo y Julieta")
# apilar("Azul")
# apilar("La metarmorfosis")
# apilar("Genesis")
# apilar("JOB")

# cont = len(miPila)
# while cont > 0:
#     print(desapilar())
#     cont-=1
#===========================================================================
#Matrices

matriz = [[2,30],
          [5,6000]]

for fila in matriz:
    for coulmna in fila:
        print(f"{coulmna:>9}", end="")
    print("="*18)