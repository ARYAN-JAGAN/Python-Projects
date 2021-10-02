from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyautogui
from time import sleep
from playsound import playsound
import pyjokes
import pprint 
from functools import cache
import requests
from fpdf import FPDF
from covid_india import states
from geopy.geocoders import Nominatim 
import os
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
import randfacts
import smtplib
from email.message import EmailMessage
import webbrowser


print(r"""

     ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗     █████╗ ██╗
     ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║
     ██║███████║██║     █████╔╝        ██║   ███████║█████╗      ███████║██║
██   ██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝      ██╔══██║██║
╚█████╔╝██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗    ██║  ██║██║
 ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝
                                                                                                                                                                                                
""")

global AI_Name

dictionary = PyDictionary()
r = sr.Recognizer()
engine = pyttsx3.init()

nospace = lambda value: value.replace(" ","")

def runJack():
    def say(what_to_say):
        engine.setProperty("rate",260)
        engine.say(what_to_say)
        engine.runAndWait()
    
    say("Activating The System.")
    say("initializing JAck dot  AI , version 3 point 9")
    
    def greet():
        currentTime = datetime.now()
        currentTime.hour

        if currentTime.hour < 12: 
            print('Good morning.')
            say("Good morning sir, how can i help you")
            
        elif 12 < currentTime.hour < 18: 
            print('Good afternoon.')
            say("Good afternoon sir, how can i help you")
            
        else: 
            print('Good evening.')
            say("Good evening sir, how can i help you")
    greet()        

    def takeCommand():
        try:
            with sr.Microphone() as source:  
                print("listening >>>")                     
                audio = r.listen(source)  
                order = r.recognize_google(audio, language="en-US").lower() 
                AI_name = "jack"               
                if AI_name in order:
                    order = order.replace(AI_name, "")
                    
        except Exception as e:
            print(e)    
            say(e) 
            
        return order    

    def microphone():
        try:
            with sr.Microphone() as source:  
                print("listening >>>")                     
                audio = r.listen(source)  
                order = r.recognize_google(audio, language="en-in").lower()                
                    
        except Exception as e:
            print(e)    
            say(e) 
            
        return order    
                
    def run_AI():
        order = takeCommand()
        global phone_num, text

        if ("play" or "can you play") in order:
            song = order.replace("play", "");
            say("Playing " + song)
            pywhatkit.playonyt(song)
            mick = microphone()

        elif "shut up" in order:
            exit()
            
        elif "some facts" in order:
            print(randfacts.getFact())
            say(randfacts.getFact())    

        elif "take screenshot after" in order:
            screen = pyautogui.screenshot()
            screen.save("screenRecord.jpg")

        elif "who is" in order:
            person = order.replace("who is", "")
            print(wikipedia.summary(person))
            say(wikipedia.summary(person))
            mick = microphone()
            if "stop" in mick:
                exit()

        elif "can i call you as" in order:
            AI_name = order.replace("can i call you as","")
            say("Ok sir you can call me as" + AI_name)

        elif "send message to" in order:

            if "mother" in order:
                phone_number = "9321697497"
                text = order.replace("send message to mother that", "")

            elif "father" in order:
                phone_number = "9892095438"
                text = order.replace("send message to father that", "")

            elif "alwin" in order:
                phone_number = "8080082962"
                text = order.replace("send message to alwin that", "")

            elif "dinesh" in order:
                phone_number = "8976008966"
                text = order.replace("send message to dinesh that", "")

            elif "joshua" in order:
                phone_number = "8169963550"
                text = order.replace("send message to joshua that", "")

            elif "kanchana teacher" in order:
                phone_number = "9967270550"
                text = order.replace("send message to tution teacher that", "")

            elif "rani teacher" in order:
                phone_number = "7506814021"
                text = order.replace("send message to tution teacher that", "")

            pywhatkit.sendwhatmsg_instantly(f"+91{phone_number}", f"{text}")

        elif "tell" and "about" in order:
            person = order.replace("tell me about", "")
            print(wikipedia.summary(person))
            say(wikipedia.summary(person))

        elif "shut down laptop in" in order:
            time = order.replace("shut down laptop in", "")
            say("shuting down laptop in" + time)
            time = int(time.replace("minutes", ""))
            seconds = time * 60
            os.system(f"shutdown -s -t {seconds}")

        elif "shutdown laptop at" in order:
            time_to_shut = order.replace("shut down laptop at","")
           
            while (1):
                current_time = datetime.datetime.now().strftime("%I%M")
                if (time_to_shut == current_time) :
                    os.system("shutdown -s -t 1")
                    break

        elif "what is " and "the weather in" in order:
            place = order.replace("what is the weather in", "")
            search = f"Weather in {place}"
            url = "https://www.google.com/search?&q=" + search
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            current_weather = soup.find("div", class_="BNeawe").text
            say("Current Temprature in" + place + " is " + current_weather)
            print(f"{search} now is {current_weather}")
        
        elif "todays" and ("headlines" or "headline") in order:
            url = "https://inshorts.com/en/read"
            r = requests.get(url)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            headlines = soup.find_all("span", itemprop="headline")
            say("Todays headlines are ")
            for headline in headlines:
                print(headline.text) 
                say(headline.text)    
        
        elif "turn on camera" in order:
            say("turning on camera")
            os.system("start microsoft.windows.camera:")

        elif "what is" and "your name" in order:
            say("My Name Is Jack i am your personal assistant")
        
        elif "print" in order:
            say("please enter, the path of file which you want to print")
            to_print = input("Enter The File Location : ")
            os.startfile(to_print, "print") 
                
        elif "a screenshot" in order:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot(1).jpg")
            say("Screenshoot has been taken")

        elif "increase brightness" in order:
            say("increasing brightness")
            pyautogui.press("f4")

        elif "decrease brightness" in order:
            say("decreasing brightness")
            pyautogui.press("f3")
        
        elif "todays" and "news" in order:
            url = "https://inshorts.com/en/read"
            r = requests.get(url)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            headlines = soup.find_all("span", itemprop="headline")
            say("Todays headlines are ")
            for headline in headlines:
                print(headline.text) 
                say(headline.text)    
                
        elif "what is the covid cases" and " in" in order:
            city = order.replace("what is the covid cases in", "").title()
            print(states.getdata(city))
            say(states.getdata(city))
                
        elif "create" and "pdf" in order:
            pdf = FPDF()
            say("What Is Should Be The Name Of Pdf")
            pdf_name = microphone()
            say("What Is The Content In PDF")
            pdf_content = microphone()
            pdf.add_page()
            pdf.set_font("Arial", size = 15)
            pdf.cell(200, 10, txt = pdf_content, ln = 2, align = 'C')
            pdf.output( pdf_name + ".pdf")   
            say("PDF HAS BEEN CREATED")
                
        elif "search for" in order:
            link = order.replace("search for", "") 
            say("searching for" + link)
            pywhatkit.search(link)   
            
        elif "repeat me" in order:
            user_said = order.replace("repeat me", "")
            say("you said " + user_said)
            
        elif "open whatsapp" in order:
            say("opening " + "whatsapp")    
            webbrowser.open("web.whatsapp.com/")   
            
        elif "open excel" in order:
            say("opening excel")
            os.startfile("excel")

        elif "what is the " and "temperature in" in order:
            try:
                place = order.replace("what is the temprature in", "")
                search = f"Weather in {place}"
                url = f"https://www.google.com/search?&q={search}"
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                current_weather = soup.find("div", class_="BNeawe").text
                say("Current Temprature in" + place + " is " + current_weather)
                print(f"{search} now is {current_weather}")
            except Exception as e:
                print(e)
                say(e)

        elif "switch off" in order:
            say("Ok Sir")
            exit()
            
        elif "open youtube" in order:
            webbrowser.open("youtube.com")  
        
        elif "open" and ("code" or "vs code" or "visual studio code") in order:
            os.system("code")
            
        elif "what is " and "the time" in order:
            say("Current time is " + datetime.now().strftime("%H %M %p"))     
            
        elif "where is" and "located" in order:
            area = order.replace("where is" and "located", "")
            print(area)
            def lonlat():
                app = Nominatim(user_agent="tutorial")
                location = app.geocode(area).raw
                pprint(location)
            lonlat()

        elif "some jokes" in order:
            print(pyjokes.get_joke())
            say(pyjokes.get_joke())
            
        elif ("restart " or "rebot") in order:
            os.system("shutdown/r")  
            
        elif "create a file " and "named" in order:
            f_name = order.replace("create a file named", "")
            f = open(f_name, "w")
            f.close()
            say("what to write in that file")
            mick = microphone()
            f = open(f_name, "w")
            f.write(mick)
            f.close()
            say("File has Been Created In PyProjects Folder")      

        elif "take photo" in order:
            os.system("start microsoft.windows.camera:")
            pyautogui.press("enter")

        elif "meaning of" in order:
            word = order.replace("what is meaning of", "")
            print(dictionary.meaning(word))
            say(dictionary.meaning(word))

        elif "ment by" in order:
            word = order.replace("what is ment by", "")
            print(dictionary.meaning(word))
            say(dictionary.meaning(word))
            
        elif "what is " and "ment by" in order:
            word = order.replace("what is ment by", "")   
            print(dictionary.meaning(word))
            say(dictionary.meaning(word))
            
        elif "opposite of" in order:
            word = order.replace("what is opposite of", "")     
            print(dictionary.meaning(word))
            say(dictionary.antonym(word))
        
        elif "antonym of" in order:
            word = order.replace("antonym of", "")  
            print(dictionary.meaning(word))
            say(dictionary.meaning(word))  

        elif "logoff" in order:
            say("sure sir")
            os.system("logoff")   

        elif "off wifi" in order:
            os.system('netsh interface set interface "Wi-Fi" disabled')  

        elif "send email to" in order:

            def sendEmail(receiver, subject, message):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email', 'your_password')
                email = EmailMessage()
                email['From'] = 'your_email'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)
                
            def getEmailInfo():
                person = nospace(order.replace("send email to",""))
                receiver = email_list[person]
                say("What Is The Subject Of Your Email")
                subject = microphone()
                say("What is The Message Of Your Email")
                message = microphone()
                sendEmail(receiver, subject, message)
                say("Hey Lazzy. Your email has been sent")
                say("do you want to send more")
                yesorno = microphone()
                if "yes" in yesorno:
                    getEmailInfo()
            
            getEmailInfo()

    while True:
        run_AI()

runJack() 
