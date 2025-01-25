from pynput.mouse import Listener
import time
import json

print("prepare for 4 seconds")
time.sleep(4)
print("4 seconds done ...")

# List to store mouse movements
mouse_movements = []

# Start time to calculate the time between movements
start_time = time.time()

# Function to record mouse movements
def on_move(x, y):
    current_time = time.time() - start_time
    mouse_movements.append({'time': current_time, 'x': x, 'y': y})

# Function to stop recording when the listener is stopped
def on_click(x, y, button, pressed):
    if not pressed:
        return False  # Stop listener when mouse is released

# Start the listener
with Listener(on_move=on_move, on_click=on_click) as listener:
    print("Recording mouse movements. Click to stop.")
    listener.join()

# Save the recorded data to a file
with open('mouse_movements.json', 'w') as f:
    json.dump(mouse_movements, f)
    print(f"Mouse movements recorded and saved to 'mouse_movements.json'")
