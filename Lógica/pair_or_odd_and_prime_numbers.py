
# coding: UTF-8

# pair_or_odd_and_prime_numbers.py

# O script fornecido pair_or_odd_and_prime_numbers.py solicita que o usuário insira um número e então determina se o número é primo ou não e se é ímpar ou par.

import os, time

os.system ('clear')

try:

    number = int (input ('Type the number: '))

except ValueError:

    print ("Please enter a valid number.")
    os.system ('clear')
    exit ()

except KeyboardInterrupt:

    os.system ('clear')
    exit ()

class Numbers:

    def __init__ (self, number):

        self.number = number

    def is_prime (self):

        if self.number < 2:

            return False

        for i in range (2, int (self.number ** 0.5) + 1):

            if self.number % i == 0:

                return False

        return True

    def pair_or_odd_and_prime_numbers (self):

        prime_status = "prime" if self.is_prime () else "not prime"
        even_odd_status = "even" if self.number % 2 == 0 else "odd"
        return f"Number {self.number} is {prime_status} and {even_odd_status}."

result = Numbers (number)

os.system ('clear')
print (result.pair_or_odd_and_prime_numbers ())
time.sleep (3.5)
os.system ('clear')
