import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, Checkbutton, BooleanVar
import threading
import time
from record import start_listeners, save_to_file, recorded_events, recording_event  # Import the necessary functions
from play import play_recording  # Import playback function


# Start recording function
def start_recording():
    messagebox.showinfo("Info", "Recording started!")
    status_label.config(text="Status: Recording...")

    # Set the recording event to signal recording should start
    recording_event.set()  # Start recording

    # Start the listeners in a separate thread to avoid blocking the main GUI
    def start_listening():
        recorded_events.clear()  # Clear previous recordings
        keyboard_listener, mouse_listener = start_listeners()
        while recording_event.is_set():  # Keep listening while recording event is set
            time.sleep(0.1)  # Keep the listeners running until the recording event is cleared
        keyboard_listener.stop()
        mouse_listener.stop()

    # Start the listeners in a separate thread
    recording_thread = threading.Thread(target=start_listening)
    recording_thread.daemon = True  # Ensures the thread will exit when the program ends
    recording_thread.start()

# Stop recording function
def stop_recording():
    messagebox.showinfo("Info", "Recording stopped!")
    status_label.config(text="Status: Recording stopped")

    # Clear the recording event to stop recording
    recording_event.clear()  # Stop recording
    save_to_file()  # Save recorded events to file

# Play recording function
def start_playback():
    messagebox.showinfo("Info", "Playback starting in 3 seconds...")

    # Update the label immediately to indicate waiting
    status_label.config(text="Status: Playing in 3 seconds...")
    root.update_idletasks()  # Force GUI update
    
    # Function to be called after the delay
    def delayed_start():
        # Start playback
        status_label.config(text="Status: Playing...")
        root.update_idletasks()  # Ensure the label is updated

        # Start the playback in a separate thread
        def run_playback():
            repeat_count = repeat_entry.get()

            # Loop for custom number of repeats or infinite loop
            for i in range(int(repeat_count)):  
                status_label.config(text=f"Status: Playing... ({i + 1}/{repeat_count})")
                play_recording()  # Call the playback function
                root.update_idletasks()  # Refresh GUI
                time.sleep(1)  # Short pause between repeats if needed    

            status_label.config(text="Status: Waiting...")  # Final status update
            root.update_idletasks()  # Refresh GUI after all repetitions

        # Start the playback thread
        threading.Thread(target=run_playback, daemon=True).start()

    # Delay playback start (non-blocking) using after method
    root.after(3000, delayed_start)  # Delay for 3 seconds before starting the playback

# Handle key press events for F1, F2, and F3
def on_key_press(event):
    if event.keysym == "F1":
        start_recording()
    elif event.keysym == "F2":
        stop_recording()
    elif event.keysym == "F3":
        start_playback()

# GUI Setup
root = tk.Tk()
root.title("Keyboard & Mouse Recorder")
root.geometry("300x250")  # Adjust the window size to fit the status text

# Keep the window always on top
root.attributes("-topmost", True)

# Bind F1, F2, F3 to start recording
root.bind("<F1>", on_key_press)
root.bind("<F2>", on_key_press)
root.bind("<F3>", on_key_press)

# Buttons
tk.Button(root, text="F1 = Start Recording", command=start_recording).pack(pady=10)
tk.Button(root, text="F2 = Stop Recording", command=stop_recording).pack(pady=10)
tk.Button(root, text="F3 = Play Recording", command=start_playback).pack(pady=10)

# Input field for repeat count
repeat_label = Label(root, text="Repeat Count:")
repeat_label.pack()
repeat_entry = Entry(root)
repeat_entry.insert(0, "1") 
repeat_entry.pack()

# Status label
status_label = tk.Label(root, text="Status: Waiting", font=("Arial", 12))
status_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
