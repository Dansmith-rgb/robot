import pyttsx3
import speech_recognition as sr
from gpiozero import CamJamKitRobot, LineSensor
import time
import re

robot = CamJamKitRobot()

leftmotorspeed = 0.5
rightmotorspeed = 0.47

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, -rightmotorspeed)
motorright = (-leftmotorspeed, rightmotorspeed)

class Movement:

    def forward(self):
        speak("Moving robot forward")
        robot.value = motorforward

    def backward(self):
        speak("Moving robot backwards")
        robot.value = motorbackward

    def left(self):
        speak("Moving robot left")
        robot.value = motorleft

    def right(self):
        speak("Moving robot right")
        robot.value = motorright

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))

    return said.lower()

def main():
    print("Started Program")
    commands = Movement()
    END_PHRASE = "stop"
    result = None
    APPS = {
        re.compile("[\w\s]+ turn right"): commands.right,
        re.compile("turn right"): commands.right,
        re.compile("[\w\s]+ turn left"): commands.left,
        re.compile("turn left"): commands.left,
        re.compile("[\w\s]+ go forward"): commands.forward,
        re.compile("[\w\s]+ forward"): commands.forward,
        re.compile("forward"): commands.forward,
        re.compile("go forward"): commands.forward,
        re.compile("[\w\s]+ backwards [\w\s]"): commands.backward,
        re.compile("[\w\s]+ backwards"): commands.backward,
        re.compile("go backwards"): commands.backward,
    }

    while True:
        speak("Listening...")
        text = get_audio()

        for pattern, func in APPS.items():
            if pattern.match(text):
                result = func()
                break

        if result:
            speak(result)

        if text.find(END_PHRASE) != -1:
            speak("Stopping program")
            robot.stop()
            exit()

main()