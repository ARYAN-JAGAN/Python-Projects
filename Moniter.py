import psutil
import smtplib
from email.message import EmailMessage
import pywhatkit
from datetime import datetime

def runningOrNot(name):
    """
    This Function Checks Weather An App
    Is Running Or Not You Will Need To 
    Specify The Name Of Application In
    The Parameters
    """
    try:
        return f"{name}.exe" in (i.name() for i in psutil.process_iter()) 
    except:
        return False


def sendEmail(my_email,password,person,subject,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(my_email,password)
    email = EmailMessage()
    email["From"] = my_email
    email["To"] = person
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)

def what_message(person,message):
    pywhatkit.sendwhatmsg_instantly(person,message)

if __name__ == "__main__":
    while True:
        while True:
            current_time = datetime.now().strftime("%I:%M %p")
            if runningOrNot("chrome"):
                sendEmail(
                    "your_email",
                    "your_pasword",
                    "person_to_send_email",
                    "Bad News",
                    f"Your Brother Was Playing Games In Your Laptop At {current_time} Please Warn Him"
                    )
                break
            else:
                continue
    
