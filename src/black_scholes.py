import numpy as np
import scipy.stats as si

def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Black-Scholes price of a European option.

    Parameters:
    S: float - Current stock price
    K: float - Strike price
    T: float - Time to expiration (in years)
    r: float - Risk-free interest rate
    sigma: float - Volatility of the underlying asset
    option_type: str - "call" or "put"

    Returns:
    float - Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * si.norm.cdf(-d2) - S * si.norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return price

if __name__ == "__main__":
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to expiry (1 year)
    r = 0.05  # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)

    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")

    print(f"Call Price: {call_price:.4f}")
    print(f"Put Price: {put_price:.4f}")