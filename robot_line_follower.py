from gpiozero import CamJamKitRobot, LineSensor
import time

pinLineFollower = 25

linesensor = LineSensor(pinLineFollower)
robot = CamJamKitRobot()

leftmotorspeed = 0.5
rightmotorspeed = 0.47

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, -rightmotorspeed)
motorright = (-leftmotorspeed, rightmotorspeed)

direction = True
isoverblack = True
linelost = False

def lineseen():
    global isoverblack, linelost
    print("The line has been found")
    isoverblack = True
    linelost = False
    robot.value = motorforward

def linenotseen():
    global isoverblack
    print("The line has been lost")
    isoverblack = False

def seekline():
    global direction, linelost
    robot.stop()

    print("Seeking the line")

    seeksize = 0.25
    seekcount = 1
    maxseekcount = 5

    while seekcount <= maxseekcount:
        seektime = seeksize * seekcount

        if direction:
            print("Looking left")
            robot.value = motorleft
        else:
            print("Looking right")
            robot.value = motorright

        starttime = time.time()

        while (time.time() - starttime) <= seektime:
            if isoverblack:
                robot.value = motorforward
                return True

        robot.stop()

        seekcount += 1

        direction = not direction
    
    robot.stop()
    print("The line has been lost - relocate your robot")
    linelost = True
    return False

linesensor.when_line = lineseen
linesensor.when_line = linenotseen

try:
    robot.value = motorforward
    while True:
        if not isoverblack and not linelost:
            seekline()

except KeyboardInterrupt:
    exit()