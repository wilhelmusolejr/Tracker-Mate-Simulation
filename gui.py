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
    messagebox.showinfo("Info", "Recording started!")
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
    messagebox.showinfo("Info", "Recording stopped!")
    status_label.config(text="Status: Recording stopped")
    recording_event.clear()
    save_to_file()

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
root.title("Keyboard & Mouse Recorder")
root.geometry("300x300")

# Keep the window always on top
root.attributes("-topmost", True)

# Buttons
tk.Button(root, text="F1 = Start Recording", command=start_recording).pack(pady=10)
tk.Button(root, text="F2 = Stop Recording", command=stop_recording).pack(pady=10)

# Horizontal line (separator)
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

tk.Button(root, text="F3 = Start Playback", command=start_playback).pack(pady=10)
tk.Button(root, text="F4 = Stop Playback", command=stop_playback).pack(pady=10)

# Input field for repeat count
repeat_label = Label(root, text="Repeat Count:")
repeat_label.pack()
repeat_entry = Entry(root)
repeat_entry.insert(0, "1")
repeat_entry.pack()

# Status label
status_label = tk.Label(root, text="Status: Waiting", font=("Arial", 12))
status_label.pack(pady=10)

# Register global hotkeys
keyboard.add_hotkey("f1", start_recording)
keyboard.add_hotkey("f2", stop_recording)
keyboard.add_hotkey("f3", start_playback)
keyboard.add_hotkey("f4", stop_playback)

# Run the GUI
root.mainloop()
