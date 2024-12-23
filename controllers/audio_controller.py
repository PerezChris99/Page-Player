class AudioController:
    def __init__(self):
        self.is_playing = False
        self.current_position = 0

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            # Code to start audio playback
            print("Playing audio...")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            # Code to pause audio playback
            print("Audio paused.")

    def rewind(self, seconds):
        self.current_position -= seconds
        # Code to rewind audio playback
        print(f"Rewinding audio by {seconds} seconds.")

    def forward(self, seconds):
        self.current_position += seconds
        # Code to forward audio playback
        print(f"Forwarding audio by {seconds} seconds.")