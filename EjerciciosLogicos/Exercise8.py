phrase = input("Write a word or a phrase\n")
if(phrase == ''.join(reversed(phrase))):
    print(f"{phrase} is a palidrome")
else:
    print(f"{phrase} isn't a palindrome")
    