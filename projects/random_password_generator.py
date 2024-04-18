import string

import secrets

length=int(input("please enter length for which you want to generate random password: "))

contain_symbols=input("If you want to include symbols in password enter True: ")

contain_uppercase=input("If you want to include uppercase letters in password enter True: ")

def pasword_generator(length,contain_symbols,contain_uppercase):
    
    combination=""

    password=""

    lowercase=string.ascii_lowercase
    
    combination+=lowercase

    if contain_symbols=="True":
        symbols=string.punctuation
        combination+=symbols

    if contain_uppercase=="True":
        uppercase=string.ascii_uppercase
        combination+=uppercase

    for _ in range(length):

        password+=combination[secrets.randbelow(len(combination))]

    return password

print(pasword_generator(length,contain_symbols,contain_uppercase))
