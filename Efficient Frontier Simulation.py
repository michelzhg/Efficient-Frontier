import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Number of assets and observations (simulated data)
number_assets = 4
number_observations = 1000

# Generate random returns for 4 assets
returns = np.random.randn(number_observations, number_assets)

# Calculate mean returns and covariance matrix
mean_returns = np.mean(returns, axis=0)
cov_matrix = np.cov(returns.T)

# Number of simulated portfolios
number_portfolios = 5000

# Initialize arrays to store portfolio volatility, returns, and Sharpe ratio
results = np.zeros((3, number_portfolios))
weights_record = []

for i in range(number_portfolios):
    # Generate random weights for each asset and normalize them
    weights = np.random.random(number_assets)
    weights /= np.sum(weights)
    weights_record.append(weights)

    # Calculate portfolio return
    portfolio_return = np.sum(mean_returns * weights)

    # Calculate portfolio volatility (standard deviation)
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Store volatility, return, and Sharpe ratio (assuming risk-free rate = 0)
    results[0, i] = portfolio_std
    results[1, i] = portfolio_return
    results[2, i] = portfolio_return / portfolio_std if portfolio_std != 0 else 0

# Identify the portfolio with the maximum Sharpe ratio and the portfolio with minimum volatility
max_sharpe_idx = np.argmax(results[2])
min_vol_idx = np.argmin(results[0])

sdp, rp, sr = results[0, max_sharpe_idx], results[1, max_sharpe_idx], results[2, max_sharpe_idx]
sdp_min, rp_min, sr_min = results[0, min_vol_idx], results[1, min_vol_idx], results[2, min_vol_idx]

# Plot the simulated portfolios and highlight the optimal ones
plt.figure(figsize=(10, 7))
plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='viridis', marker='o', s=10, alpha=0.3)
plt.colorbar(label='Ratio Sharpe')
plt.scatter(sdp, rp, marker='h', color='red', s=200, label='Max Sharpe')
plt.scatter(sdp_min, rp_min, marker='^', color='blue', s=200, label='Min Volatility')
plt.title("Efficient Frontier")
plt.xlabel("Volatility")
plt.ylabel("Return")
plt.legend()
plt.show()