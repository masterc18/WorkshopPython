limit = int(input("Write the limit\n"))
aux = 1
fib = 0

if(limit > 0):
    for i in range (limit):
        aux+=fib
        fib = aux - fib
        result = fib
        
        print(f"{aux}+{fib} = {result}")
else:
     print("The number must be edelry than 0")