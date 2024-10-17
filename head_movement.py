import RPi.GPIO as GPIO
import time
import random

class HeadMovement:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)  # Configura PWM a 50 Hz
        self.pwm.start(7.5)  # Posición inicial (90 grados)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

    def set_angle(self, angle):
        # Ajuste para el SG90, basado en el datasheet
        duty = 2.5 + (angle / 180.0) * 10.0  # Interpolación lineal precisa para 0-180 grados
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.05)
        self.pwm.ChangeDutyCycle(0)
        print(f"Moviendo a {angle} grados (duty cycle: {duty}%)")

    def say_no(self):
        # Movimiento de decir "no"
        for angle in range(135, 45, -10):
            self.set_angle(angle)
        for angle in range(45, 135, 10):
            self.set_angle(angle)

    def casual_move(self):
        while True:
            angle = random.randint(45, 135)
            self.set_angle(angle)
            time.sleep(random.uniform(1, 3))
