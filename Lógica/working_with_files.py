
# coding: UTF-8

# working_with_files.py

# O script fornecido apresenta uma ferramenta de gerenciamento de arquivos com múltiplas opções para trabalhar com arquivos.

import os
import shutil
import time
import subprocess
import sys

all_files = ['file.txt', 'elif.txt']
folder = 'folder'

for all_file in all_files:

    if os.path.exists (all_file):

        os.remove (all_file)

    else:

        pass

if os.path.isdir (folder):

    shutil.rmtree(folder, ignore_errors=True)

else:

    pass

while True:

    try:

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
        print ('\n* Copyright of Demétrio Freitas, 2022                                        *')
        print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
        print ('\n* https://github.com/PPrrooggrraammeerr/Python/workingwithfiles.py           *')
        print ('\n******************************************************************************')
        print ('\n')

        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        break

    except KeyboardInterrupt:

        subprocess.run (['clear'], shell=True)
        break

while True:

    def main ():

        try:

            print ('\n')
            print (' ' * 8 + ' ' + '=' * 41)
            print (' ' * 8 + '*' + ' ' * 8 + '1 - Create text file' + ' ' * 13  + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '2 - Create folder' + ' ' * 16  + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '3 - List all files and folders' + ' ' * 3 + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '4 - See current path' + ' ' * 13 + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '5 - Rename file' + ' ' * 18 + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '6 - Copy file' + ' ' * 20 + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '7 - Move file' + ' ' * 20 + '*')
            print (' ' * 8 + '*' + ' ' * 8 + '8 - Exit program' + ' ' * 17 + '*')
            print (' ' * 8 + ' ' + '=' * 41)
            print ('\n')

            Type_the_option = int (input ('Type the option: '))
            os.system ('clear')
            time.sleep (0.5)

            class files:

                def __init__ (self, Type_the_option):

                    self.working_with_files = Type_the_option

                def create_text_file (self):

                    text_file = open ('file.txt', 'w')
                    text_file.write ('Hello World!')

                def create_folder (self):

                    folder = os.makedirs ('folder')
                    print (folder)

                def list_files_and_folders (self):

                    files_and_folders = os.listdir ()

                    for file_and_folder in files_and_folders:

                        print (file_and_folder)

                def see_current_path (self):

                    current_path = os.getcwd ()
                    print (current_path)

                def rename_file (self):

                    text_file = open ('file.txt', 'w')
                    text_file.write ('Hello World!')

                    rename = os.rename ('file.txt', 'elif.txt')
                    print (rename)

                def copy_file (self):

                    text_file = open ('file.txt', 'w')
                    text_file.write ('Hello World!')

                    folder = os.makedirs ('folder')
                    print (folder)

                    shutil.copy ('file.txt', 'folder')

                def move_file (self):

                    text_file = open ('file.txt', 'w')
                    text_file.write ('Hello World!')

                    folder = os.makedirs ('folder')
                    print (folder)

                    shutil.move ('file.txt', 'folder')

                def exit_program (self):

                    subprocess.run (['clear'], shell=True)
                    time.sleep (0.5)
                    sys.exit ()
                    exit ()

            final_result = files (Type_the_option)

            if Type_the_option == 1:

                subprocess.run (['clear'])
                print (final_result.create_text_file ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 2:

                subprocess.run (['clear'], shell=True)
                print (final_result.create_folder ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 3:

                subprocess.run (['clear'], shell=True)
                print (final_result.list_files_and_folders ())
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 4:

                subprocess.run (['clear'], shell=True)
                print (final_result.see_current_path ())
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 5:

                subprocess.run (['clear'], shell=True)
                print (final_result.rename_file ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 6:

                subprocess.run (['clear'], shell=True)
                print (final_result.copy_file ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 7:

                subprocess.run (['clear'], shell=True)
                print (final_result.move_file ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

            elif Type_the_option == 8:

                subprocess.run (['clear'], shell=True)
                print (final_result.exit_program ())
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)
                exit ()

        except KeyboardInterrupt:

            subprocess.run (['clear'], shell=True)
            time.sleep (0.5)
            sys.exit ()
            exit ()

    if __name__ == '__main__':

        main ()

while True:

    os.system ('clear')
    time.sleep (0.5)
    sys.exit ()
    exit ()

