
# coding: UTF-8

# ping.py

import os, sys

while True:

    os.system ('clear')
    os.system ('sleep 0.5')

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/ping.py                       *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('sleep 0.5')
    
    Type_the_IP_or_host_or_eE_to_exit = input ('Type the IP or host or e/E to exit: ')
    os.system ('sleep 0.5')

    if Type_the_IP_or_host_or_eE_to_exit == 'e' or Type_the_IP_or_host_or_eE_to_exit == 'E':

        os.system ('clear')
        os.system ('sleep 0.5')
        break

    else:

        os.system ('clear')
        os.system ('sleep 0.5')
        os.system ('ping {}'.format (Type_the_IP_or_host_or_eE_to_exit))
        os.system ('sleep 2.5')
        os.system ('clear')
        continue
        
while True:
    
    os.system ('clear')
    os.system ('sleep 0.5')
    sys.exit ()
    
