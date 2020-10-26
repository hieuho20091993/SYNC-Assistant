import speech_recognition

sync_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print ("Syns is listening")
	audio = sync_ear.listen(mic)
user = sync_ear.recognize_google(audio)
print(user)
