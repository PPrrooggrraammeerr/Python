
# coding: UTF-8

# not_shutdown.py

# O script not_shutdown_for_windows.py utiliza a biblioteca ctypes para fazer uma chamada à API do Windows e prevenir que o computador entre em modo de suspensão automática.

import ctypes
import time
import os

def prevent_sleep ():

    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    
    ctypes.windll.kernel32.SetThreadExecutionState (
        
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED

    )

prevent_sleep ()

while True:

    time.sleep (1.5)

