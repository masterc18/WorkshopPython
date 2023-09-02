number1 = int(input("Write the first number\n"))
number2 = int(input("write the second number\n"))
number3 = int(input("Write the third number\n"))

if number1 > number2 and number1 > number3:
    print(f"the ederly number is {number1}")
elif number2 > number1 and number2 > number3:
    print(f"the ederly number id {number2}")
else:
    print(f"the ederly number is {number3}")

# Maximun=max(number1,number2,number3)

# print(f"The ederly number is {Maximun}")