import random
from colorama import Fore


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '[', ']']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(4, 12)  #int(input("How many letters would you like in your password?\n"))
nr_symbols = random.randint(2, 9)  #int(input(f"How many symbols would you like?\n"))
nr_numbers = random.randint(2, 10)  #int(input(f"How many numbers would you like?\n"))

password = []

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

random.shuffle(password)
password_size = len(password)
print(f" your password contains: {password_size} characters")
random_password = "".join(password)
print(f"Your randomly generated password is: " + Fore.GREEN + f"{random_password}")

