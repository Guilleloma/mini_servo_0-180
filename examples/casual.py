import sys
import os
import time

# Añadir el directorio padre al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from head_movement import HeadMovement

def main():
    servo_pin = 12  # Usa el pin GPIO 12
    head = HeadMovement(servo_pin)
    
    try:
        print("Iniciando el movimiento casual de la cabeza...")
        head.casual_move()  # Ejecuta el movimiento casual de la cabeza
    except KeyboardInterrupt:
        head.cleanup()
        print("Limpieza y apagado.")

if __name__ == "__main__":
    main()
