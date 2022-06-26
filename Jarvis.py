import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12 :
		speak("Good Morning Dear")
	elif hour>=12 and hour<18 :
		speak("Good After noon Dear")
	else:
		speak("Good Evening Dear")

	speak("Hi this is Jarvis. Please tell me How I can help you")


def takeCommand():
	#it takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		# print(e)

		print("Say that again please...")
		return "None"
	return query

if __name__ == "__main__":
	wishMe()

	while True:
		query = takeCommand().lower() 

		if 'wikipedia' in query:
			speak('Searching wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to wikipedia")
			speak(results)
			print(results)

		elif 'thankyou jarvis' in query:
			speak("Welcome!")

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			music_dir = 'D:\\Music'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"The time is {strTime}")
			print(f"The time is {strTime}")

		elif 'how are you' in query:
			speak("I am fine. What about you?")

		elif 'open sublime' in query:
			codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(codePath)

		elif 'quit' in query:
			exit()

		
