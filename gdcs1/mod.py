from translate import Translator

print("\nINDIAN LANGUAGE TRANSLATOR\n")

# List of 22 Scheduled Languages recognized by the Constitution of India
scheduled_languages = {
    "en": "English(India)",
    "gu-IN": "Gujarati(India)",
    "hi-IN": "Hindi(India)",
    "kn-IN": "Kannada(India)",
    "kok-IN": "Konkani(India)",
    "mr-IN": "Marathi(India)",
    "pa-IN": "Punjabi(India)",
    "sa-IN": "Sanskrit(India)",
    "ta-IN": "Tamil(India)",
    "te-IN": "Telugu(India)",
    "bn-IN": "Bengali(India)",
    "ur-IN": "Urdu(India)",
    "ml-IN": "Malayalam(India)",
    "or-IN": "Odia(India)",
    "as-IN": "Assamese(India)",
    "bo-IN": "Bodo(India)",
    "dog-IN": "Dogri(India)",
    "ka-IN": "Kashmiri(India)",
    "ma-IN": "Maithili(India)",
    "ne-IN": "Nepali(India)"
}

print("Available Languages:")
for lang_code, lang_name in scheduled_languages.items():
    print(f"{lang_code} {lang_name}")

say_lang = input("\nENTER THE LANGUAGE IN WHICH YOU ARE FAMILIAR WITH (ENTER THE LANG_CODE): ")
convert_lang = input("\nENTER THE LANGUAGE YOU WANT TO CONVERT INTO (ENTER THE LANG_CODE): ")
translator = Translator(from_lang=say_lang, to_lang=convert_lang)
sentence = input("\nENTER THE SENTENCE YOU WANT TO CONVERT INTO: ")
translation = translator.translate(sentence)
print("\nTranslation:")
print(translation)

