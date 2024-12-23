import pygame
from gtts import gTTS
import os

class AudioController:
    def __init__(self):
        pygame.mixer.init()
        self.current_audio = None

    def play_audio(self, text):
        tts = gTTS(text)
        tts.save("temp.mp3")
        self.current_audio = "temp.mp3"
        pygame.mixer.music.load(self.current_audio)
        pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def resume_audio(self):
        pygame.mixer.music.unpause()

    def stop_audio(self):
        pygame.mixer.music.stop()
        if self.current_audio and os.path.exists(self.current_audio):
            os.remove(self.current_audio)
            self.current_audio = None

    def rewind_audio(self, seconds):
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(seconds)

    def forward_audio(self, seconds):
        current_pos = pygame.mixer.music.get_pos() / 1000.0
        pygame.mixer.music.set_pos(current_pos + seconds)