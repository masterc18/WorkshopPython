limit = int(input("Write the limit\n"))
aux = 1
fib = 0

if(limit > 0):
    for i in range (limit):
        print(f"[{fib}]")
        aux+=fib
        fib = aux - fib
else:
     print("The number must be edelry than 0")