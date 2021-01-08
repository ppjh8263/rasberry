import RPi.GPIO as GPIO
import picamera
import smtplib, subprocess, time, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

GPIO.setmode(GPIO.BCM)

PIR = 12
RLED = 21

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(RLED, GPIO.OUT)

camera = picamera.PiCamera()


print("System Working")
SMTP_USERNAME = '' # Gmail id of the sender
SMTP_PASSWORD = '' # Gmail Password of the sender
SMTP_RECIPIENT = '' # Mail id of the receiver
SMTP_SERVER = 'smtp.gmail.com' # Address of the SMTP server
SSL_PORT = 465

while True:
    try:
        if GPIO.input(PIR):
            print('Motion Detected')
            
            GPIO.output(RLED,1)
            camera.capture('./image0.jpg')
            time.sleep(1)
            GPIO.output(RLED,0)
            p = subprocess.Popen(["runlevel"], stdout=subprocess.PIPE)
            out, err = p.communicate()
            if out[2] == '0':
                print('Halt detected')
                exit(0)
            if out [2] == '6':
                print('Shutdown detected')
                exit(0)
            print("Connected to mail")
            # Create the container (outer) email message
            TO = SMTP_RECIPIENT
            FROM = SMTP_USERNAME
            
            #text
#             localtime = datetime.datetime.now()
#             strTime = localtime.strftime("%Y-%m-%d %H:%M")
#             msg = MIMEText('Motion Detected in RPi: '+strTime)#mail massage

            #msg['From'] = SMTP_RECIPIENT+'@gmail.com'
            
            #image
            fp = open('./image0.jpg','rb')
            msg = MIMEImage(fp.read())
            fp.close()

            
            msg['Subject'] = 'Raspi Noti'
            msg['To'] = SMTP_RECIPIENT
            # Send the email via Gmail
            print("Sending the mail")
            server = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            #server.send_message(msg)
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
            print("Mail sent")
        else:
            print('-')
        time.sleep(1)
    except IOError:
        print("Error")
        GPIO.cleanup()
        break
    except KeyboardInterrupt:
        print("Good Bye")
        GPIO.cleanup()
        break