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

def set_duty_cycle(duty):
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)
    print(f"Duty cycle: {duty}%")

try:
    while True:
        # Ajuste manual del duty cycle para calibrar el servo
        duty = float(input("Ingrese el duty cycle (0-100): "))
        set_duty_cycle(duty)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
