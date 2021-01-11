import time
from gpiozero import DistanceSensor

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