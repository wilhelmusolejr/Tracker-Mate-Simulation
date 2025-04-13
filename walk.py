from pynput.keyboard import Controller
import time
from pynput.mouse import Controller as MouseController, Button

keyboard = Controller()
mouse = MouseController()

# Configuration
initial_waiting_time = 10
print(f"Move to the game in {initial_waiting_time} seconds")
time.sleep(initial_waiting_time)

def press_key_for_seconds(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

num = 0
while True:
    print("Pressing W for 3 seconds...")
    press_key_for_seconds('w', 1)
    
    print("Firing", num)
    press_key_for_seconds('e', 1)
    time.sleep(1)

    print("Pressing A for 3 seconds...")
    press_key_for_seconds('a', 3)
    
    num += 1
