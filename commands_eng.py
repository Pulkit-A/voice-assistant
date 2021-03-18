from playsound import playsound
from gtts import gTTS
import os
import webbrowser
import random
from datetime import datetime, date
import wikipedia


class Command_eng:
    def discover(self, text):
        if text in ['hello', 'hey', 'hi', 'yo', 'good morning', 'good afternoon', 'good evening']:
            self.respond(text)
        
        elif "what is the time" in text or "what time" in text or "tell time" in text or "tell me the time" in text or "current time" in text or "what's the time" in text:
            now = datetime.now()
            answer = "Time right now is  " + now.strftime("%H:%M:%S")
            self.respond(answer)

        elif "tell me about" in text:
            text = text.replace("tell me about", "")
            wikipedia.set_lang('en')
            results = wikipedia.summary(text, sentences=2)
            self.respond(results)

        elif "play music" in text or "play songs" in text or "play song" in text or "play a song" in text:
            webbrowser.open_new_tab('www.jiosaavn.com')
            self.respond('Here you can select for song')

        elif "google search" in text:
            text = text.replace("google search", "")
            url = "https://www.google.co.in/search?q=" + text
            webbrowser.get().open(url)
            self.respond("Here is what i found for " + text)
        
        elif "open" in text:
            self.open_software(text)

        elif "what" in text:
            if "name" in text:
                if 'my' in text:
                    self.respond("I don't know")
                else:
                    self.respond("My name is Lucy!")

            elif "doing" in text:
                self.respond("Nothing special. What you doing? ")

            else:
                url = "https://www.google.co.in/search?q=" + text
                webbrowser.get().open(url)
                self.respond("Here is what i found for " + text)
        
        elif text in [""]:
            pass
        
        else:
            self.respond("Command unavailable")

    def respond(self, response):
        voice = gTTS(text=response, lang='en', slow=False)
        response_file = "response" + str(random.randint(0, 1000000)) + ".mp3"
        voice.save(response_file)
        print(response)
        playsound(response_file)
        os.remove(response_file)
    
    def open_software(self, text):
        if "youtube" in text:
            webbrowser.open_new_tab('www.youtube.com')
            self.respond('Youtube is open')
        
        elif "ms word" in text or "ms-word" in text:
            self.respond("Ok, Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')


        elif "excel" in text:
            self.respond("Ok, Opening Microsoft Excel")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')

        elif "powerpoint" in text:
            self.respond("Ok, Opening Microsoft PowerPoint")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007')
        
        elif "vs code" in text:
            self.respond("Ok, Opening Visual Studio Code")
            os.startfile('C:\\Users\PULKIT\AppData\Local\Programs\Microsoft VS Code\Code')

        else:
            self.respond("Sorry, not available")