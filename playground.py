from pynput.mouse import Controller
import time

# Create mouse controller
mouse = Controller()

# Simulate relative mouse movements
time.sleep(4)  # Wait to focus the game window

# Move mouse relative to the center of the screen
for i in range(100):
    mouse.move(10, 0)  # Move right by 10 pixels
    time.sleep(0.02)  # Adjust time for smoothness

    # You could adjust for more complex movement or add loops for continuous movements.
