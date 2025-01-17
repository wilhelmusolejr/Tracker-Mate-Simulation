import time
import random


states = ['ingame', 'waiting']
initial_message = "waiting"
last_message = None

run_times = 1

while True:
  last_message = random.choice(states)
  
  if(last_message == "ingame"):
    print("Currently in game")
    time.sleep(10)
  
  if(last_message == "waiting"):
    print("Ready now")
    time.sleep(5)
  
  print(run_times)
  run_times += 1
  print("Bot running")
  print(last_message)

  