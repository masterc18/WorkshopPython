from math import gcd

number1 = int(input("Write the first number\n"))
number2 = int(input("Write the second number\n"))

result = gcd(number1,number2)

print(f"The greatest common divisor of {number1} and {number2} is {result}")