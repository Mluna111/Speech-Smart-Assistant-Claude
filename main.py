# import speech_recognition as sr
# # Create a recognizer instance
# r = sr.Recognizer()
# # Path to your audio file (update this to your actual audio file's path)
# audio_file_path = "voice.wav"
# # Use the AudioFile class to work with the pre-recorded audio file
# with sr.AudioFile(audio_file_path) as source:
#     # Listen to the audio file
#     audio_data = r.record(source)
#     try:
#         # Use Google Speech Recognition
#         text = r.recognize_google(audio_data)
#         print("Recognized text:", text)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


import speech_recognition as sr
import anthropic
# Import the required module for text
# to speech conversion
from gtts import gTTS
import os

language = 'en'


# Create a recognizer instance
r = sr.Recognizer()

# # Create a recognizer instance
# audio_file_path = "voice.wav"
# # Use the AudioFile class to work with the pre-recorded audio file
# with sr.AudioFile(audio_file_path) as source:
#     # Listen to the audio file
#     audio_data = r.record(source)

#Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)


try:
    # Use Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)


    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="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",
    )

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        messages=[{"role": "user", "content": text}]
    )
    print(message.content[0].text)

    myobj = gTTS(text=message.content[0].text, lang=language, slow=False)

    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("mpg321 welcome.mp3")

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))




