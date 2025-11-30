
# coding: UTF-8

# tcpserver.py

import socket, subprocess, time, sys, os

while True:

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/tcpserver.py                  *')
    print ('\n******************************************************************************')
    print ('\n')

    break

while True:

    try:

        server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

        Type_the_IP_or_host = input ('Type the IP or host: ')
        Type_the_port = int (input ('Type the port: '))

        time.sleep (0.5)
        subprocess.run (['cls'], shell=True)

        server.bind ((Type_the_IP_or_host, Type_the_port))

        server.listen ()

        dice, client = server.accept ()

        print ('Server IP or host: {}'.format (Type_the_IP_or_host))
        print ('Open port: {}'.format (Type_the_port))
        print ('\n')
        break

    except KeyboardInterrupt:
    
        subprocess.run (['cls'], shell=True)
        time.sleep (0.5)
        server.close ()
        sys.exit ()

while True:

    try:
    
        package = dice.recv (1024)
        package = package.decode ('UTF-8')
        print ('Client: {}'.format (package))

        message = input ('Server: ')

        dice.send (message.encode ('UTF-8'))

    except KeyboardInterrupt:
    
        subprocess.run (['clear'], shell=True)
        time.sleep (0.5)
        server.close ()  
        client.close ()  
        sys.exit ()
