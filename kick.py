import time
from pynput.keyboard import Controller
# Removed mouse controller since it's no longer needed

# Initialize keyboard controller
keyboard = Controller()

# Configuration
initial_waiting_time = 2
ready_interval = 3  # Time between each action
num = 0

# Start countdown
print(f"Move to the game in {initial_waiting_time} seconds")
time.sleep(initial_waiting_time)

while True:
    print("Pressing E", num)
    keyboard.press('e')
    keyboard.release('e')
    time.sleep(1)
    
    keyboard.press('e')
    keyboard.release('e')
    time.sleep(ready_interval - 1)  # total of 10s between sets
    num += 1
