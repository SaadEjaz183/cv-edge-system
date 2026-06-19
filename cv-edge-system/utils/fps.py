import time
from collections import deque

class FPSCounter:
    """Calculates a smooth rolling average FPS over the last N frames."""
    def __init__(self, window_size=30):
        self.timestamps = deque(maxlen=window_size)

    def update(self):
        now = time.time()
        self.timestamps.append(now)
        if len(self.timestamps) < 2:
            return 0.0
        elapsed = self.timestamps[-1] - self.timestamps[0]
        if elapsed <= 0:
            return 0.0
        return (len(self.timestamps) - 1) / elapsed