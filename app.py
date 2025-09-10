import tkinter as tk

# --- Simulation Mode ---
arduino = None  # No USB/Arduino connected

def turn_on():
    if arduino:
        arduino.write(b'1')
    print("💡 LED ON (simulated)")

def turn_off():
    if arduino:
        arduino.write(b'0')
    print("💡 LED OFF (simulated)")

# --- Tkinter GUI ---
root = tk.Tk()
root.title("IoT LED Control")

label = tk.Label(root, text="Arduino not connected! (Simulation Mode)", fg="blue")
label.pack(pady=10)

btn_on = tk.Button(root, text="Turn LED ON", command=turn_on, width=20)
btn_on.pack(pady=5)

btn_off = tk.Button(root, text="Turn LED OFF", command=turn_off, width=20)
btn_off.pack(pady=5)

# Add a fake LED indicator
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()
led = canvas.create_oval(30, 30, 70, 70, fill="green")

def update_led(color):
    canvas.itemconfig(led, fill=color)

def turn_on_gui():
    turn_on()
    update_led("yellow")

def turn_off_gui():
    turn_off()
    update_led("green")

btn_on.config(command=turn_on_gui)
btn_off.config(command=turn_off_gui)

root.mainloop()
