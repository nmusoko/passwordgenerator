import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passWord = [] # list to hold the password

#Generate Random letters in letters list
for letter in range (1,nr_letters + 1):
    l = random.randint(0, len(letters)-1)
    passWord += letters[l]
#Generate Random symbols in symbols list
for symbol in range (1,nr_symbols + 1):
    s = random.randint(0, len(symbols)-1)
    passWord += symbols[s]
#Generate Random numbers in numbers list
for number in range (1,nr_numbers + 1):
    n = random.randint(0, len(numbers)-1)
    passWord += numbers[n]

random.shuffle(passWord) # << shuffle my list
final_Password = "".join(passWord) #Convert my list to a string
print(f"Your Password is {final_Password}")


