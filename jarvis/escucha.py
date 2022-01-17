import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init()

voices = engine.getProperty('voices')

print(voices)

engine.setProperty('voice', voices[1].id)
print(voices[2].id)

author = "Miguel"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Buenos dias {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Buenas tardes {author}")
    else:
        speak(f"Buenas noches {author}")

    speak(f"Hola {author} Me llamo Jarvis, Dime como puedo ayudarte")


def takecommand():
    """
    take microphone input from the user and return string
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='es-ES')
        print(f"User Said : {query}\n")
    except Exception as e:
        print(f"Sorry {author}, Say That again...")
        return "None"
    return query

if __name__ == "__main__":
    speak(f"Bienvenido {author}, Me llamo Jarvis")
    #wishMe()
    #takecommand()
    #if 1:
    #    query = takecommand().lower()
    #    if 'wikipedia' and 'who' in query:
    #        speak("Searching Wikipedia...")
    #        query = query.replace("wikipedia", "")
    #        results = wikipedia.summary(query, sentences = 2)
    #        speak("According to wikipedia")
    #        print(results)
    #        speak(results)