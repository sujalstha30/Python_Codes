from gtts import gTTS 
text=("Abhilasha Shrestha is my Bestuuuuu.")
tts=gTTS(text=text,lang="en")
tts.save("audio.mp3")
print("Audio saved!")