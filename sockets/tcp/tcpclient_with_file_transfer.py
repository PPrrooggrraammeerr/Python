
# coding: UTF-8

# tcpclient_with_file_transfer.py

import socket, subprocess, time, sys, os

while True:

    os.system ('cls')
    os.system ('timeout /t 1 > nul')

    print ('\n')
    print ('*********************************************************************************')
    print (r"""
                         _
 ____                   /_/_        _         _____         _ _                *
|  _ \  ___ _ __ ___   ___| |_ _ __(_) ___   |  ___| __ ___(_) |_ __ _ ___
| | | |/ _ \ '_ ` _ \ / _ \ __| '__| |/ _ \  | |_ | '__/ _ \ | __/ _` / __|    *
| |_| |  __/ | | | | |  __/ |_| |  | | (_) | |  _|| | |  __/ | || (_| \__ \
|____/ \___|_| |_| |_|\___|\__|_|  |_|\___/  |_|  |_|  \___|_|\__\__,_|___/    *

    """)

    print ('\n********************************************************************************')
    print ('\n* Copyright of Demétrio Freitas, 2023                                          *')
    print ('\n* https://github.com/PPrrooggrraammeerr                                        *')
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/tcpclient_with_file_transfer.py *')
    print ('\n********************************************************************************')
    print ('\n')

    os.system ('timeout /t 1 > nul')
    break

try:

    IP_or_host = input ('Type the IP or host: ')
    port = int(input ('Type the port: '))
    os.system ('cls')

    user_profile = os.getlogin ()
    client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

    client.connect((IP_or_host, port))
    print ('Client: {} is connected on port: {}'.format (IP_or_host, port))
    print ('\n')

    arquivo = str (input ('File: '))
    os.system ('cls')

    client.send (arquivo.encode ())

    with open (f'C:\\Users\\{user_profile}\\Desktop\\{arquivo}', 'wb') as file:
    
        while True:
    
            try:
            
                data = client.recv (2048)

                if not data:
                
                    break

                file.write (data)

                print ('File received successfully!')
                time.sleep (2.5)
                os.system ('cls')

            except KeyboardInterrupt:
                
                subprocess.run (['cls'], shell=True)
                time.sleep (0.5)
                sys.exit ()

except Exception as e:

    print (f'Error: {e}')

finally:

    client.close ()