
# coding: UTF-8

# main.py

from modules.open_jahu import open_jahu
from modules.extract_jahu import extract_jahu
from modules.extract_jahu import add_year_by_exercise
from modules.extract_jahu import add_title_and_address
from modules.extract_jahu import exclude_column_year
from modules.extract_jahu import merge_excels_into_final

def main ():

    print (f'MAIN.PY EM EXECUÇÃO! CHAMANDO OPEN_JAHU.PY PARA EXECUTAR...\n')
    open_jahu ()
    
    print (f'OPEN_JAHU.PY EXECUTADO COM SUCESSO!')
    print (f'ARQUIVOS PDFS EXTRAÍDOS E SALVOS COM SUCESSO!\n')
    
    print (f'MAIN.PY EM EXECUÇÃO! CHAMANDO EXTRACT_JAHU.PY PARA EXECUTAR...\n')
    extract_jahu ()
    
    print (f'EXECUTANDO EXTRACT_JAHU E PEGANDO OS VALORES DE TOTAL DA DÍVIDA...')
    print (f'PASSANDO ESSES VALORES PARA EXCEL...\n')
    
    print (f'EXTRAINDO ANO E PASSANDO PARA EXCEL...\n')
    add_year_by_exercise ()
    
    print (f'EXTRAINDO DADOS DE ENDEREÇO E PASSANDO PARA EXCEL...\n')
    add_title_and_address ()
    
    print (f'EXCUINDO COLUNA ANO DE CADA ARQUIVO EXCEL...\n')
    exclude_column_year ()
    
    print (f'MESCLANDO DADOS E PASSANDO PARA EXCEL FINAL...\n')
    merge_excels_into_final ()
    
    print (f'EXTRACT_JAHU.PY EXECUTADO COM SUCESSO!\n')

if __name__ == '__main__':
    
    main ()