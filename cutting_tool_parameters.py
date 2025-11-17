import math
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        depthofcut = float(depth_entry.get())
        feedrate = float(feed_entry.get())
        cuttingspeed = float(speed_entry.get())
        diameter = float(diameter_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
        return

    spindle_speed = (1000 * cuttingspeed) / (math.pi * diameter)
    mrr = depthofcut * feedrate * spindle_speed
    spindle_result.config(text=f"Spindle Speed (N): {spindle_speed:.2f} rpm")
    mrr_result.config(text=f"Material Removal Rate (MRR): {mrr:.2f} mm³/min")
root = tk.Tk()
root.title("Cutting Tool Parameters Calculator")
root.geometry("400x350")
root.resizable(False, False)
tk.Label(root, text="Depth of Cut (mm):", font=("Arial", 12)).pack(pady=5)
depth_entry = tk.Entry(root, font=("Arial", 12))
depth_entry.pack()

tk.Label(root, text="Feed Rate (mm/rev):", font=("Arial", 12)).pack(pady=5)
feed_entry = tk.Entry(root, font=("Arial", 12))
feed_entry.pack()

tk.Label(root, text="Cutting Speed (m/min):", font=("Arial", 12)).pack(pady=5)
speed_entry = tk.Entry(root, font=("Arial", 12))
speed_entry.pack()

tk.Label(root, text="Tool/Workpiece Diameter (mm):", font=("Arial", 12)).pack(pady=5)
diameter_entry = tk.Entry(root, font=("Arial", 12))
diameter_entry.pack()

tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), command=calculate).pack(pady=15)

spindle_result = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
spindle_result.pack(pady=5)

mrr_result = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
mrr_result.pack(pady=5)

root.mainloop()
