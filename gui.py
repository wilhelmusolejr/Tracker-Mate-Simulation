import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, ttk
import threading
import time
import keyboard  # For global hotkeys
from record import start_listeners, save_to_file, recorded_events, recording_event  # Import the necessary functions
from play import play_recording  # Import playback function

stop_playback_flag = False

# Start recording function
def start_recording():
    # messagebox.showinfo("Info", "Recording started!")
    status_label.config(text="Status: Recording...")

    recording_event.set()  # Start recording

    def start_listening():
        recorded_events.clear()  # Clear previous recordings
        keyboard_listener, mouse_listener = start_listeners()
        while recording_event.is_set():
            time.sleep(0.1)
        keyboard_listener.stop()
        mouse_listener.stop()

    threading.Thread(target=start_listening, daemon=True).start()

# Stop recording function
def stop_recording():
    recording_event.clear()
    save_to_file()
    # messagebox.showinfo("Info", "Recording stopped!")
    status_label.config(text="Status: Recording stopped")
    
# Play recording function
def start_playback():
    global stop_playback_flag
    
    stop_playback_flag = False
    messagebox.showinfo("Info", "Playback starting in 3 seconds...")
    status_label.config(text="Status: Playing in 3 seconds...")
    root.update_idletasks()

    def delayed_start():
        global stop_playback_flag
        
        status_label.config(text="Status: Playing...")
        root.update_idletasks()

        def run_playback():
            global stop_playback_flag
            repeat_count = repeat_entry.get()

            for i in range(int(repeat_count)): 
                
                if stop_playback_flag:  # Check if stop flag is set
                    status_label.config(text="Status: Playback Stopped")
                    root.update_idletasks()
                    return  # Exit the playback loop if flag is set
                
                 
                status_label.config(text=f"Status: Playing... ({i + 1}/{repeat_count})")
                play_recording()
                root.update_idletasks()
                time.sleep(1)

            status_label.config(text="Status: Waiting...")
            stop_playback_flag = False
            root.update_idletasks()
            

        threading.Thread(target=run_playback, daemon=True).start()

    root.after(3000, delayed_start)

def stop_playback():
    global stop_playback_flag
    stop_playback_flag = True  # Set the flag to stop playback
    status_label.config(text="Status: Playback Stopped")

# GUI Setup
root = tk.Tk()
root.title("Track Mate | Keyboard & Mouse Recorder")
root.geometry("300x350")

# Keep the window always on top
root.attributes("-topmost", True)

# Configure the grid columns to allow buttons to expand and center
root.grid_columnconfigure(0, weight=1, minsize=300)  # Column 0 will center widgets

# Configure the rows to center the buttons in the middle
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Buttons (using grid, centered in the window)
tk.Button(root, text="F9 = Start Recording", command=start_recording).grid(row=0, column=0, pady=10, padx=10, sticky="ew", ipadx=10, ipady=5)
tk.Button(root, text="F10 = Stop Recording", command=stop_recording).grid(row=1, column=0, pady=10, padx=10, sticky="ew", ipadx=10, ipady=5)
tk.Button(root, text="F11 = Start Playback", command=start_playback).grid(row=3, column=0, pady=10, padx=10, sticky="ew", ipadx=10, ipady=5)
tk.Button(root, text="F12 = Stop Playback", command=stop_playback).grid(row=4, column=0, pady=10, padx=10, sticky="ew", ipadx=10, ipady=5)

root.grid_columnconfigure(0, weight=1, uniform="equal")
root.grid_columnconfigure(1, weight=1, uniform="equal")

# Input field for repeat count (using grid)
repeat_label = Label(root, text="Repeat Count:")
repeat_label.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

repeat_entry = Entry(root)
repeat_entry.insert(0, "1")
repeat_entry.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

repeat_entry.focus_set()  # Ensure the entry widget gets focus on startup

# Status label (using grid)
status_label = tk.Label(root, text="Status: Waiting", font=("Arial", 12))
status_label.grid(row=7, column=0, columnspan=2, pady=5)

# Status label (using grid)
status_label = tk.Label(root, text="Developed by TC.666", font=("Arial", 12))
status_label.grid(row=8, column=0, columnspan=2, pady=5)

# Register global hotkeys
keyboard.add_hotkey("f9", start_recording)
keyboard.add_hotkey("f10", stop_recording)
keyboard.add_hotkey("f11", start_playback)
keyboard.add_hotkey("f12", stop_playback)

# Run the GUI
root.mainloop()
