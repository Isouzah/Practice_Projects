import string
import random

print("Bem vindo ao gerador de senhas!")
input("Pressione enter para continuar...")
length = int(input("Quantos digitos deseja que a senha tenha? "))

upper_case = (input("deseja adiconar letras maiusculas? (S/N) ")).upper().strip()
if upper_case == "S":
    upper_case = True
else:
    upper_case = False

lower_case = (input("deseja adiconar letras minusculas? (S/N) ")).upper().strip()
if lower_case == "S":
    lower_case = True
else:
    lower_case = False

numbers = (input("deseja adiconar numeros? (S/N)) ")).upper().strip()
if numbers == "S":
    numbers = True
else:
    numbers = False

special_characters = (input("deseja adiconar caracteres especiais? (S/N) ")).upper().strip()
if special_characters == "S":
    special_characters = True
else:
    special_characters = False

possible_characters = ""
if upper_case == True:
    possible_characters += string.ascii_uppercase
if lower_case == True:
    possible_characters += string.ascii_lowercase
if numbers == True:
    possible_characters += string.digits
if special_characters == True:
    possible_characters += string.punctuation

def generator(lenght, possible_characters):
    password = "".join(random.choice(possible_characters) 
                       for _ in range(lenght))
    return password

print("Gerando senha...")
password = generator(length, possible_characters)
print(f"Sua senha é: {password}")