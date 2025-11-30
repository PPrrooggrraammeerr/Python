
# coding: UTF-8

# passwords_generator_in_quantities.py

# O script passwords_generator_in_quantities.py gera uma quantidade especificada de senhas aleatórias com um número definido de caracteres, utilizando uma combinação de letras, dígitos e símbolos de pontuação. Cada senha é exibida ao usuário após sua criação.
    
from random import choice
import os, string

os.system ('cls')

quantity_of_passwords = int (input ('Quantity of passwords: '))
size_of_password = int (input ('Dígits: '))

characters = string.ascii_letters + string.digits + string.punctuation

os.system ('cls')

for quantity in range (quantity_of_passwords):

    secure_password = ''

    for password in range (size_of_password):

        secure_password += choice (characters)

    print (secure_password)

