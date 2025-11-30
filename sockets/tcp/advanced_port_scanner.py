
# coding: UTF-8

# advanced_port_scanner.py

# O script advanced_port_scanner.py é um escaneador simples de portas que tenta se conectar a cada porta de um IP ou host fornecido, do intervalo 1 a 65535. Se a porta estiver aberta, ele exibe essa porta junto com o serviço associado.

import socket, sys, subprocess, os, time

def usage ():

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/advanced_port_scanner.py      *')
    print ('\n******************************************************************************')
    print ('\n')

    print ('python3 advancedportscan.py -h')
    print ('\n')
    subprocess.run (['sleep 3.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    sys.exit ()

def advancedportscan (Type_the_IP_or_host):

    time.sleep (0.5)
    os.system ('clear')

    try:

        for port in range (1, 65535):

            client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout (0.5)
            code = client.connect_ex ((Type_the_IP_or_host, port))

            if code <= 0 or code == 0:

                print ('{} open {}'.format (port, socket.getservbyport (port)))
                client.close ()

    except:

        os.system ('clear')
        time.sleep (0.5)
        pass

    return Type_the_IP_or_host

def main ():

    try:

        if sys.argv [1] == '-h':

            time.sleep (0.5)
            os.system ('clear')

            print ('python3 advancedportscan.py [IP or host]')

            time.sleep (3.5)
            os.system ('clear')

        else:

            Type_the_IP_or_host = (sys.argv [1])
            advancedportscan (Type_the_IP_or_host)

    except:

        usage ()

if __name__ == '__main__':

    main ()

while True:

    subprocess.run (['sleep 3.5'], shell=True)
    break

sys.exit ()
