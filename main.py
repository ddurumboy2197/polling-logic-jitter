import random
import time

class PollingLogic:
    def __init__(self, jitter_range):
        self.jitter_range = jitter_range
        self.last_request_time = time.time()

    def jitter(self):
        return random.uniform(-self.jitter_range, self.jitter_range)

    def poll(self):
        current_time = time.time()
        jitter = self.jitter()
        delay = max(0, self.jitter_range - jitter)
        time.sleep(delay)
        return current_time - self.last_request_time

    def update_last_request_time(self):
        self.last_request_time = time.time()

def create_polling_logic(jitter_range):
    return PollingLogic(jitter_range)

def main():
    jitter_range = 0.5  # 0.5 second
    polling_logic = create_polling_logic(jitter_range)

    while True:
        delay = polling_logic.poll()
        print(f"Delay: {delay} seconds")
        polling_logic.update_last_request_time()

if __name__ == "__main__":
    main()
