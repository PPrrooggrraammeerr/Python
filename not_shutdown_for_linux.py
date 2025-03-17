
# coding: UTF-8

# not_shutdown.py

# O script not_shutdown_for_linux.py utiliza um comando chamado xset com parâmetros e assim evita que o computador entre em modo de suspensão automática.

import time
import os

def prevent_sleep ():

    os.system ('xset s off')
    os.system ('xset -dpms')

prevent_sleep ()

while True:

    time.sleep (1.5)

