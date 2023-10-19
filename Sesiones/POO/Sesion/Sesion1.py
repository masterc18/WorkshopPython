
class Product:
    def __init__(self, name, price, stock):
        self.name = name,
        self.price = price,
        self.stock = stock
        
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"
    
def main():
    cafe = Product("cafe",1.5,10)
    soda = Product("Soda", 2.5,20)
    print(cafe, soda, sep="/n")
    
if __name__ == "__main__":
    main()