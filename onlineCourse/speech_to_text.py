import speech_recognition as sr
Audio_File = ("Donald Trump Speech - Never Ever Give Up.wav")
r = sr.Recognizer.__init__(Audio_File) #initialize the recognizer

with sr.AudioFile(Audio_File) as source:
    audio = r.record(source)
#reads the audio file

try:
    text = r.recognize_google(audio)
    print("Audio file Contains " + text)
except sr.UnknownValueError :    #exception is a type of error
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("Couldn't get the results from Google Speech Recognition")