
# coding: UTF-8

# IP_address_options.py

# O script IP_address_options.py é uma ferramenta de linha de comando que fornece ao usuário uma interface simples para verificar diferentes endereços IP associados ao sistema ou à conexão de rede atual.

import socket
import requests
import os
import sys
import time

def clear_screen ():

    os.system ('cls' if os.name == 'nt' else 'clear')

def show_banner ():

    clear_screen ()

    print('\n')
    print('******************************************************************************')
    print(r"""
                         _
 ____                   /_/_        _         _____         _ _
|  _ \  ___ _ __ ___   ___| |_ _ __(_) ___   |  ___| __ ___(_) |_ __ _ ___
| | | |/ _ \ '_ ` _ \ / _ \ __| '__| |/ _ \  | |_ | '__/ _ \ | __/ _` / __|
| |_| |  __/ | | | | |  __/ |_| |  | | (_) | |  _|| | |  __/ | || (_| \__ \
|____/ \___|_| |_| |_|\___|\__|_|  |_|\___/  |_|  |_|  \___|_|\__\__,_|___/

    """)

    print('\n******************************************************************************')
    print('\n* Copyright of Demétrio Freitas, 2021                                        *')
    print('\n* https://github.com/PPrrooggrraammeerr                                      *')
    print('\n* https://github.com/PPrrooggrraammeerr/Python/IP_address_options.py         *')
    print('\n******************************************************************************')
    print('\n')

    time.sleep(3.5)
    clear_screen()

def main ():

    while True:

        clear_screen ()

        print ('\n')
        print ("""    ===========================
   *                           *
   *      1 - IP internal      *
   *      2 - IP external      *
   *      3 - IP localhost     *
   *      4 - Exit program     *
   *                           *
    =========================== """)
        print ('\n')

        option = input ("What's my IP? Type the option: ")

        if option == '1':

            client = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
            client.connect (('8.8.8.8', 80))
            result = client.getsockname () [0]
            print (f"What's my IP internal: {result}")
            time.sleep (3.5)

        elif option == '2':

            IP_external = requests.get ('https://api.ipify.org/').text
            print (f"What's my IP external: {IP_external}")
            time.sleep (3.5)

        elif option == '3':

            hostname = socket.gethostname ()
            localhost = socket.gethostbyname (hostname)
            print (f"What's my IP localhost: {localhost}")
            time.sleep (3.5)

        elif option == '4':

            sys.exit ()


if __name__ == '__main__':

    show_banner ()
    main ()
