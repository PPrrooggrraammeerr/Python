
# coding: UTF-8

# tcpserver_with_file_transfer.py

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
    print ('\n* Copyright of Demétrio Freitas, 2023                                        *')
    print ('\n* https://github.com/DFSecurity                                              *')
    print ('\n* https://github.com/DFSecurity/Python/tcpserver_with_file_transfer.py       *')
    print ('\n******************************************************************************')
    print ('\n')

    break

try:

    IP_or_host = input ('Type the IP or host: ')
    port = int (input ('Type the port: '))
    os.system ('cls')

    server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    server.bind ((IP_or_host, port))
    server.listen (1)

    print ('Server: {} is in listening mode on port: {}'.format (IP_or_host, port))
    data, client = server.accept ()
    print ('Client: {} is connected on port: {}'.format (IP_or_host, port))

    result = data.recv (1024).decode ('UTF-8')

    with open ('udpclient.py', 'rb') as file:
    
        for line in file:
        
            data.send (line)

    print ('\n')
    print ('Successful file transfer!')
    time.sleep (2.5)
    os.system ('cls')

except KeyboardInterrupt:

    subprocess.run (['cls'], shell=True)
    time.sleep (0.5)
    sys.exit ()

finally:

    server.close ()
    data.close ()

