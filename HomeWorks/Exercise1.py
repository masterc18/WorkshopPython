"""Leer x cantidad de numeros pares y mostrar dichos numeros"""
pairNumbers = []
unPairNumbers = []
number = int(input("Tell me how many number you will write: "))

for i in range (number):
    numbers = int(input("Write the numbers: "))
    if(numbers % 2 == 0):
        pairNumbers.append(numbers)
    else:
        unPairNumbers.append(numbers)
        
print(f"Los numeros pares son: {pairNumbers}")
print(f"Los numeros inpares son: {unPairNumbers}")