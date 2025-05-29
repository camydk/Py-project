#!/usr/bin/env python3

import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result_label.config(text=response.text)
        else:
            result_label.config(text="Failed to fetch weather info.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Weather Checker")
root.geometry("300x150")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
