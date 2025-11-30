
# coding: UTF-8

# calcular_media.py

# O script calcular_media.py calcula a média das quatro notas inseridas e, com base na média calculada, determina se o aluno foi aprovado, aprovado pelo conselho de classe, em recuperação ou reprovado.

import os, time

os.system ('clear')

first_note = float (input ('First note: '))
second_note = float (input ('Second note: '))
third_note = float (input ('Third note: '))
fourth_note = float (input ('Fourth note: '))

class calcular_media:

    def __init__ (self, first_note, second_note, third_note, fourth_note):

        self.note_first = first_note
        self.note_second = second_note
        self.note_third = third_note
        self.note_fourth = fourth_note

    def calculation (self):

        return self.note_first + self.note_second + self.note_third + self.note_fourth

result_division = calcular_media (first_note, second_note, third_note, fourth_note)

if result_division.calculation () / 4 > 5.5:

    os.system ('clear')
    print ('aluno aprovado!')
    time.sleep (1.5)
    os.system ('clear')

elif result_division.calculation () / 4 <= 5.5 and result_division.calculation () / 4 >= 4.5:

    os.system ('clear')
    print ('aluno aprovado pelo conselho de classe!')
    time.sleep (1.5)
    os.system ('clear')

elif result_division.calculation () / 4 >= 4.0 and result_division.calculation () / 4 < 4.5:

    os.system ('clear')
    print ('aluno em recuperação!')
    time.sleep (1.5)
    os.system ('clear')

elif result_division.calculation () / 4 < 4.0 and result_division.calculation () / 4 >= 0.0:

    os.system ('clear')
    print ('aluno reprovado!')
    time.sleep (1.5)
    os.system ('clear')

exit ()
