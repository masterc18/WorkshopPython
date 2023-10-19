from clases import Student
from os import system
import random
students = dict()

def addStudent():
    id = random.randint(100, 999)
    name = input("Nombre: ")
    email = input("Email: ")
    carrer = input("Carrera: ")
    avg = int(input("Promedio: "))
    price = int(input("Precio: "))
    student = Student(name, email, carrer, avg, price)
    students[id] = student #Dato principal es el id pero puede ser cambiado por ejemplo
    #students[name] = student


def isStudent(id):
    return id in students


def deleteStudent():
    id = int(input("Escribe el id del estudiante a eliminar: "))
    if (isStudent(id)):
        del students[id]
    else:
        print("El estudiante no existe en el registro")


def updateStudent():
    id = int(input("Escribe el id del estudiante: "))
    if (isStudent(id)):
        print("Que datos desea actualizar o cambiar?")
        print("1. Nombre")
        print("2. Email")
        print("3. Carrera")
        print("4. Promedio")
        print("5. Precio de la carrera")
        print("6. Salir")
        op = int(input("Digite una opcion: "))
        if op == 1:
            newName = input("Escriba el nuevo nombre del estudiante: ")
            students[id].name = newName
        elif op == 2:
            newEmail = input("Escriba el nuevo email del estudiante: ")
            students[id].email = newEmail
        elif op == 3:
            newCarrer = input('Escriba el nombre del nueva carrera: ')
            students[id].carrer = newCarrer
        elif op == 4:
            newAvg = int(input("Escriba el nuevo promedio: "))
            students[id].avg = newAvg
        elif op == 5:
            newPrice = int(input("Escribe el nuevo precio de la carrera: "))
            students[id].price = newPrice
        elif op == 6:
            print("Saliendo.......")


def showStudents():
    for key, value in students.items():
        print(f"""ID: {key}
{value}""")


def menu():
    print("Bienvenido al sistema administrativo academico")
    print("="*46)
    print("Que desea realizar?\n")
    print("""1. Agregar estudiante
2. Ver lista de estudiantes
3. Eliminar estudiante
4. Actualizar datos de estudiantes
5. Salir""")
    op = int(input("Digite su opcion: "))
    return op


def main():
    while True:
        system("cls")
        op = menu()
        if op == 1:
            system("cls")
            addStudent()
            system("pause")
        elif op == 2:
            system("cls")
            showStudents()
            system("pause")
        elif op == 3:
            system("cls")
            deleteStudent()
            system("pause")
        elif op == 4:
            system("cls")
            updateStudent()
            system("pause")
        elif op == 5:
            print("Saliendo.........")
            system("pause")
        else:
            print("Opcion invalida")


main()
