import subprocess
import tkinter as tk
from tkinter import filedialog
import os

print("Made by ZethornDeath (https://github.com/ZethornDeath)")

def load_wad():
    wad_filename = filedialog.askopenfilename(filetypes=[("WAD Files", "*.wad")])
    if wad_filename:
        try:
            wad_filename = os.path.abspath(wad_filename)
            subprocess.run(["gzdoom.exe", "-file", wad_filename], check=True)
        except subprocess.CalledProcessError:
            error_label.config(text="Error: WAD file not found")
    else:
        error_label.config(text="No WAD file selected.")

app = tk.Tk()
app.title("GZDoom WAD Loader")

# Calculate the center of the screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 400  # Adjust this to your desired width
window_height = 120  # Adjust this to your desired height
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window's geometry
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

info_label = tk.Label(app, text="Select a WAD file to load with GZDoom:")
info_label.pack(pady=10)

note_label = tk.Label(app, text="(Make sure WADOpener is in the same folder as gzdoom.exe)")
note_label.pack()

load_button = tk.Button(app, text="Load WAD", command=load_wad)
load_button.pack(pady=5)

error_label = tk.Label(app, text="", fg="red")
error_label.pack(pady=10)

app.mainloop()
