import speech_recognition as sr
fi=("Kabira - Arijit Singh - 320Kbps.wav")
r=sr.Recognizer()
with sr.AudioFile(fi) as source:
    print("reading...")
    audio=r.record(source)
print("done with reading")
print("printing results")
print(r.recognize_google(audio))
