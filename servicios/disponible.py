#!/usr/bin/env python3

import time
from datetime import datetime

LOG_FILE = "/tmp/disponible.log"


while True:
    hora_actual = datetime.now().strftime("%H:%M:%S")
    mensaje = f"Son las {hora_actual} y sigo disponible\n"
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(mensaje)
    except Exception as e:
        print(f"Error al escribir en el fichero: {e}")
        
    time.sleep(60)
