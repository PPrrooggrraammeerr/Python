
# coding: UTF-8

# start_the_XAMPP_with_Apache_and_MySQL.py

# O script start_the_XAMPP_with_Apache_and_MySQL.py automatiza o start de determinados processos presentes em uma lista, onde visa que, com base em seu conteúdo, se inicie todos os processos ou encerre o código.

import os
import time
import subprocess
import pyautogui

xampp_location_path = f'C:\\xampp\\'

list_of_process_with_xampp = ['xampp-control.exe', 'httpd.exe', 'mysqld.exe']

if os.path.exists (xampp_location_path) == True:
    
    def start_the_XAMPP_with_Apache_and_MySQL ():
    
        verify_process_of_xampp = subprocess.check_output (['tasklist']).decode ('latin1')
        
        for process_of_xampp in list_of_process_with_xampp:
    
            if all (process_of_xampp in verify_process_of_xampp for process_of_xampp in list_of_process_with_xampp):

                exit ()

            else:

                for process_of_xampp in list_of_process_with_xampp:
                
                    try:

                        subprocess.run (['taskkill', '/f', '/im', process_of_xampp], check=True)

                    except:                  
    
                        continue
                        
                os.startfile (xampp_location_path + 'xampp-control.exe')
                        
                pyautogui.moveTo (440, 140)
                time.sleep (1.5)
                pyautogui.click ()
                time.sleep (1.5)
                pyautogui.moveTo (440, 175)
                time.sleep (1.5)
                pyautogui.click ()
                time.sleep (1.5)
                pyautogui.keyDown ('alt')
                pyautogui.press ('f4')
                pyautogui.keyUp ('alt')
                exit()
                
    start_the_XAMPP_with_Apache_and_MySQL ()
    
else:

    exit ()

