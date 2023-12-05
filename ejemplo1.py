from threading import Thread
import time

global_variable_1: str = None
global_variable_2: str = None
global_variable_3: str = None

def funcion_1() -> None:
    while (True):
        print("1", global_variable_1)
        print("2", global_variable_2)
        print("3", global_variable_3)
        print("--------------------")
        time.sleep(1)

def funcion_2() -> None:
    global global_variable_1 #Permite que la modificación de la variable sea visible fuera del hilo.
    global_variable_1 = "Dato cambiado"
    global_variable_2 = "Dato cambiado"
    global_variable_3 = "Dato cambiado"

hilo_1: object = Thread(target = funcion_1)
hilo_2: object = Thread(target = funcion_2)

hilo_1.start()
hilo_2.start()

