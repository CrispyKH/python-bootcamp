import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
option = int(input(f"Press 1 to shuffle the order. Press 0 for normal order "))

if option == 0:
    #Easy Mode - Order not randomised:
    password = "" #empty string for password
    #ex: nr_letters = 4
    for char in range(1, nr_letters + 1): #loop for number of letters
        password += random.choice(letters) #adds a random letter to password
    for char in range(1 , nr_symbols + 1):
        password += random.choice(symbols)
    for num in range(1 , nr_numbers + 1):
        password += random.choice(numbers)
    print(f"Password generated: {password}")
elif option == 1:
    #Hard Mode - Order randomized
    password_list = [] #empty list for password
    for char in range(0 , nr_letters):
        password_list.append(random.choice(letters))
    for char in range(0 , nr_symbols):
        password_list.append(random.choice(symbols))
    for num in range(0 , nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    print(f"Your random password is: {password}")
else:
    print("Invalid option")


