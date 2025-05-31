import speech_recognition as sr
from pydub import AudioSegment

# Convert M4A to WAV (if needed)
# audio_path = "/Users/shishir/Downloads/pioneer.m4a"
audio_wav = "/Users/shishir/Downloads/converted_audio.wav"
# AudioSegment.from_file(audio_path).export(audio_wav, format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_wav) as source:
    audio_data = recognizer.record(source)

print("Done Part 1")
# Perform speech recognition
# transcription = recognizer.recognize_google(audio_data)
transcription = recognizer.recognize_sphinx(audio_data)
print("Transcription:", transcription)
try:
    # transcription = recognizer.recognize_google(audio_data)
    print("Transcription:", transcription)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Error in the speech recognition service.")
