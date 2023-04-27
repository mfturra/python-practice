# Given Prompt
import random

# Preset variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomized
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

# Create empty list for password
password = []

# Randomly select letters from letters variable and append
for l in range(1, nr_letters + 1):
    password += random.choice(letters)

# Randomly select symbols from symbols variable and append
for s in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Randomly select numbers from numbers variable and append
for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# Output random concatenated string of letter's symbols and numbers
# print(random_letters + random_symbols + random_numbers)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Create empty list for password
password_list = []

# Randomly select letters from letters variable and append
for l in range(1, nr_letters + 1):
    password_list += random.choice(letters)

# Randomly select symbols from symbols variable and append
for s in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Randomly select numbers from numbers variable and append
for n in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Output random concatenated string of letter's symbols and numbers
# print(random_letters + random_symbols + random_numbers)
password = ""
for char in password_list:
    password += char

# Another concatenation attempt
'''password_list = list(password)
random.shuffle(password_list)'''

# Output password
print(f"Here is your password: {password}")
