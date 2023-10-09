from os import system
#Ejemplo 1: Pilas con funciones
#Arreglo de numeros
#Mostrar los numeros pares
#Mostrar la suma de los impares
#Mostrar todo los elementos de la lista
#Buscar elemento
#Eliminar un valor
listNumber = []

def addNumber():
    num = int(input("Write a number: "))
    if isNumber(num):
        print(f"{num} ya esta registrado")
    else:
        listNumber.append(num)
    system("Pause")
    
def showPairs():
    system("cls")
    print("Lista de numeros pares")
    for number in listNumber:
        if(number%2==0):
            print(number)
    system("pause")

def plusUnPairs():
    suma = 0
    for number in listNumber:
        if number%2 != 0:
            suma+=number
    print(f"La suma de los impares es: {suma}")
    system("pause")

def showElements():
    print(listNumber)
    system("Pause")
    
def searchNumber(number):
    if number in listNumber:
        print(f"Se encontro: {number} en la lista")
    else:
        print(f"No se encontro {number} en la lista")

def deleteNumber(number):
    if(isNumber(number)):
        listNumber.remove(number)
        print(f"Se ha eliminado el numero {number}")
    else:
        print("El numero no existe")
        
def isNumber(number):
    return number in listNumber  


def menu():
    print("""1. Agregar
2. Mostrar Pares
3. Mostrar suma
4. Mostrar los elementos de la lista
5. Buscar numero
6. Eliminar
0. Salir""")
    op = int(input("Digite una opcion: "))
    if(op == 1):
        addNumber()
    elif op == 2:
        showPairs()
    elif op == 3:
        plusUnPairs()
    elif op == 4:
        showElements()
    elif op == 5 :
        number = int(input("Dime un numero "))
        searchNumber(number)
    elif op == 6:
        number = int(input("Dime el numero que quieres eliminar"))
        deleteNumber(number)
    elif op == 0:
        print("Adios...")
    else:
        print("Opcion invalida")
    return op

def main():
    option = -1
    system("cls")
    while option != 0:
        option = menu()
        
main()