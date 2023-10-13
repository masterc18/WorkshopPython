# Clase
class Person:
    def __init__(self, Firstname, Secondname, Birthdate):
        # Atributos
        self.Firstname = Firstname,
        self.Secondname = Secondname,
        self.Birthdate = Birthdate

    # Metodos
    def getEmail(self):
        return f"{self.Firstname}.{self.Secondname}@gmail.com"

    def getAge(self):
        return 2023 - self.Birthdate

    def isOlder(self):
        #Operador ternario
        return "Mayor de edad" if self.getAge() >= 18 else "Menor de edad"
