"""Diccionarios en python

diccionario 1"""

from os import system
# diccionario1 = {1, "Diego", 2, "Jose", 3, "Luis"}  # Forma1
# diccionario2 = dict(diego=1, Enrique=2, carlos=3, jose='gamer')  # Forma2
# print(diccionario1)
# print(diccionario2)


system("cls")
"""Dado un numero del 1 al 7, diga el dia de la semana que corresponde"""
# dias = {1:"Domingo", 2: "Lunes", 3:"Martes", 4:"Miercoles", 5:"Jueves", 6:"Viernes", 7:"sabado"}

# dia = int(input("Ingrese un numero del 1 al 7: "))

# print(dias[dia])
# #Actualizar un elemento o valor
# dias[1]= "Sunday"
# print(dias)
# #agregando un valor
# dias[8] = "Dia no existe"
# print(dias)
# #Eliminar valor
# dia = int(input("ingresa un numero del 1 al 7: "))
# del dias[dia]
# print(dias)
# ---------------------------------------------------------------------------------------------------------
# 1. Almacenar en un dicionario los nombres y notas de los alumnos
# 2. Imprimir los alumnos con sus respectivas notas
# 3 . Imprimir las notas mayor a 90

# datos = dict(carlos=86, diego=90, enrique=100, cesar=60, pedro=70)
# print(datos)

# for nombre, nota in datos.items():
#     print(f"Estudiante: {nombre:<10}", f"Nota: {nota:>3}", sep="-->")

# # for student in datos:
# #     print(student, datos[student])

# # for name, grade in datos.items():
# #     if grade > 60:
# #         print(name, grade)


# operadores en diccionarios
# product = {1: "Teclado", 2: "Mouse", 3: "Monitor", 4: "Grafica"}
# #Buscar producto

# #Uso de in
# # 1 esta en diccionario
# 1 in product
# # 5 esta en diccionario
# 5 in product

# #uso de not in
# 2 not in product
# 5 not in product

'''Almacenar productos con sus precios '''
productos = {}


def addProduct():
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingresar el precio: "))
    # Agregar elementos al diccionario por input
    productos[name] = price


def deleteProduct():
    name = input("Ingrese el nombre del producto: ")
    if name in productos:
        del productos[name]
    else:
        print("El producto no existe")


def showProduct():
    name = input("Ingrese el nombre del producto: ")
    if name in productos:
        print(f"El precio del producto es: {productos[name]}")


def showAllProducts():
    for name, price in productos.items():
        print(f"Producto: {name:<10}, precio: {price:>3}")


def menu():
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Mostrar Producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")
    op = int(input("Ingrese una opcion: "))
    return op


def main():
    while True:
        op = menu()
        if op == 1:
            addProduct()
            system("pause")
        elif op == 2:
            deleteProduct()
            system("pause")
        elif op == 3:
            showProduct()
            system("pause")
        elif op == 4:
            showAllProducts()
            system("pause")
        elif op == 5:
            break
        else:
            print("Opcion invalida")
            system("pause")


main()
