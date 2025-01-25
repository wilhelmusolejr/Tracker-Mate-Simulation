import time
import json
from pynput import keyboard, mouse

recording = False  # Flag to track if recording is active
recorded_events = []
stop_script = False  # Flag to exit the script

# Record Keyboard Events
def on_press(key):
    global recording, stop_script
    try:
        key_value = key.char  # Get character key
    except AttributeError:
        key_value = str(key)  # Get special key as string

    # Start recording when F1 is pressed
    if key == keyboard.Key.f1:
        print("Recording started...")
        recorded_events.clear()  # Clear previous recordings
        recording = True
        return
    
    # Stop recording when F2 is pressed
    if key == keyboard.Key.f2:
        print("Recording stopped!")
        recording = False
        save_to_file()
        return

    # Exit script when ESC is pressed
    if key == keyboard.Key.esc:
        print("Exiting script...")
        stop_script = True
        return False  # Stops keyboard listener

    # Only record if active
    if recording:
        recorded_events.append({"type": "keyboard", "event": "press", "key": key_value, "time": time.time()})

def on_release(key):
    if recording:
        recorded_events.append({"type": "keyboard", "event": "release", "key": str(key), "time": time.time()})

# Record Mouse Events
def on_move(x, y):
    if recording:
        recorded_events.append({"type": "mouse", "event": "move", "x": x, "y": y, "time": time.time()})

def on_click(x, y, button, pressed):
    if recording:
        recorded_events.append({"type": "mouse", "event": "click", "x": x, "y": y, "button": str(button), "pressed": pressed, "time": time.time()})

# Save recorded data to file
def save_to_file():
    with open("recorded_events.json", "w") as file:
        json.dump(recorded_events, file, indent=4)
    print("Recording saved to recorded_events.json")

# Start Keyboard and Mouse Listeners
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

# Keep script running until ESC is pressed
while not stop_script:
    time.sleep(0.1)

keyboard_listener.stop()  # Stop listeners before exiting
mouse_listener.stop()
print("Script exited successfully.")
