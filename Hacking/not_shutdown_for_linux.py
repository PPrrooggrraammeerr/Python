
# coding: UTF-8

# not_shutdown.py

# O script not_shutdown_for_linux.py utiliza o comando xset com parâmetros específicos para evitar que o computador entre automaticamente em modo de suspensão.

import time
import os

def prevent_sleep ():

    os.system ('xset s off')
    os.system ('xset -dpms')

prevent_sleep ()

while True:

    time.sleep (1.5)

