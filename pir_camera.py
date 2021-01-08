import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BCM)

PIR = 12
RLED = 21

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(RLED, GPIO.OUT)

camera = picamera.PiCamera()


while True:
    try:
        if GPIO.input(PIR):
            print('Motion Detected')
            
            GPIO.output(RLED,1)
            camera.capture('./image0.jpg')
            time.sleep(1)
            GPIO.output(RLED,0)
        else:
            print('-')
        time.sleep(1)
    except IOError:
        print("Error")
        GPIO.cleanup()
    except KeyboardInterrupt:
        print("Good Bye")
        GPIO.cleanup()