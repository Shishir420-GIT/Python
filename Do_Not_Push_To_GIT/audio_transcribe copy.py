import speech_recognition as sr
from pydub import AudioSegment

# Convert M4A to WAV (if needed)
audio_path = "/Users/shishir/Downloads/pioneer.m4a"
audio_wav = "/Users/shishir/Downloads/converted_audio.wav"

with sr.AudioFile(audio_wav) as source:
    recognizer = sr.Recognizer()
    for chunk in range(0, int(source.DURATION), 30):  # 10 sec chunks
        audio_chunk = recognizer.record(source, duration=10)
        print(recognizer.recognize_google(audio_chunk))
        # print(recognizer.recognize_sphinx(audio_chunk)) # definately wrong
