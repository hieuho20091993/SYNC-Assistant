import speech_recognition
import pyttsx3
from googletrans import Translator
import random

# Setup
sync_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)
running = True

#Starting
sync_brain = "Hello. I am Sync Translator"
engine.say (sync_brain)
engine.runAndWait()

while running:
	# Listening
	with speech_recognition.Microphone() as mic:
		engine.say ("I am ready")
		engine.runAndWait()
		print ("Sync is listening...")
		audio = sync_ear.listen(mic)
	try: 
		user = sync_ear.recognize_google(audio)
	except:
		user = ""

	# Understanding
	if user == "":
		sync_brain = "I cannot hear you, please speak louder"
		engine.say (sync_brain)
		engine.runAndWait()
	else:
		print(user)
		translator = Translator()
		translated_sentence = translator.translate(user, src='en', dest='vi')
		print (translated_sentence.text)
	user_answer = input("Do you want to continue? Yes or No ? ")
	while user_answer not in ("yes", "no", "Yes", "No"):
		user_answer = input ("Enter yes or no ")
	user_answer.lower()
	if user_answer == "no":
		print ("Thank you, good luck")
		break

	




	


#Understanding and output

