class Student:
    def __init__(self, name, email, carrer, average, price):
        self.name = name
        self.email = email
        self.carrer = carrer
        self.average = average
        self.price = price


    def getScholarShip(self):
    # Otrorgar beca del 50% si el promedio es mayor que 85 y menos de 95
    # Otorgar beca del 100% si el promedio es mayor a 95
        if (self.average > 85 and self.average < 95):
            return self.price * 0.5
        elif (self.average >= 95 and self.average <= 100):
            return self.price * 1
        else:
            return 0


    def getTotal(self):
        return self.price - self.getScholarShip()


    def __str__(self):
        return f"""Nombre {self.name}
Email {self.email}
Carrera {self.carrer}
Promedio {self.average}
Precio {self.price}
Beca {self.getScholarShip()}
Total a pagar {self.getTotal()}"""
