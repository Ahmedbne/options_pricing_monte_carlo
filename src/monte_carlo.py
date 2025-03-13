def monte_carlo_option_importance_sampling(S, K, T, r, sigma, num_simulations=10000, option_type="call"):
    """
    Monte Carlo simulation with Importance Sampling to price European options.

    Parameters:
    S: float - Current stock price
    K: float - Strike price
    T: float - Time to expiration (in years)
    r: float - Risk-free interest rate
    sigma: float - Volatility of the underlying asset
    num_simulations: int - Number of Monte Carlo simulations
    option_type: str - "call" or "put"

    Returns:
    float - Estimated option price with variance reduction
    """
    np.random.seed(42)

    mu_shift = (np.log(K / S) - (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))  # Shift mean
    Z = np.random.normal(mu_shift, 1, num_simulations)  # Sample from shifted distribution
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)  # Simulated prices

    if option_type == "call":
        payoff = np.maximum(ST - K, 0) * np.exp(-0.5 * (mu_shift**2) + mu_shift * Z)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0) * np.exp(-0.5 * (mu_shift**2) + mu_shift * Z)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    option_price = np.exp(-r * T) * np.mean(payoff)
    return option_price

if __name__ == "__main__":
    call_price = monte_carlo_option_importance_sampling(S, K, T, r, sigma, option_type="call")
    put_price = monte_carlo_option_importance_sampling(S, K, T, r, sigma, option_type="put")

    print(f"Monte Carlo with Importance Sampling - Call Price: {call_price:.4f}")
    print(f"Monte Carlo with Importance Sampling - Put Price: {put_price:.4f}")
