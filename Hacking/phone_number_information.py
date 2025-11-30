
# coding: UTF-8

# phone_number_information.py

# O script phone_number_information.py recupera informações sobre um número de telefone usando a phonenumbers biblioteca.

import phonenumbers, time, subprocess, os, sys
from phonenumbers import geocoder
from phonenumbers import carrier

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/phonenumberinformation.py     *')
    print ('\n******************************************************************************')
    print ('\n')

usage ()

try:

    subprocess.run (['sleep 0.5'], shell=True)
    Type_the_phone_number = input ('Type the phone number: ')
    subprocess.run (['sleep 0.5'], shell=True)
    subprocess.run (['clear'], shell=True)

    telephone = Type_the_phone_number
    telephone_ajust = phonenumbers.parse (telephone)

    print (telephone_ajust)
    time.sleep (1)

    subprocess.run (['clear'], shell=True)

except KeyboardInterrupt:

    subprocess.run (['clear'], shell=True)
    time.sleep (0.5)
    sys.exit ()

def main ():

    print ('\n')
    print ('\n**********************')
    print ('\n* 1 - which location *')
    print ('\n* 2 - which operator *')
    print ('\n**********************')
    print ('\n')

    try:

        subprocess.run (['sleep 0.5'], shell=True)
        Type_the_option = int (input ('Type_the_option: '))
        subprocess.run (['sleep 0.5'], shell=True)
        subprocess.run (['clear'], shell=True)

        if Type_the_option == 1:

            telephone_ajust = phonenumbers.parse (telephone)
            telephone_format = phonenumbers.format_number (telephone_ajust, phonenumbers.PhoneNumberFormat.NATIONAL)

            print (telephone_format)
            time.sleep (1)

            location = geocoder.description_for_number (telephone_ajust, 'pt-br')

            print (location)
            time.sleep (2.5)

        elif Type_the_option == 2:

            telephone_ajust = phonenumbers.parse (telephone)
            telephone_format = phonenumbers.format_number (telephone_ajust, phonenumbers.PhoneNumberFormat.NATIONAL)

            print (telephone_format)
            time.sleep (1)

            operator = carrier.name_for_number (telephone_ajust, 'pt-br')

            print (operator)
            time.sleep (2.5)

    except KeyboardInterrupt:

        subprocess.run (['clear'], shell=True)
        time.sleep (0.5)
        sys.exit ()

if __name__ == '__main__':

    main ()

while True:

    os.system ('clear')
    time.sleep (0.5)
    sys.exit ()
    exit ()
