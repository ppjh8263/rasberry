import picamera
from time import sleep

camera = picamera.PiCamera()

camera.capture('./image1.jpg')
sleep(2)
camera.capture('./image2.jpg')