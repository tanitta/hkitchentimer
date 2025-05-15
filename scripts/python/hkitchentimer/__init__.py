import time
import winsound

class KitchenTimer:
    def __init__(self, threshold=5.0):
        self.threshold = threshold  # [sec]
        self.last_time = time.time()

    def update(self):
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        if delta > self.threshold:
            self.notify(delta)

    def notify(self, duration):
        winsound.PlaySound("C:\\Windows\\Media\\notify.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

