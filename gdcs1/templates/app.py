from flask import Flask, render_template, request, send_file
from gtts import gTTS
import io

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text_to_speech']
    tts = gTTS(text)
    audio_file = io.BytesIO()
    tts.save(audio_file)
    audio_file.seek(0)
    return send_file(audio_file, as_attachment=True, download_name='speech.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
