
# coding: UTF-8

# estacoes_do_ano.py

# O script estacoes_do_ano.py fornece um menu de opções para consulta das estações do ano e seus respectivos meses associados a elas.

import datetime
import os

os.system ('cls')
print ('\n')
print (''' 
          ========================================                     
         [   01 - Saber estação pelo mês          ]
         [   02 - Meses que ocorrem as estações   ]
         [   03 - Saber estação do mês atual      ]
          ======================================== ''')
print ('\n')

opcoes_meses_estacoes = int (input ('Digite a opção: '))

if opcoes_meses_estacoes == 1:
    
    while True:

        os.system ('cls')
        print('\n')
        print(''' 
              ===================
             [   01 - Janeiro    ]
             [   02 - Fevereiro  ]
             [   03 - Março      ]
             [   04 - Abril      ]
             [   05 - Maio       ]
             [   06 - Junho      ]
             [   07 - Julho      ]
             [   08 - Agosto     ]
             [   09 - Setembro   ]
             [   10 - Outubro    ]
             [   11 - Novembro   ]
             [   12 - Dezembro   ]
              =================== ''')
        print('\n')

        digite_opcao_mes = int (input ('Digite a opção: '))
        os.system ('cls')
        
        meses_ano_lista = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
        estacoes_ano_lista = ['Primavera', 'Verão', 'Outono', 'Inverno']
        
        mes_ano_associado = meses_ano_lista [digite_opcao_mes - 1]
        
        if 1 <= digite_opcao_mes <= 12:
        
            if digite_opcao_mes == 12 or digite_opcao_mes == 1 or digite_opcao_mes == 2:

                estacao_mes_associado = estacoes_ano_lista [1]
                print (f'A estação do mês de {mes_ano_associado} é: {estacao_mes_associado}')
                break
                
            elif digite_opcao_mes == 3 or digite_opcao_mes == 4 or digite_opcao_mes == 5:

                estacao_mes_associado = estacoes_ano_lista [2]
                print (f'A estação do mês de {mes_ano_associado} é: {estacao_mes_associado}')
                break
                
            elif digite_opcao_mes == 6 or digite_opcao_mes == 7 or digite_opcao_mes == 8:
                
                estacao_mes_associado = estacoes_ano_lista [3]
                print (f'A estação do mês de {mes_ano_associado} é: {estacao_mes_associado}')
                break
                
            elif digite_opcao_mes == 9 or digite_opcao_mes == 10 or digite_opcao_mes == 11:

                estacao_mes_associado = estacoes_ano_lista [0]
                print (f'A estação do mês de {mes_ano_associado} é: {estacao_mes_associado}')
                break

elif opcoes_meses_estacoes == 2:
    
    os.system ('cls')
    print ('\n')
    print (''' 
             ====================
            [    1 - Primavera   ]
            [    2 - Verão       ]
            [    3 - Outono      ]
            [    4 - Inverno     ]
             ==================== ''')
    print ('\n')

    opcao_numero_estacao = int (input ('Digite a opção: '))
    os.system ('cls')
    
    estacoes_ano = {
        1: 'Primavera',
        2: 'Verão',
        3: 'Outono',
        4: 'Inverno'
    }

    meses_estacoes_ano = {
        1: ['Setembro', 'Outubro', 'Novembro'],
        2: ['Dezembro', 'Janeiro', 'Fevereiro'],
        3: ['Março', 'Abril', 'Maio'],
        4: ['Junho', 'Julho', 'Agosto']
    }
    
    if opcao_numero_estacao in estacoes_ano:
        
        estacao_ano = estacoes_ano [opcao_numero_estacao]
        mes_estacao = meses_estacoes_ano [opcao_numero_estacao]
        
        print (f'Os meses que ocorrem a estação da {estacao_ano} são:\n')
        
        for estacao_mes in mes_estacao:
            
            print (estacao_mes)

elif opcoes_meses_estacoes == 3:
    
    os.system ('cls')
    
    data_atual = datetime.datetime.now ()
    
    mes_atual = data_atual.month
    
    meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
    estacao_atual_mes = meses_do_ano [mes_atual - 1]
    
    if mes_atual in [12, 1, 2]:
    
        print (f'Estamos no mês de {estacao_atual_mes}, portanto sua estação é:\n')
        print ('Verão')
        
    elif mes_atual in [3, 4, 5]:
        
        print (f'Estamos no mês de {estacao_atual_mes}, portanto sua estação é:\n')
        print ('Outono')
        
    elif mes_atual in [6, 7, 8]:
        
        print (f'Estamos no mês de {estacao_atual_mes}, portanto sua estação é:\n')
        print ('Inverno')
        
    elif mes_atual in [9, 10, 11]:
        
        print (f'Estamos no mês de {estacao_atual_mes}, portanto sua estação é:\n')
        print ('Primavera')

