from os import system
from statistics import median, mean
#Deseo una lista de numeros y calcular las media de los numberos
numbers = []

def addNumber(number):
    numbers.append(number)
    
def readNumber():
    number = int(input("Ingresa un numero: "))
    addNumber(number)
    
def showNumber():
    for number in numbers:
        print(number)
#Forma basica de hacerlo        
"""def getMedia():
    suma = 0
    for number in numbers:
        suma+=number
    avg = suma/len(numbers)
    return avg"""
    
#Forma mejor
def getAverage():
    # numbers.sort()
    return mean(numbers)

def menu():
    op = int(input("""
1. Ingresar
2. Mostrar
3. Media
4. Salir
Dime una opcion:
"""))
    return op

def main():
    op = 0
    while(op!=4):
        system("cls")
        op = menu()
        if(op == 1):
            readNumber()
            system("pause")
        elif(op == 2):
            showNumber()
            system("pause")
        elif(op == 3):
            #print(f"La media es {getMedia()}")
            print(f"La media es {getAverage()}")
            system("pause")
        else:
            print("Sayonara")
            system("pause")
            
main()