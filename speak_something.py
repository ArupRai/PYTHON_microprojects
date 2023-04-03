# 1st method
import pyttsx3
if __name__ == '__main__' :
    engine = pyttsx3.init()
    engine.say("Haare krishna")
    engine.runAndWait()
    engine.stop()
# 2nd method using os module
# import os