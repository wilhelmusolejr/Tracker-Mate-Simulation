import time
import json
from pynput import keyboard, mouse
import threading

recorded_events = []
stop_script = False  # Flag to exit the script

# Use threading Event for shared state between threads
recording_event = threading.Event()  # This will control recording state

# Record Keyboard Events
def on_press(key):
    try:
        if key == keyboard.Key.f2:  # Ignore F2 key
            return
        
        key_value = key.char  # Get character key
    except AttributeError:
        key_value = str(key)  # Get special key as string

    # Only record if active
    if recording_event.is_set():  # Check if the event is set (recording is active)
        recorded_events.append({"type": "keyboard", "event": "press", "key": key_value, "time": time.time()})

def on_release(key):
    if recording_event.is_set():  # Check if the event is set (recording is active)
        recorded_events.append({"type": "keyboard", "event": "release", "key": str(key), "time": time.time()})

# Record Mouse Events
def on_move(x, y):
    if recording_event.is_set():  # Check if the event is set (recording is active)
        recorded_events.append({"type": "mouse", "event": "move", "x": x, "y": y, "time": time.time()})

def on_click(x, y, button, pressed):
    if recording_event.is_set():  # Check if the event is set (recording is active)
        recorded_events.append({"type": "mouse", "event": "click", "x": x, "y": y, "button": str(button), "pressed": pressed, "time": time.time()})

# Save recorded data to file
def save_to_file():
    with open("recorded_events.json", "w") as file:
        json.dump(recorded_events, file, indent=4)
    print("Recording saved to recorded_events.json")

# Start listeners for keyboard and mouse
def start_listeners():
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()

    return keyboard_listener, mouse_listener
