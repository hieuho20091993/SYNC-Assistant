import speech_recognition
import pyttsx3
import random
from datetime import date, datetime

#setup
sync_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)

#start the conversation
user_start = ["hello", "hey", "how are you doing", "hi"]
sync_start = ["how are you doing", "hello", "hi"]


#finish the conversation
user_exit = ["bye", "I am done", "I'm done", "that's all for today", "no thank you"]
sync_exit = ["bye, have a nice day", "ok good luck", "goodbye"]

#Starting
sync_brain = "Hello. I am Sync."
engine.say(sync_brain)
engine.runAndWait()

while True:
# Listening
	with speech_recognition.Microphone() as mic:
		engine.say ("May I help you")
		engine.runAndWait()
		print ("Sync is listening...")
		audio = sync_ear.listen(mic)
	try: 
		user = sync_ear.recognize_google(audio)
		print (user)
	except:
		user = ""

	# Understanding
	if user in user_start:
		if user == "how are you doing":
			sync_brain = "I'm doing great. Thank you"
		else:
			sync_brain = random.choice(sync_start)
	elif "how are you" in user:
		sync_brain = "I am fine, thank you."
	elif "your name" in user:
		sync_brain = "My name is Sync"
	elif "ask you" in user:
		sync_brain = "This is my pleasure"
	elif "date" in user:
		today = date.today()
		current_day = today.strftime("%A %B %d, %Y")
		sync_brain = "Today is " + str(current_day)
	elif "time" in user:
		time = datetime.now()
		sync_brain = time.strftime("%H hours %M minutes %S seconds")
	elif "united states" and "president" in user:
		sync_brain = "Donald Trump"
	elif "united states" and "capital" in user:
		sync_brain = "Washington D.C"
	elif user == "":
		sync_brain = "I cannot hear you, please speak louder"
	elif user in user_exit:
		sync_brain = random.choice(sync_exit)
		engine.say (sync_brain)
		engine.runAndWait()
		break

	# Speaking
	engine.say (sync_brain)
	engine.runAndWait()



