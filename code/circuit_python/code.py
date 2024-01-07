import board, time
import digitalio

motor1a = digitalio.DigitalInOut(board.GP8)
motor1a.direction = digitalio.Direction.OUTPUT

motor1b = digitalio.DigitalInOut(board.GP9)
motor1b.direction = digitalio.Direction.OUTPUT

motor2a = digitalio.DigitalInOut(board.GP10)
motor2a.direction = digitalio.Direction.OUTPUT

motor2b = digitalio.DigitalInOut(board.GP11)
motor2b.direction = digitalio.Direction.OUTPUT

def stop():
    motor1a.value = False
    motor1b.value = False
    motor2a.value = False
    motor2b.value = False

def forward():
    motor1a.value = False
    motor1b.value = True

    motor2a.value = True
    motor2b.value = False

def reverse():
    motor1a.value = True
    motor1b.value = False

    motor2a.value = False
    motor2b.value = True

def spin_right():
    motor1a.value = False
    motor1b.value = True

    motor2a.value = False
    motor2b.value = True

def spin_left():
    motor1a.value = True
    motor1b.value = False

    motor2a.value = True
    motor2b.value = False

while True:
    stop()
    time.sleep(1)
 
    forward()
    time.sleep(2)

    spin_right()
    time.sleep(2)

    spin_left()
    time.sleep(2)

    reverse()
    time.sleep(2)
