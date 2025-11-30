
# coding: UTF-8

# subdomains.py

# O script subdomains.py procura subdomínios de um determinado domínio usando uma lista predefinida em subdomains.txt. Se este arquivo não existir, ele criará um com alguns subdomínios comuns.

import socket
import os
import time

def clear_screen ():

    os.system ('cls' if os.name == 'nt' else 'clear')

def get_subdomains ():

    default_subdomains = {'www', 'ftp', 'mail', 'localhost', 'webmail', 'smtp', 'support', 'download', 'files', 'blog'}

    if not os.path.exists ('subdomains.txt'):

        with open ('subdomains.txt', 'w') as file:

            for subdomain in default_subdomains:

                file.write (subdomain + '\n')

    with open ('subdomains.txt', 'r') as file:

        subdomains = file.readlines ()

    return set (subdomain.strip () for subdomain in subdomains)

def scan_subdomains (domain, subdomains):

    for subdomain in subdomains:

        full_domain = f"{subdomain}.{domain}"

        try:

            ip_address = socket.gethostbyname (full_domain)
            print (f"{full_domain}: {ip_address}")

        except socket.gaierror:

            pass

def main ():

    clear_screen ()
    domain = input ('domain: ')
    print ('\n')
    subdomains = get_subdomains ()
    scan_subdomains (domain, subdomains)
    print ('\n')

if __name__ == '__main__':

    main ()
