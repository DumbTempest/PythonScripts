import tkinter as tk
import pyautogui

saved_positions = []

def update_position():
    x, y = pyautogui.position()
    position_label.config(text=f"Mouse Position: ({x}, {y})")
    root.after(100, update_position)

def save_cord(event=None):
    x, y = pyautogui.position()
    saved_positions.append((x, y))
    update_saved_positions()

def update_saved_positions():
    saved_text = "\n".join([f"({x}, {y})" for x, y in saved_positions])
    saved_label.config(text=saved_text)

root = tk.Tk()
root.title("Mouse Coord Tracker")

position_label = tk.Label(root, text="Mouse Coord: (0, 0)", font=("Arial", 14))
position_label.pack(pady=15)

save_button = tk.Button(root, text="Save Coords", command=save_cord)
save_button.pack(pady=2)

saved_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
saved_label.pack(pady=10)

root.bind("<s>", save_cord)

update_position()
root.mainloop()
