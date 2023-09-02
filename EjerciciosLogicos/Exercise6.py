limit = 5
suma = 0

for i in range (limit):
    numbers = int(input("Write the numbers\n"))
    
    suma += numbers
    
    percentaje = suma / limit
    
    print(f" the percentage is {percentaje}")