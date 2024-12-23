# Page Player - Book Reader App

This project is a Python application that allows users to upload books in Word or PDF format and listen to them via audio playback. Users can control the audio with play, pause, rewind, and forward functionalities.

## Features

- Upload books in Word or PDF format.
- Convert uploaded files into a format suitable for audio reading.
- Text-to-speech functionality to read the book aloud.
- Audio playback controls: play, pause, rewind, and forward.

## Project Structure

```
# Page Player

Page Player is a Python application that allows you to upload a book in either Word or PDF format and have it read to you via audio. You can pause, play, rewind, and forward the audio.

## Project Structure

```plaintext
page-player
├── src
│   ├── main.py
│   ├── controllers
│   │   └── audio_controller.py
│   ├── services
│   │   └── file_service.py
│   ├── utils
│   │   └── audio_utils.py
│   ├── templates
│   │   ├── index.html
│   │   └── style.css
│   ├── static
│   │   └── script.js
├── requirements.txt
└── README.md

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/book-reader-app.git
   cd book-reader-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- Upload a book using the provided interface.
- Use the playback controls to listen to the book.
- Enjoy your reading experience!

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.