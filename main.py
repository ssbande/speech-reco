import speech_recognition as sr
import os
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	os.system("say 'Say Something '")
	audio = r.listen(source)
	try:
		x = r.recognize_sphinx(audio)
		print("I think you said " + x)
		os.system("say " + x)
	except sr.UnknownValueError:
		print("I could not understand audio")
	except sr.RequestError as e:
		print("error; {0}".format(e))

	# try:
	# 	# for testing purposes, we're just using the default API key
	# 	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# 	# instead of `r.recognize_google(audio)`
	# 	print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
	# except sr.UnknownValueError:
	# 	print("Google Speech Recognition could not understand audio")
	# except sr.RequestError as e:
	# 	print("Could not request results from Google Speech Recognition service; {0}".format(e))


# import pyttsx
# speech_engine = pyttsx.init('nsss') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
# speech_engine.setProperty('rate', 150)

# def speak(text):
# 	speech_engine.say(text)
# 	speech_engine.runAndWait()


# speak("Say something!")