#import math
num=(int(input("Write a number\n")))
factorial = 1
if(num > 0):
    for i in range (factorial,num+1):
        factorial *= i
    
    print(f"The factorial of {num} = {factorial}")
else:
    print("The number must be positive")

# factorial = math.factorial(num)

# print(f"The factorial of {num} is {factorial}")
