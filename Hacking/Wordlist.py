
# coding: UTF-8

# Wordlist.py

# O script Wordlist.py tem como objetivo gerar uma wordlist com todas as permutações possíveis de uma string fornecida pelo usuário. Essas permutações são salvas em um arquivo chamado Wordlist.txt na área de trabalho do usuário.

import itertools, os, time

time.sleep (0.5)
os.system ('cls')

print ('\n')
print ('******************************************************************************')
print (r"""
                         _
 ____                   /_/_        _         _____         _ _              *
|  _ \  ___ _ __ ___   ___| |_ _ __(_) ___   |  ___| __ ___(_) |_ __ _ ___
| | | |/ _ \ '_ ` _ \ / _ \ __| '__| |/ _ \  | |_ | '__/ _ \ | __/ _` / __|  *
| |_| |  __/ | | | | |  __/ |_| |  | | (_) | |  _|| | |  __/ | || (_| \__ \
|____/ \___|_| |_| |_|\___|\__|_|  |_|\___/  |_|  |_|  \___|_|\__\__,_|___/  *
    
""")
    
print ('\n******************************************************************************')
print ('\n* Copyright of Demétrio Freitas, 2021                                        *')
print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
print ('\n* https://github.com/PPrrooggrraammeerr/Python/Wordlist.py                   *')
print ('\n******************************************************************************')
print ('\n')

time.sleep (0.5)

string = input ('string used: ')
user_profile = os.getlogin ()
results = itertools.permutations (string, len (string))

if os.path.exists (f'C:\\Users\\{user_profile}\\Desktop\Wordlist.txt'):

    with open (f'C:\\Users\\{user_profile}\\Desktop\Wordlist.txt', 'w') as file:

        for result in results:

            wordlist = ''.join (result)  
            print ('{}'.format (wordlist), file=file)
        
        file.close ()

else:

    with open (f'C:\\Users\\{user_profile}\\Desktop\Wordlist.txt', 'w') as file:

        for result in results:

            wordlist = ''.join (result)
            print ('{}'.format (wordlist), file=file)
            
        file.close ()

os.system ('cls')
time.sleep (0.5)
