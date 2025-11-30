
# coding: UTF-8

# CPF_identification_by_Brazilian_states.py

# O script CPF_identification_by_Brazilian_states.py identifica um estado brasileiro (ou sua sigla) e imprime uma identificação fictícia de CPF associada a esse estado.

import sys, time, os

def show_usage ():

    os.system ('clear')
    print ("Usage: python3 CPF_identification_by_Brazilian_states.py [state or acronym]")
    time.sleep (3.5)
    os.system ('clear')

def get_cpf_identification (state_or_acronym):

    os.system ('clear')

    cpf_mapping = {

        ('Rio Grande do Sul', 'RS'): '111.111.110-11',
        ('Distrito Federal', 'DF', 'Goiás', 'GO', 'Mato Grosso', 'MT', 'Mato Grosso do Sul', 'MS', 'Tocantins', 'TO'): '222.222.221-22',
        ('Amazonas', 'AM', 'Pará', 'PA', 'Roraima', 'RO', 'Amapá', 'AP', 'Acre', 'AC', 'Rondônia', 'RO'): '333.333.332-33',
        ('Ceará', 'CE', 'Maranhão', 'MA', 'Piauí', 'PI'): '444.444.443-44',
        ('Paraíba', 'PB', 'Pernambuco', 'PE', 'Alagoas', 'AL', 'Rio Grande do Norte', 'RN'): '555.555.554-55',
        ('Bahia', 'BA', 'Sergipe', 'SE'): '666.666.665-66',
        ('Minas Gerais', 'MG'): '777.777.776-77',
        ('Rio de Janeiro', 'RJ', 'Espírito Santo', 'ES'): '888.888.887-88',
        ('São Paulo', 'SP'): '999.999.998-99',
        ('Paraná', 'PR', 'Santa Catarina', 'SC'): '000.000.009-00',

    }

    for states, cpf in cpf_mapping.items ():

        if state_or_acronym in states:

            print (f'Brazilian state or acronym: {state_or_acronym}')
            print (f'CPF identification: {cpf}')
            time.sleep (3.5)
            os.system ('clear')
            return

    print ('Brazilian state or acronym not found...')
    time.sleep (3.5)
    os.system ('clear')

def main ():

    if len (sys.argv) != 2:

        show_usage ()
        return

    if sys.argv [1] == '-h':

        show_usage ()
        return

    state_or_acronym = sys.argv [1]
    get_cpf_identification (state_or_acronym)

if __name__ == '__main__':

    main ()

