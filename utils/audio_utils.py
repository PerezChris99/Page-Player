def text_to_speech(text, output_file):
    from gtts import gTTS
    import os

    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    os.system(f"start {output_file}")  # For Windows, use 'open' for macOS

def manage_audio(action, audio_file=None):
    import pygame

    pygame.mixer.init()
    
    if action == 'play':
        if audio_file:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
    elif action == 'pause':
        pygame.mixer.music.pause()
    elif action == 'unpause':
        pygame.mixer.music.unpause()
    elif action == 'rewind':
        pygame.mixer.music.rewind()
    elif action == 'stop':
        pygame.mixer.music.stop()