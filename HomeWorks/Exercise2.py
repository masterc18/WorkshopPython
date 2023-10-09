"""Leer un listado de frutas y solo mostrar las frutas cuyo nombre tenga mas de 5 letras"""
largeNames=[]
shortNames=[]
Fruits = int(input("Write the fruits that you wanna add: "))

for i in range (Fruits):
    Names = input("Write the name: ")
    
    if(len(Names)>5):
        largeNames.append(Names)
    else:
        shortNames.append(Names)
        
print(f"The fruits with large name are: {largeNames}")
print(f"The fruits with short name are: {shortNames}")