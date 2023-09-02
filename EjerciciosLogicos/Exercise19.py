num = input("Write a number chain\n")

if(num == ''.join(reversed(num))):
    print(f"{num} is a numeric palindrome")
else:
    print(f"{num} isn't a numeric palindrome")