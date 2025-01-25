import time
import json
from pynput.keyboard import Controller, Key, KeyCode
from pynput.mouse import Controller as MouseController, Button

print("Prepare for 5 seconds")
time.sleep(5)

# Load Recorded Events
with open("recorded_events.json", "r") as file:
    recorded_events = json.load(file)

keyboard = Controller()
mouse = MouseController()

start_time = recorded_events[0]["time"]  # Get first event time

for event in recorded_events:
    time.sleep(event["time"] - start_time)  # Maintain correct timing
    start_time = event["time"]  # Update last event time

    if event["type"] == "keyboard":
        key_value = event["key"]

        # Convert key to KeyCode if it's a single character
        if len(key_value) == 1:  
            key_obj = KeyCode.from_char(key_value)
        elif key_value.startswith("Key."):  
            key_obj = getattr(Key, key_value.split("Key.")[1], None)
        else:
            key_obj = None  # Invalid key

        if key_obj:
            if event["event"] == "press":
                keyboard.press(key_obj)
            elif event["event"] == "release":
                keyboard.release(key_obj)

    elif event["type"] == "mouse":
        if event["event"] == "move":
            mouse.position = (event["x"], event["y"])
        elif event["event"] == "click":
            button = Button.left if event["button"] == "Button.left" else Button.right
            if event["pressed"]:
                mouse.press(button)
            else:
                mouse.release(button)

print("Playback Finished!")
