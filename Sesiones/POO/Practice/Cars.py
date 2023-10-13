from os import system
import claseCar as c
Cars = []
def addCar():
    marca = input("Escribe la marca del coche: ")
    model = input("Escribe el modelo del coche: ")
    color = input("Escribe el color del coche: ")
    price = float(input("Escribe el precio del coche: "))
    car = c.Car(marca,model,color,price)
    Cars.append(car)
    
def showCars():
    for car in Cars:
        print(f"La marca del coche es: {car.marca}")
        print(f"El modelo del coche es: {car.model}")
        print(f"El color del coche es: {car.color}")
        print(f"El precio del coche es {car.getPrice()}")
        
def main():
    while True:
        system("cls")
        print("""1. Agregar coche
2. Mostrar coches
3. Salir""")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            addCar()
            system("pause")
        elif op == 2:
            showCars()
            system("pause")
        elif op == 3:
            print("Good bye")
            system("pause")
        else:
            print("Opcion invalida")

main()
            