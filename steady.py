import time
from pynput.keyboard import Controller, Key  # <-- Make sure Key is imported

keyboard = Controller()

def press_key_for_seconds(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

num = 0
while True:
    print(f"Pressing Enter... ({num})")
    press_key_for_seconds(Key.enter, 1)  # Use Key.enter for special keys
    time.sleep(10)
    num += 1
