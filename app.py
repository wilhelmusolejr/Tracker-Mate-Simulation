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


num = 0
while True:
  print("Firing", num)
  mouse.click(Button.left, 1)
  time.sleep(1)
  mouse.click(Button.left, 1)
  num += 1