from pynput.keyboard import Controller
import time
from pynput.mouse import Controller as MouseController, Button

keyboard = Controller()
mouse = MouseController()

def press_key_for_seconds(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

num = 0
while True:
    print("Pressing W for 3 seconds...")
    press_key_for_seconds('w', 1)
    
    print("Firing", num)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.click(Button.left, 1)
    num += 1

    print("Pressing A for 3 seconds...")
    press_key_for_seconds('a', 5)
