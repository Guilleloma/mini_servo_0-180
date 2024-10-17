import RPi.GPIO as GPIO
import time

# Configuración del pin de la Raspberry Pi
servo_pin = 12  # GPIO12 (PWM0)

# Configuración del modo de pin
GPIO.setwarnings(False)  # Desactivar advertencias de configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Configuración del PWM en el pin con una frecuencia de 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)  # Inicia el PWM con un duty cycle de 0

def set_angle(angle):
    # Ajuste para el SG90, basado en el datasheet
    # Duty cycle entre 2.5% (0 grados) y 12.5% (180 grados)
    duty = 2.5 + (angle / 180.0) * 10.0  # Interpolación lineal precisa para 0-180 grados
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.01)  # Pausa más corta para un movimiento más rápido
    print(f"Moviendo a {angle} grados (duty cycle: {duty}%)")

try:
    while True:
        # Movimiento de derecha a izquierda (135 a 45 grados) simulando un "no"
        for angle in range(135, 45, -1):
            set_angle(angle)
        # Movimiento de izquierda a derecha (45 a 135 grados) simulando un "no"
        for angle in range(45, 136):
            set_angle(angle)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
