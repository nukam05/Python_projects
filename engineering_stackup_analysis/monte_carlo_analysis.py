# pylint: disable=all

import numpy as np
import matplotlib.pyplot as plt

def worst_case_analysis(tolerances):
    """Calculates worst-case tolerance accumulation."""
    return sum(abs(tol) for tol in tolerances)

def rss_analysis(tolerances):
    """Calculates statistical (RSS) tolerance accumulation."""
    return np.sqrt(sum(tol**2 for tol in tolerances))

def monte_carlo_analysis(tolerances, num_simulations=100000):
    """Performs Monte Carlo simulation for tolerance stack-up."""
    simulated_results = np.sum(np.random.normal(0, tolerances, (num_simulations, len(tolerances))), axis=1)
    return simulated_results

# Example: List of tolerances for components (in mm)
component_tolerances = [0.1, 0.05, 0.02, 0.08, 0.04]

# Compute worst-case and RSS stack-up results
worst_case_result = worst_case_analysis(component_tolerances)
rss_result = rss_analysis(component_tolerances)

# Monte Carlo simulation
num_simulations = 100000
monte_carlo_results = monte_carlo_analysis(component_tolerances, num_simulations)

# Compute statistical results from simulation
mean_mc = np.mean(monte_carlo_results)
std_mc = np.std(monte_carlo_results)
tolerance_99_percent = 3 * std_mc  # 99.7% confidence (3-sigma)

# Plot Monte Carlo results
plt.hist(monte_carlo_results, bins=50, density=True, alpha=0.6, color='b')
plt.axvline(-tolerance_99_percent, color='r', linestyle='dashed', linewidth=2, label=f"-3σ: {tolerance_99_percent:.3f} mm")
plt.axvline(tolerance_99_percent, color='r', linestyle='dashed', linewidth=2, label=f"+3σ: {tolerance_99_percent:.3f} mm")
plt.xlabel("Total Tolerance (mm)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation - Tolerance Stack-Up")
plt.legend()
plt.grid()
plt.show()

# Print results
print(f"Worst-case stack-up: ±{worst_case_result:.3f} mm")
print(f"RSS stack-up: ±{rss_result:.3f} mm")
print(f"Monte Carlo 3σ range: ±{tolerance_99_percent:.3f} mm")