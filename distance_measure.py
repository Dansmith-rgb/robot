import time
#from gpiozero import DistanceSensor
import socket
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

"""
def measure():
  
  start = time.time()

  stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance




# Define GPIO to use on Pi
GPIO_TRIGGER = 17
GPIO_ECHO = 18

print("Ultrasonic Measurement")

# Set pins as output and input
sensor = DistanceSensor(echo=GPIO_ECHO, trigger=GPIO_TRIGGER)

try:

    while True:

        distance = measure_average()
        print("Distance : %.1f" % sensor.distance)
        if sensor.distance < 1.0:
            print("object in the way of vehicle")
        time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  sensor.cleanup()

"""