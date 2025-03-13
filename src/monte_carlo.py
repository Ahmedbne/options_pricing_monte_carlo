import numpy as np

def monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    """
    Monte Carlo simulation to price European options.

    Parameters:
    S: float - Current stock price
    K: float - Strike price
    T: float - Time to expiration (in years)
    r: float - Risk-free interest rate
    sigma: float - Volatility of the underlying asset
    num_simulations: int - Number of Monte Carlo simulations
    option_type: str - "call" or "put"

    Returns:
    float - Estimated option price
    """
    np.random.seed(42)  # For reproducibility
    Z = np.random.standard_normal(num_simulations)  # Generate random variables
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)  # Simulated terminal stock prices

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)  # Call option payoff
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)  # Put option payoff
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    option_price = np.exp(-r * T) * np.mean(payoff)  # Discounted expected payoff
    return option_price

if __name__ == "__main__":
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to expiry (1 year)
    r = 0.05  # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)

    call_price = monte_carlo_option_pricing(S, K, T, r, sigma, option_type="call")
    put_price = monte_carlo_option_pricing(S, K, T, r, sigma, option_type="put")

    print(f"Monte Carlo Call Price: {call_price:.4f}")
    print(f"Monte Carlo Put Price: {put_price:.4f}")
