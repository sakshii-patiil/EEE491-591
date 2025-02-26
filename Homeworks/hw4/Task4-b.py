from tkinter import *
import math

tk = Tk()
tk.title("Scientific Calculator")
tk.geometry("380x350")

entry = Entry(tk, width=25, font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10)

def on_button_click(value):
    current_text = entry.get()
    if value == "=":
        try:
            result = eval(current_text) 
            entry.delete(0, END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, END)  
    elif value == "log":
        try:
            result = math.log(float(current_text))
            entry.delete(0, END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif value == "sin":
        try:
            result = math.sin(math.radians(float(current_text)))
            entry.delete(0, END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif value == "cos":
        try:
            result = math.cos(math.radians(float(current_text)))
            entry.delete(0, END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, END)
            entry.insert(0, "Error")
    else:
        entry.insert(END, value)  

buttons = [
    ("7", "8", "9", "/", "**"),
    ("4", "5", "6", "*", "log"),
    ("1", "2", "3", "-", "sin"),
    ("C", "0", "=", "+", "cos"),
]

for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        Button(tk, text=char, width=5, height=2, font=("Arial", 14),
               command=lambda ch=char: on_button_click(ch)).grid(row=r, column=c, padx=5, pady=5)

tk.mainloop()