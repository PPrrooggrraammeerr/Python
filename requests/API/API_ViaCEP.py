
# coding: UTF-8

# API_ViaCEP.py

# O script ViaCEP.py tem como objetivo consultar informações relacionadas a um CEP (Código de Endereçamento Postal) brasileiro por meio do serviço ViaCEP.

import requests
import os
import sys
import time

def clear_screen ():

    os.system ('cls' if os.name == 'nt' else 'clear')

def usage ():

    clear_screen ()
    time.sleep (0.5)

    print ('\n')
    print ('******************************************************************************')
    print (r"""
                         _
 ____                   /_/_        _         _____         _ _
|  _ \  ___ _ __ ___   ___| |_ _ __(_) ___   |  ___| __ ___(_) |_ __ _ ___
| | | |/ _ \ '_ ` _ \ / _ \ __| '__| |/ _ \  | |_ | '__/ _ \ | __/ _` / __|
| |_| |  __/ | | | | |  __/ |_| |  | | (_) | |  _|| | |  __/ | || (_| \__ \
|____/ \___|_| |_| |_|\___|\__|_|  |_|\___/  |_|  |_|  \___|_|\__\__,_|___/

    """)

    print ('\n******************************************************************************')
    print ('\n* Copyright of Demétrio Freitas, 2022                                        *')
    print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/ViaCEP.py                     *')
    print ('\n******************************************************************************')
    print ('\n')

    print ('python3 ViaCEP.py -h')
    print ('\n')

    time.sleep (3.5)
    clear_screen ()
    sys.exit ()

def viacep (cep):

    clear_screen ()

    cep = cep.replace ('-', '')

    if len (cep) == 8:

        link = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get (link)

        if response.status_code == 200:

            data = response.json ()

            if "erro" not in data:

                print (f"CEP: {data['cep']}")
                print (f"Logradouro: {data['logradouro']}")
                print (f"Bairro: {data['bairro']}")
                print (f"Localidade: {data['localidade']}")
                print (f"UF: {data['uf']}")
                print (f"IBGE: {data['ibge']}")
                print (f"GIA: {data['gia']}")
                print (f"DDD: {data['ddd']}")
                print (f"SIAFI: {data['siafi']}")

                time.sleep (3.5)
                clear_screen ()

            else:

                print ("Invalid CEP.")
                time.sleep (3.5)
                clear_screen ()

    else:

        print ("Invalid CEP format.")
        time.sleep (3.5)
        clear_screen ()

def main ():

    if len (sys.argv) < 2:

        usage ()

    option = sys.argv [1]

    if option == '-h':

        print ('python3 ViaCEP.py [CEP]')
        time.sleep (3.5)
        clear_screen ()

    else:

        viacep (option)

if __name__ == '__main__':

    main ()
