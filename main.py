
import speech_recognition as sr
import anthropic
# Import the required module for text
# to speech conversion
from gtts import gTTS
import os

language = 'en-us'


# Create a recognizer instance
r = sr.Recognizer()

#Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    # Use Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)
    text = "Answer the questions in 90 words or less: " + text

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="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",
    )

    message = client.messages.create(
        #model="claude-3-opus-20240229",
        model="claude-3-haiku-20240307",
        max_tokens=200,
        temperature=0,
        messages=[{"role": "user", "content": text}]
    )
    print(message.content[0].text)

    #system(message.content[0].text)

    myobj = gTTS(text=message.content[0].text, lang=language, slow=False)

    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("mpg321 welcome.mp3")

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

