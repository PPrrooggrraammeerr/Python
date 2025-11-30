
# coding: UTF-8

# IP_Scanner.py

# O código abaixo tem como objetivo verificar um determinado intervalo de endereços IP. Em seguida, ele tenta executar ping em cada endereço IP nesse intervalo e grava o resultado em um arquivo nomeado IP_Scanner_results.txt na área de trabalho do usuário.

import ipaddress, os, time

try:

    os.system ('cls')
    user_profile = os.getlogin ()
    IP_or_host = input ('IP or host with range: ')
    generators = ipaddress.ip_network ('{}'.format (IP_or_host))
    print ('\n')

    with open (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt', 'w') as file:

        for generator in generators:

            file.write ('{}\n'.format (generator))            

    with open (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt', 'r') as file:

        IPs = file.readlines ()

        for IP in IPs:

            IP = IP.split () [0]
            response = os.popen (f'ping {IP} -n 1').read ()

            if 'Aproximar um n£mero redondo de vezes em milissegundos:' in response:
            
                print ('\033[32m{} is up'.format (IP))
                results = open (f'C:\\Users\\{user_profile}\\Desktop\\IP_Scanner_results.txt', 'a')
                results.write ('{} is up\n'.format (IP))
                results.close ()

            elif 'Resposta de {}: Host de destino inacess¡vel.'.format (IP) or 'Esgotado o tempo limite do pedido.' in response:
                
                print ('\033[31m{} is down'.format (IP))

except KeyboardInterrupt:

    os.system ('cls')
    os.remove (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt')
    time.sleep (0.5)
    os.system ('taskkill /f /im python3.10.exe > nul')
