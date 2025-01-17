import time
from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController, Button

# Initialize controllers
keyboard = Controller()
mouse = MouseController()

# Configuration
initial_waiting_time = 2
ready_location = (730, 430)  # Ready button position
ready_interval = 10  # Click the ready button every 10 seconds

# Start countdown
print(f"Move to the game in {initial_waiting_time} seconds")
time.sleep(initial_waiting_time)

print("Game started - Running in-game actions")
spam_key = 'w'  # Initial spam key
switch_time = time.time() + 5  # Switch every 5 seconds
next_ready_time = time.time() + ready_interval  # First ready button click time

while True:  
    keyboard.press(spam_key)
    keyboard.release(spam_key)
    print(f"Pressed {spam_key} key")

    time.sleep(0.1)  # Adjust spam speed

    # Switch between 'w' and 'a' every 5 seconds
    if time.time() >= switch_time:
        spam_key = 'a' if spam_key == 'w' else 'w'
        switch_time = time.time() + 5  # Reset switch time

    # Click the ready button every 10 seconds
    if time.time() >= next_ready_time:
        mouse.position = ready_location
        mouse.click(Button.left, 1)
        print("Pressed ready button")
        next_ready_time = time.time() + ready_interval  # Update next trigger time
