from flask import Flask, request, jsonify, render_template
from controllers.audio_controller import AudioController
import os

app = Flask(__name__)
audio_controller = AudioController()

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        # Process the file (convert to text, etc.)
        return jsonify({'message': 'File uploaded successfully', 'file': file.filename})
    return jsonify({'message': 'No file uploaded'}), 400

@app.route('/play', methods=['POST'])
def play_audio():
    # Play audio logic
    audio_controller.play_audio("Sample text to play")
    return '', 204

@app.route('/pause', methods=['POST'])
def pause_audio():
    audio_controller.pause_audio()
    return '', 204

@app.route('/rewind', methods=['POST'])
def rewind_audio():
    audio_controller.rewind_audio(10)  # Rewind by 10 seconds
    return '', 204

@app.route('/forward', methods=['POST'])
def forward_audio():
    audio_controller.forward_audio(10)  # Forward by 10 seconds
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)