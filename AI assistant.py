import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes
import schedule
import time
from plyer import notification
import re

# Initialize pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

# Global list to store reminders
reminders = []

# Function to speak out the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to get the current time and speak it
def time_now():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is")
    speak(Time)

# Function to greet the user
def welcome():
    speak("You are very welcome")

# Function to get the current or future date
def date_now(offset=0):
    today = datetime.datetime.now() + datetime.timedelta(days=offset)
    year = today.year
    month = today.month
    day = today.day

    months = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    def get_day_suffix(day):
        if 10 <= day <= 20:
            return 'th'
        elif day % 10 == 1:
            return 'st'
        elif day % 10 == 2:
            return 'nd'
        elif day % 10 == 3:
            return 'rd'
        else:
            return 'th'

    day_suffix = get_day_suffix(day)

    if offset == 0:
        speak("Today's date is")
    elif offset < 0:
        speak("The date {} days ago was".format(-offset))
    else:
        speak("The date {} days from now will be".format(offset))

    speak(f"{day}{day_suffix} {months[month]} {year}")

# Function to greet the user based on the time of the day
def greeting():
    speak('Hello user.')

    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("It is a nice morning isn't it?") 
    elif 12 <= hour < 18:
        speak("It sure is one nice afternoon")
    elif 18 <= hour < 24:
        speak("What a good evening it is.")
    else:
        speak("Good night user")

    speak('I am your AI assistant. What are your plans')

# Function to recognize user's speech input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-us')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please..")

        return "None"
    return query

# Function to show notification reminders
def reminder(title):
    print(f"{title}: Time to {title.lower()}!")
    notification.notify(
        title=title,
        message=f"It's time for {title.lower()}!",
        app_name='My Application',
        timeout=5
    )

# Function to schedule a reminder
def schedule_reminder(title, schedule_time):
    schedule.every().day.at(schedule_time).do(reminder, title)

# Function to get user's speech input for setting reminders
def get_speech_input():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak your reminder title and time.")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return None

# Main function to control the assistant
def main():
    global reminders
    while True:
        schedule.run_pending()  # Check if any scheduled reminders are due
        query = take_command().lower()

        if 'time' in query:
            time_now()

        elif 'date' in query:
            date_now()

        elif 'thank you' in query:
            welcome()

        elif 'how are you' in query:
            speak("I am an AI assistant that is doing just fine. What do you need")

        elif 'go offline' in query:
            speak("Alright sure. Goodbye")
            quit()

        elif 'set a reminder' in query:
            speak("What should I remember?")
            title_and_time = get_speech_input()
            if title_and_time:
                try:
                    match = re.search(r'(\d{1,2})[:\.]?(\d{2})\s?(a\.?m\.?|p\.?m\.?)', title_and_time, re.IGNORECASE)
                    if match:
                        hour = int(match.group(1))
                        minute = int(match.group(2))
                        period = match.group(3).lower()
                        if period.startswith('p') and hour < 12:
                            hour += 12
                        elif period.startswith('a') and hour == 12:
                            hour = 0
                        time_str = f'{hour:02d}:{minute:02d}'
                        
                        title = re.sub(r'\s+at\s+' + match.group(0), '', title_and_time, flags=re.IGNORECASE)
                        
                        reminders.append({'title': title.strip(), 'time': time_str})
                        schedule_reminder(title.strip(), time_str)
                        speak(f"Reminder '{title.strip()}' scheduled for {time_str}")
                    else:
                        speak("Sorry, I couldn't recognize the time. Please try again.")
                except Exception as e:
                    speak(f"An error occurred: {e}")

        elif 'do i have any reminders' in query:
            for reminder in reminders:
                speak(f"You have a reminder for '{reminder['title']}' at {reminder['time']}")

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 

if __name__ == "__main__":
    greeting()
    main()
    schedule.every().minute.do(main)  # Schedule main function to run every minute
    while True:
        schedule.run_pending()
        time.sleep(1)
