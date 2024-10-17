import RPi.GPIO as GPIO
import time
import random

# Configuración del pin de la Raspberry Pi
servo_pin = 12  # GPIO12 (PWM0)

# Configuración del modo de pin
GPIO.setwarnings(False)  # Desactivar advertencias de configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Configuración del PWM en el pin con una frecuencia de 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7.5)  # Inicia el PWM con un duty cycle de 7.5% (posición central)

def set_angle(angle):
    # Ajuste para el SG90, basado en el datasheet
    # Duty cycle entre 2.5% (0 grados) y 12.5% (180 grados)
    duty = 2.5 + (angle / 180.0) * 10.0  # Interpolación lineal precisa para 0-180 grados
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)  # Detiene el ciclo PWM
    print(f"Moviendo a {angle} grados (duty cycle: {duty}%)")

try:
    while True:
        # Generar un ángulo aleatorio entre 45 y 135 grados (±45 grados alrededor de 90)
        angle = random.randint(0, 180)
        set_angle(angle)
        # Esperar un tiempo aleatorio entre 1 y 3 segundos antes de moverse nuevamente
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
