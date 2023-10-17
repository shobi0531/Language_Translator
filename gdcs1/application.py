from flask import Flask, render_template, request, send_file
import os
import gtts  # Google Text-to-Speech library

app = Flask(__name__)

# Define a dictionary of language codes and labels
supported_languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)",
    # Add more languages as needed
}


@app.route("/")
def index():
    return render_template("second.html", supported_languages=supported_languages)


@app.route("/convert", methods=["POST"])
def convert():
    text_to_convert = request.form.get("text-to-convert")
    lang_code = request.form.get("select-language-code")

    if text_to_convert:
        # Check if the selected language code is in the supported_languages dictionary
        if lang_code in supported_languages:
            # Use Google Text-to-Speech to convert text to speech
            tts = gtts.gTTS(text=text_to_convert, lang=lang_code)

            # Save the generated speech as an audio file
            audio_file = "output.mp3"
            tts.save(audio_file)

            return send_file(audio_file, as_attachment=True)  # Remove download_name

        else:
            return "Selected language is not supported."
    else:
        return "No text to convert."


if __name__ == "__main__":
    app.run(debug=True)
