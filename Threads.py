#-------------------------------------------------------------------
# Incluye bibliotecas necesarias
#-------------------------------------------------------------------
import threading
from time import sleep
#-------------------------------------------------------------------
# Inicializa variables globales
#-------------------------------------------------------------------
n_sem = 1
t_espera = 5
semaforo = threading.Semaphore(n_sem) # Inicializa el semaforo
#-------------------------------------------------------------------
# Definicion de una clase para un hilo (el proceso)
#-------------------------------------------------------------------
class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        print ("Hilo %s comienza a funcionar." %(self.id))
        semaforo.acquire()
        print ("Hilo %s entra a esta seccion." %(self.id))
        sleep(t_espera)
        semaforo.release()
        print ("Hilo %s finaliza funcionamiento." %(self.id))

# Funcion principal del programa
#-------------------------------------------------------------------
def main():
    print ("Iniciando programa ... ");
    hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6)] # define hilos
    for h in hilos: h.start() # Pone en marcha todos los hilos definidos
#-------------------------------------------------------------------
# Invocación de la funcion principal
#-------------------------------------------------------------------
main()