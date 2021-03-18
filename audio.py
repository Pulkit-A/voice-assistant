import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from commands_hin import Command_hin
from commands_eng import Command_eng
import os
import random


def say(stext):
    voice = gTTS(text=stext, lang='en', slow=False)
    voice_file = "voice" + str(random.randint(0,1000000)) + ".mp3"
    voice.save(voice_file)
    playsound(voice_file)
    os.remove(voice_file)


r = sr.Recognizer()
lang = 0
standby = 0

def initSpeech():
    global standby
    global lang
    if lang == 0:
        cmd = Command_eng()
    else:
        cmd = Command_hin()
    
    if standby == 0:
        with sr.Microphone() as source:
            playsound('soft_notification.mp3')
            print("Listening...")
            audio = r.record(source, duration=4)

        command = ""

        try:
            command = r.recognize_google(audio, language="en-in")
            command = command.lower()
        except:
            pass

        print(f"Your Command: {command}")
        if command in ['quit', 'exit', 'bye', 'goodbye', 'bye bye']:
            say('Going offline. bye')
            exit()
        
        elif "activate english mod" in command:
            lang = 0
            say('English mode active')
        
        elif "hindi mein baat kare" in command or "hindi mein bole" in command:
            lang = 1
            say('hindi mode activate ho gaya')
        
        elif "lucy" in command and "rest" in command:
            standby = 1
            say("Ok sir, going to standby")
        
        else:
            cmd.discover(command)
    
    else:
        with sr.Microphone() as source:
            audio = r.record(source, duration=2)

        command = ""

        try:
            command = r.recognize_google(audio, language="en-in")
            command = command.lower()
        except:
            pass
        
        if "lucy" in command:
            standby = 0
            say('Listening')

say('Listening')
while True:
    initSpeech()
