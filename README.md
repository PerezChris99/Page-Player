# Page Player - Book Reader App

This project is a Python application that allows users to upload books in Word or PDF format and listen to them via audio playback. Users can control the audio with play, pause, rewind, and forward functionalities.

## Features

- Upload books in Word or PDF format.
- Convert uploaded files into a format suitable for audio reading.
- Text-to-speech functionality to read the book aloud.
- Audio playback controls: play, pause, rewind, and forward.

## Project Structure

```
book-reader-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── controllers
│   │   └── audio_controller.py # Manages audio playback
│   ├── services
│   │   └── file_service.py     # Handles file operations
│   └── utils
│       └── audio_utils.py      # Utility functions for audio processing
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in version control
```

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