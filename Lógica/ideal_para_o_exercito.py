
# coding: UTF-8

# ideal_para_o_exercito.py

# O script ideal_para_o_exercito.py verifica se uma pessoa atende a determinados critérios para servir no exército com base em idade, altura e peso. Informa ao usuário se ele atende aos requisitos ou não.

import os, time

class Exercito:

    def __init__ (self):

        os.system ('clear')
        self.idade = int (input ('Informe sua idade: '))
        self.altura = float (input ('Informe sua altura: '))
        self.peso = int (input ('Informe seu peso: '))
        os.system ('clear')

    def verificar_requisitos (self):

        resultados = {

            "Idade": self.idade >= 18,
            "Altura": self.altura >= 1.70,
            "Peso": self.peso >= 60

        }

        return resultados

    def exibir_resultado (self):

        requisitos = self.verificar_requisitos ()

        try:

            if all (requisitos.values ()):

                print ("Parabéns! Você possui todos os requisitos mínimos para servir ao exército, veja: ")
                print ('\n')

            else:

                print ("Você não possui todos os requisitos mínimos para servir ao exército, veja: ")
                print ('\n')

            for requisito, valido in requisitos.items ():

                cor = '\033[32m' if valido else '\033[31m'
                print (f"{cor}{requisito}: {'Atendido' if valido else 'Não atendido'}")

            print ('\033[0m')
            time.sleep (4.5)
            os.system ('clear')

        except KeyboardInterrupt:

            os.system ('clear')
            pass

if __name__ == "__main__":

    candidato = Exercito ()
    candidato.exibir_resultado ()
