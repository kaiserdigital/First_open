import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hours_angle = (hours + minutes / 60) * 30
    minutes_angle = (minutes + seconds / 60) * 6
    seconds_angle = seconds * 6

    canvas.coords(hour_hand, 200, 200, 200 + 100 * math.cos(math.radians(hours_angle - 90)), 200 + 100 * math.sin(math.radians(hours_angle - 90)))
    canvas.coords(minute_hand, 200, 200, 200 + 150 * math.cos(math.radians(minutes_angle - 90)), 200 + 150 * math.sin(math.radians(minutes_angle - 90)))
    canvas.coords(second_hand, 200, 200, 200 + 180 * math.cos(math.radians(seconds_angle - 90)), 200 + 180 * math.sin(math.radians(seconds_angle - 90)))

    root.after(1000, update_clock)

root = tk.Tk()
root.title("Analoge Uhr")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.create_oval(50, 50, 350, 350)

for i in range(12):
    angle = math.radians(i * 30 - 90)
    x1 = 200 + 140 * math.cos(angle)
    y1 = 200 + 140 * math.sin(angle)
    x2 = 200 + 160 * math.cos(angle)
    y2 = 200 + 160 * math.sin(angle)
    canvas.create_line(x1, y1, x2, y2, width=2)

hour_hand = canvas.create_line(200, 200, 200, 100, width=6, fill="black")
minute_hand = canvas.create_line(200, 200, 200, 50, width=4, fill="blue")
second_hand = canvas.create_line(200, 200, 200, 20, width=2, fill="red")

update_clock()
root.mainloop()
