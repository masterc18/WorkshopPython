import clases as c
from os import system
listPerson = list()

# Agregar elementos
def addPerson():
    fName = input("Ingrese el primer nombre: ")
    sName = input("Ingrese el segundo nombre: ")
    birth = int(input("Ingrese la fecha de nacimiento: "))
    person = c.Person(fName, sName, birth)
    listPerson.append(person)

# Mostrar los elementos
def showAll():
    for person in listPerson:
        print(f"Primer Nombre: {person.Firstname}")
        print(f"Segundo Nombre: {person.Secondname}")
        print(f"Edad: {person.getAge()}")
        print(f"Email: {person.getEmail()}")
        print(f"La persona es: {person.isOlder()}")

def main():
    while True:
        system("cls")
        print("1. Agregar persona")
        print("2. Mostrar persona")
        print("3. Salir")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            addPerson()
            system("pause")
        elif op == 2:
            showAll()
            system("pause")
        elif op == 3:
            print("Adios....")
            system("pause")
        else:
            print("Opcion invalida")
            
main()
