import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    np.random.seed(42)
    Z = np.random.standard_normal(num_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return np.exp(-r * T) * np.mean(payoff)

def monte_carlo_option_antithetic(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    np.random.seed(42)
    Z = np.random.standard_normal(num_simulations // 2)
    Z_antithetic = -Z  
    Z_combined = np.concatenate((Z, Z_antithetic))
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z_combined)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)

    return np.exp(-r * T) * np.mean(payoff)

def monte_carlo_option_importance_sampling(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    np.random.seed(42)
    mu_shift = (np.log(K / S) - (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    Z = np.random.normal(mu_shift, 1, num_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0) * np.exp(-0.5 * (mu_shift**2) + mu_shift * Z)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0) * np.exp(-0.5 * (mu_shift**2) + mu_shift * Z)

    return np.exp(-r * T) * np.mean(payoff)

def plot_monte_carlo_paths(S, T, r, sigma, num_simulations=1000, num_steps=252):
    np.random.seed(42)
    dt = T / num_steps
    paths = np.zeros((num_steps + 1, num_simulations))
    paths[0] = S

    for t in range(1, num_steps + 1):
        Z = np.random.standard_normal(num_simulations)
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    plt.figure(figsize=(10, 6))
    plt.plot(paths, alpha=0.5)
    plt.xlabel("Time Steps")
    plt.ylabel("Stock Price")
    plt.title(f"Monte Carlo Simulated Stock Price Paths ({num_simulations} simulations)")
    plt.show()
