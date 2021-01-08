import picamera
from time import sleep

camera = picamera.PiCamera()

camera.start_preview()
for n in range(100):
    camera.brightness =n
    sleep(0.2)
camera.stop_preview()
