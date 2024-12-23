from flask import Flask, request, render_template
from services.file_service import FileService
from controllers.audio_controller import AudioController

app = Flask(__name__)
file_service = FileService()
audio_controller = AudioController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file_path = file_service.upload_file(file)
    audio_controller.load_file(file_path)
    return 'File uploaded and ready for reading', 200

@app.route('/play', methods=['POST'])
def play():
    audio_controller.play()
    return 'Playing audio', 200

@app.route('/pause', methods=['POST'])
def pause():
    audio_controller.pause()
    return 'Audio paused', 200

@app.route('/rewind', methods=['POST'])
def rewind():
    audio_controller.rewind()
    return 'Audio rewinded', 200

@app.route('/forward', methods=['POST'])
def forward():
    audio_controller.forward()
    return 'Audio forwarded', 200

if __name__ == '__main__':
    app.run(debug=True)