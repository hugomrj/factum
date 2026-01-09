import time

INTERVALO = 120  # segundos

def main():
    print("Daemon iniciado")

    while True:
        print("Ejecutando tarea...")
        
        # acá iría tu lógica real
        time.sleep(2)  # simula trabajo
        
        print("Tarea finalizada, durmiendo...")
        time.sleep(INTERVALO)

if __name__ == "__main__":
    main()
