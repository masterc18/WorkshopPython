import os
os.system("clear")
# """Leer un numero e imprimir los numeros entre ellos"""
# num1 = int(input("Valor de inicio: "))
# num2 = int(input("Valor final: "))
# cont = num1-1
# while (cont > num2 or cont < num2 ):
#     print(cont)
#     cont -= 1


#Ejercicio 2
# num1 = int(input("Ingrese el primer numero\n"))
# num2 = int(input("Ingrese el segundo numero\n"))

# if num1 < num2:
#     cont = num1+1
#     while (cont < num2):
#         print(cont)
#         cont += 1
        
# else:
#     cont = num1-1
#     while (cont > num2):
#       print(cont)
#       cont -=1
       
"""Calcular el IVA de un producto"""
def CalculateVAT(price):
    return price * 0.15

def showTotal(price, vat):
    return price + vat

def main():
    price = int(input("Write the price of the product\n"))
    vat = CalculateVAT(price)
    total = showTotal(price,vat)
    print(f"The price {price}")
    print(f"VAT {vat}")
    print(f"Total {total}")
    

main()