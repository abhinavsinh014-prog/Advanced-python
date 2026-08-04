from gtts import gTTS

text = "Hello, this is a text-to-speech conversion using gTTS."

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

print("audio save successfully as output.mp3")
