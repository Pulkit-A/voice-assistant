from playsound import playsound
from gtts import gTTS
import os
import webbrowser
import random
from datetime import datetime, date
import wikipedia


class Command_hin:
    def discover(self, text):
        if text in ['namaste', 'radhe radhe', 'ram ram', 'radhe krishna', 'good morning', 'good afternoon', 'good evening']:
            self.respond(text)
        
        elif "time kya ho" in text or "time kitna" in text or "time bataiye" in text or "kitne baje gaye" in text or "kitna time" in text or "kitna time ho gaya" in text:
            now = datetime.now()
            answer = "Abhi time " + now.strftime("%H:%M:%S") + " hai."
            self.respond(answer)

        elif "bataiye" in text:
            text = text.replace("bataiye", "")
            wikipedia.set_lang('hi')
            results = wikipedia.summary(text, sentences=2)
            self.respond(results)

        elif "gane chalao" in text or "gana chalao" in text or "gana sunao" in text:
            webbrowser.open_new_tab('www.jiosaavn.com')
            self.respond('Aap yaha se gana chuniye')

        elif "google kariyo" in text or "google kariye" in text:
            text = text.replace("google kariyo", "")
            url = "https://www.google.co.in/search?q=" + text
            webbrowser.get().open(url)
            self.respond("Mujhe ye mila " + text + "ke liye")

        elif "kholo" in text:
            self.open_software(text)

        elif "kya" in text:
            if "naam" in text:
                if 'mera' in text:
                    self.respond("mujhe nhi pata.")
                else:
                    self.respond("mera naam Lucy hai.")

            elif "kar rahi hai" in text:
                self.respond("kuch nahi. tum bataao kya kar rhe ho. ")

            else:
                url = "https://www.google.co.in/search?q=" + text
                webbrowser.get().open(url)
                self.respond("Mujhe ye mila " + text + "ke liye")
        
        elif text in [""]:
            pass
        
        else:
            self.respond("ye command available nahi hai")

    def respond(self, response):
        voice = gTTS(text=response, lang='hi', slow=False)
        response_file = "response" + str(random.randint(0, 1000000)) + ".mp3"
        voice.save(response_file)
        print(response)
        playsound(response_file)
        os.remove(response_file)

    def open_software(self, text):
        if "youtube" in text:
            webbrowser.open_new_tab('www.youtube.com')
            self.respond('Youtube')
        
        elif "msword" in text or "ms-word" in text:
            self.respond("theek hai, Microsoft Word khol rahi hu")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')


        elif "excel" in text:
            self.respond("theek hai, Microsoft Excel khol rahi hu")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')

        elif "powerpoint" in text:
            self.respond("theek hai, Microsoft PowerPoint khol rahi hu")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007')
        
        elif "vs code" in text:
            self.respond("theek hai, Visual Studio Code khol rahi hu")
            os.startfile('C:\\Users\PULKIT\AppData\Local\Programs\Microsoft VS Code\Code')
        
        else:
            self.respond("Sorry, ye available nahi hai")

