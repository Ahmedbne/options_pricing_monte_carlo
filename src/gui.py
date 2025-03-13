import tkinter as tk
from tkinter import messagebox
from black_scholes import black_scholes

def calculate_option():
    try:
        S = float(entry_S.get())
        K = float(entry_K.get())
        T = float(entry_T.get())
        r = float(entry_r.get())
        sigma = float(entry_sigma.get())
        option_type = option_var.get()

        price = black_scholes(S, K, T, r, sigma, option_type)
        result_label.config(text=f"{option_type.capitalize()} Option Price: {price:.4f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("Option Pricing Calculator")

# Input fields
tk.Label(root, text="Stock Price (S):").grid(row=0, column=0)
entry_S = tk.Entry(root)
entry_S.grid(row=0, column=1)

tk.Label(root, text="Strike Price (K):").grid(row=1, column=0)
entry_K = tk.Entry(root)
entry_K.grid(row=1, column=1)

tk.Label(root, text="Time to Expiry (T in years):").grid(row=2, column=0)
entry_T = tk.Entry(root)
entry_T.grid(row=2, column=1)

tk.Label(root, text="Risk-free Rate (r):").grid(row=3, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=3, column=1)

tk.Label(root, text="Volatility (sigma):").grid(row=4, column=0)
entry_sigma = tk.Entry(root)
entry_sigma.grid(row=4, column=1)

# Option Type Selection
option_var = tk.StringVar(value="call")
tk.Label(root, text="Option Type:").grid(row=5, column=0)
tk.Radiobutton(root, text="Call", variable=option_var, value="call").grid(row=5, column=1)
tk.Radiobutton(root, text="Put", variable=option_var, value="put").grid(row=6, column=1)

# Calculate button
calc_button = tk.Button(root, text="Calculate Price", command=calculate_option)
calc_button.grid(row=7, column=0, columnspan=2)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
