
# coding: UTF-8

# ordem_crescente.py

# O script ordem_crescente.py solicita que o usuário insira três valores diferentes e os imprima em ordem crescente.

import os, time

os.system('clear')

values = []
values.append (int (input ('value1: ')))
values.append (int (input ('value2: ')))
values.append (int (input ('value3: ')))

sorted_values = sorted (values)

os.system ('clear')
print (sorted_values [0], sorted_values [1], sorted_values [2])
time.sleep (3.5)
os.system ('clear')
