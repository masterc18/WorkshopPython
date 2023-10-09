from os import system
system("cls")

#Ejercicio 1
# from os import system
# system("cls")
# list1 = list([1,2,3,4,5,"Diego"])#Forma 1 
# list2 = [1,"Carlos"]#Forma 2
# list3 = {1,2,5,"Enrique"}
# print(list1, type(list1))
# print(list2, type(list2))
# print(list3, type(list3))

# for i in list1:#Foreach
#     print(i)

# for i in list2:
#     print(i)
    
# for i in list3:
#     print(i)
#----------------------------------------------------------------------------------------------
#Ejercicio 2
# list1 = list(range(1,100,2))
# #list(range(donde comienza, donde termina, como ira incrementando))
# print(list1)
# name = "Enrique"
# list2 = list([name, "Diego"])#Lista de 2 o mas elementos
# #list2 = list(name) Lista de un elemento
# list2.append("Carlos")
# print(list2)

# for i in list2:
#     print(i)
#----------------------------------------------------------------------------------------------
"""Ejemplo 3"""
name = "Jezer"
list1 = list(name)
list2 = list([list1, "Freddy"])#Arreglo multidimensional
list3 = list([list2, "Jesus"])

for elemento in list2:
    for subelemento in elemento:
        print(subelemento)

