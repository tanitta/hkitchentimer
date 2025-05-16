import time
import winsound

class KitchenTimer:
    def __init__(self, sound_path, threshold=5.0):
        self.threshold = threshold  # [sec]
        self.last_time = time.time()
        self.sound_path = sound_path

    def update(self):
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        if delta > self.threshold:
            self.notify(delta)

    def notify(self, duration):
        winsound.PlaySound(self.sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

