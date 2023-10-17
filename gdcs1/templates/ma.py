
from gtts import gTTS
import os
from langdetect import detect
from translate import Translator

# Text to be converted to speech
text = input("Enter the text you want to convert to speech: ")

# Detect the language of the input text
detected_language = detect(text)

# Select the desired language for translation
selected_language = input("Enter the language code (e.g., en for English, hi for Hindi): ")

# Use the 'translate' library to translate the text
translator = Translator(to_lang=selected_language, from_lang=detected_language)
translated_text = translator.translate(text)

# Specify the language code for text-to-speech
language = selected_language

# Passing the translated text and language to the engine for text-to-speech conversion
tts = gTTS(text=translated_text, lang=language, slow=False)

# Saving the converted audio in a file
tts.save("output.mp3")

# Playing the converted file
os.system("start output.mp3")  # On Windows
