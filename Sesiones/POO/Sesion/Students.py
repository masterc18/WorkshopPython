

from clases import Student
#Agregar elementos al diccionario
student = {1: Student("Gabriela", "gabi@gmail.com", "ISI", 90, 500)}

student2 = dict(est1=Student("Diego", "diego@gmail.com", "ISI", 100, 600))

#imprimir diccionario
print(student)
print(student2)

#mostrar valores del diccionario
print(student2["est1"])
print(student[1])