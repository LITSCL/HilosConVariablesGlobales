from threading import Thread, Lock
import time

global_variable_1: int = 0
global_variable_2: int = 0
global_variable_3: int = 0

lock: object = Lock()

def funcion_1() -> None:
    while True:
        with lock:
            print("1", global_variable_1)
            print("2", global_variable_2)
            print("3", global_variable_3)
            print("--------------------")
        time.sleep(1)

def funcion_2() -> None:
    global global_variable_1, global_variable_2, global_variable_3
    while True:
        with lock:
            global_variable_1 += 1
            global_variable_2 += 1
            global_variable_3 += 1
        time.sleep(1)

hilo_1: object = Thread(target = funcion_1)
hilo_2: object = Thread(target = funcion_2)

hilo_1.start()
hilo_2.start()