import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
from newsapi import NewsApiClient
from openai import OpenAI

# Initialize the recognizer, text-to-speech engine, NewsAPI, and OpenAI API
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = NewsApiClient(api_key='1440ecbba6df40e69d6ce1fd423855b1')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_news():
    try:
        top_headlines = newsapi.get_top_headlines(language='en', country='us')
        articles = top_headlines['articles']
        if not articles:
            speak("Sorry, I couldn't find any news at the moment.")
            return

        speak("Here are the top news headlines:")
        for i, article in enumerate(articles[:5], 1):  # Reading top 5 headlines
            speak(f"Headline {i}: {article['title']}")
    except Exception as e:
        speak(f"Failed to fetch news: {e}")

def get_chatgpt_response(prompt):
    try:
        response = openai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            model="gpt-3.5-turbo"
        )
        return response.choices[0].message['content']
    except Exception as e:
        speak(f"Failed to get response from ChatGPT: {e}")
        return None

def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        sys.exit()

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        sys.exit()

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
        sys.exit()

    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
        sys.exit()

    elif "open amazon" in command:
        webbrowser.open("https://amazon.com")
        speak("Opening Amazon")
        sys.exit()

    elif "open reddit" in command:
        webbrowser.open("https://reddit.com")
        speak("Opening Reddit")
        sys.exit()

    elif "open wikipedia" in command:
        webbrowser.open("https://wikipedia.org")
        speak("Opening Wikipedia")
        sys.exit()

    elif "open github" in command:
        webbrowser.open("https://github.com")
        speak("Opening GitHub")
        sys.exit()

    elif "open stackoverflow" in command:
        webbrowser.open("https://stackoverflow.com")
        speak("Opening StackOverflow")
        sys.exit()

    elif "exit program" in command or "close program" in command or "stop program" in command:
        speak("Closing program. Goodbye!")
        sys.exit()

    elif "news" in command or "latest news" in command or "headlines" in command:
        get_news()
        sys.exit()

   
    else:
        speak("Sorry, I don't recognize that command.")
        sys.exit()

if __name__ == "__main__":
    speak("Firing up Money...")

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")
            if command.lower() == "money":
                speak("yes")

            with sr.Microphone() as source:
                print("Money activated..")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            command = recognizer.recognize_google(audio)
            
            process_command(command) 
            
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that.")
