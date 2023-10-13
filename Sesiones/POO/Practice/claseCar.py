class Car():
    def __init__(self, marca,model,color,price):
        self.marca = marca
        self.model = model
        self.color = color
        self.price = price
    
    def __str__(self):
        return f"Marca: {self.marca}| Model: {self.model}| Color: {self.color}"
    
    def getPrice(self):
        return self.price * 25.5