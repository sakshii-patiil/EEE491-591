import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Constants
MAX_YEARS = 70

# Function to perform the wealth calculation and plotting
def calculate_wealth():
    try:
        r = float(entry_return.get())  # Mean return (%)
        sigma = float(entry_std_dev.get())  # Std dev return (%)
        Y = float(entry_contribution.get())  # Yearly contribution ($)
        years_contribute = int(entry_years_contribute.get())  # No. of years of contribution
        years_to_retirement = int(entry_years_retirement.get())  # No. of years to retirement
        S = float(entry_spend.get())  # Annual spend in retirement ($)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return
    
    if years_contribute > years_to_retirement:
        messagebox.showerror("Input Error", "Years of contribution cannot exceed years to retirement.")
        return
    
    np.random.seed(42)  # Fixed seed for reproducibility
    
    wealth_results = []
    plt.figure(figsize=(10, 5))
    
    for _ in range(10):  # Run 10 simulations
        noise = (sigma / 100) * np.random.randn(MAX_YEARS)
        wealth = np.zeros(MAX_YEARS + 1)  # Track wealth over 70 years
        
        for i in range(MAX_YEARS):
            if i < years_contribute:  # During contribution years
                wealth[i+1] = max(wealth[i] * (1 + r / 100 + noise[i]) + Y, 0)
            elif i < years_to_retirement:  # After contributions but before retirement
                wealth[i+1] = max(wealth[i] * (1 + r / 100 + noise[i]), 0)
            else:  # Retirement phase (withdrawals start)
                wealth[i+1] = max(wealth[i] * (1 + r / 100 + noise[i]) - S, 0)
                if wealth[i+1] == 0:
                    break  # Stop if wealth runs out
        
        wealth_results.append(wealth[years_to_retirement])
        plt.plot(range(i + 2), wealth[:i + 2], label=f"Run {_+1}")
    
    avg_wealth = sum(wealth_results) / len(wealth_results)
    label_result.config(text=f"Average Wealth at Retirement: ${avg_wealth:,.2f}")
    
    plt.xlabel("Years")
    plt.ylabel("Wealth")
    plt.title("Wealth Over 70 years")
    plt.legend()
    plt.grid()
    plt.show(block=False)

# GUI Setup
root = tk.Tk()
root.title("Wealth Calculator")

tk.Label(root, text="Mean Return (%)").grid(row=0, column=0)
tk.Label(root, text="Std Dev Return (%)").grid(row=1, column=0)
tk.Label(root, text="Yearly Contribution ($)").grid(row=2, column=0)
tk.Label(root, text="No. of Years of Contribution").grid(row=3, column=0)
tk.Label(root, text="No. of Years to Retirement").grid(row=4, column=0)
tk.Label(root, text="Annual Spend in Retirement ($)").grid(row=5, column=0)

entry_return = tk.Entry(root)
entry_std_dev = tk.Entry(root)
entry_contribution = tk.Entry(root)
entry_years_contribute = tk.Entry(root)
entry_years_retirement = tk.Entry(root)
entry_spend = tk.Entry(root)

entry_return.grid(row=0, column=1)
entry_std_dev.grid(row=1, column=1)
entry_contribution.grid(row=2, column=1)
entry_years_contribute.grid(row=3, column=1)
entry_years_retirement.grid(row=4, column=1)
entry_spend.grid(row=5, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate_wealth)
button_quit = tk.Button(root, text="Quit", command=root.quit)

button_calculate.grid(row=6, column=0)
button_quit.grid(row=6, column=1)

label_result = tk.Label(root, text="Average Wealth at Retirement: ")
label_result.grid(row=7, column=0, columnspan=2)

root.mainloop()
