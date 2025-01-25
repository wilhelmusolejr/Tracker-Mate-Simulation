from pynput.mouse import Controller
import time
import json

print("prepare for 4 seconds")
time.sleep(4)
print("4 seconds done ...")

# Load recorded mouse movements
with open('mouse_movements.json', 'r') as f:
    mouse_movements = json.load(f)

# Create a mouse controller to move the mouse
mouse = Controller()

# Play the recorded movements
start_time = time.time()

for movement in mouse_movements:
    # Calculate the time to wait before moving to the next position
    elapsed_time = movement['time'] - (time.time() - start_time)
    
    # Ensure the sleep time is non-negative
    if elapsed_time > 0:
        time.sleep(elapsed_time)
    
    # Move the mouse to the recorded position
    mouse.position = (movement['x'], movement['y'])
    print(f"Moving mouse to: {movement['x']}, {movement['y']}")
    
print("Playback finished.")
