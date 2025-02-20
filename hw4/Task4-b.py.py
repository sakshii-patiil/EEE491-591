import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        
        # Entry widget for displaying calculations
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('**', 5, 0), ('log', 5, 1), ('sin', 5, 2), ('cos', 5, 3)
        ]
        
        # Create buttons dynamically
        for (text, row, col) in buttons:
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), 
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))  # Evaluate the expression safely
            except:
                self.expression = "Error"
        elif char == "log":
            try:
                self.expression = str(math.log(float(self.expression)))
            except:
                self.expression = "Error"
        elif char == "sin":
            try:
                self.expression = str(math.sin(math.radians(float(self.expression))))
            except:
                self.expression = "Error"
        elif char == "cos":
            try:
                self.expression = str(math.cos(math.radians(float(self.expression))))
            except:
                self.expression = "Error"
        else:
            self.expression += char
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
