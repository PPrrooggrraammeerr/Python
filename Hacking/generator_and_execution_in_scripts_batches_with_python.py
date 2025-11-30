
# coding: UTF-8

# generator_and_execution_in_scripts_batches_with_python.py

import os
import subprocess
import shutil
import time

script_batch_one = """@echo off
start taskmgr && exit
"""

script_batch_two = """@echo off
start notepad && exit
"""

script_batch_three = """@echo off
start explorer && exit
"""

scripts_batchs = {
    'script_batch_one.bat': script_batch_one,
    'script_batch_two.bat': script_batch_two,
    'script_batch_three.bat': script_batch_three
}

user_profile = os.getlogin ()
current_path = os.getcwd ()

for script_batch, content in scripts_batchs.items ():

    with open (script_batch, 'w') as file:
    
        file.write (content)
        time.sleep (0.5)

for script_batch in scripts_batchs:

    shutil.move (os.path.join (f'{current_path}', f'{script_batch}'), f'C:\\Users\\{user_profile}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    time.sleep (0.5)

for script_batch in scripts_batchs:

    execution_path = os.path.join (f'C:\\Users\\{user_profile}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup', f'{script_batch}')
    
    subprocess.run (['start', '', execution_path], shell=True)
    time.sleep (0.5)

for script_batch in scripts_batchs:

    removed_path = os.path.join (f'C:\\Users\\{user_profile}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup', f'{script_batch}')
    
    os.remove (f'{removed_path}')
    time.sleep (0.5)

exit ()
