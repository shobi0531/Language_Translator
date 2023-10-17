from flask import Flask, render_template, request
from translate import Translator
from langdetect import detect
from gtts import gTTS

app = Flask(__name__, template_folder="templates")

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

@app.route('/')
def index():
    return render_template('index.html', languages=scheduled_languages)

@app.route('/translate', methods=['POST'])
def translate():
    from_lang = request.form['selected_language_code_1']
    to_lang = request.form['selected_language_code_2']
    sentence = request.form['text_to_translate']

    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(sentence)

    return render_template('index.html', languages=scheduled_languages, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
