import tkinter as tk
from tkinter import messagebox
from black_scholes import black_scholes
from monte_carlo import monte_carlo_option_pricing

def calculate_option():
    try:
        S = float(entry_S.get())
        K = float(entry_K.get())
        T = float(entry_T.get())
        r = float(entry_r.get())
        sigma = float(entry_sigma.get())
        option_type = option_var.get()
        method = method_var.get()

        if method == "Black-Scholes":
            price = black_scholes(S, K, T, r, sigma, option_type)
        elif method == "Monte Carlo":
            price = monte_carlo_option_pricing(S, K, T, r, sigma, option_type=option_type)
        else:
            messagebox.showerror("Input Error", "Invalid pricing method selected.")
            return

        result_label.config(text=f"{method} {option_type.capitalize()} Price: {price:.4f}")
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

# Pricing Method Selection
method_var = tk.StringVar(value="Black-Scholes")
tk.Label(root, text="Pricing Method:").grid(row=7, column=0)
tk.Radiobutton(root, text="Black-Scholes", variable=method_var, value="Black-Scholes").grid(row=7, column=1)
tk.Radiobutton(root, text="Monte Carlo", variable=method_var, value="Monte Carlo").grid(row=8, column=1)

# Calculate button
calc_button = tk.Button(root, text="Calculate Price", command=calculate_option)
calc_button.grid(row=9, column=0, columnspan=2)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=10, column=0, columnspan=2)

root.mainloop()
