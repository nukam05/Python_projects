# pylint: disable=all
"""
Application of Johnson Transformation to Capability Analysis
Adding a Johnson transformation can help normalize non-normal process data 
before calculating capability indices (Cp, Cpk, Pp, Ppk). 
The Johnson transformation finds the best transformation (logarithmic, hyperbolic, or normalizing) to convert a skewed dataset
into a normal distribution.
"""

"""
Steps for Johnson Transformation in Python
Check data normality (optional, using Shapiro-Wilk test).
Apply Johnson transformation using the scipy.stats.johnsonsu method.
Compute Cp, Cpk, Pp, Ppk on transformed data.
"""
import numpy as np
import scipy.stats as stats
from scipy.optimize import curve_fit

# Sample Data: Replace with your real measurements
data = np.array([50.05, 50.02, 49.98, 50.03, 50.00, 49.97, 50.06, 50.01, 50.02, 49.99])

# Specification Limits
USL = 50.10  # Upper Spec Limit
LSL = 49.90  # Lower Spec Limit

# Compute Basic Statistics
mean = np.mean(data)
std_dev_sample = np.std(data, ddof=1)  # Sample Std Dev
std_dev_population = np.std(data, ddof=0)  # Population Std Dev

# Perform Johnson Transformation
shape1, shape2, loc, scale = stats.johnsonsu.fit(data)

# Transform Data to Normal Distribution
transformed_data = stats.johnsonsu(shape1, shape2, loc, scale).rvs(len(data))

# Compute Transformed Statistics
transformed_mean = np.mean(transformed_data)
transformed_std = np.std(transformed_data, ddof=1)

# Cp and Pp Calculation (on transformed data)
Cp = (USL - LSL) / (6 * transformed_std)
Pp = (USL - LSL) / (6 * std_dev_sample)

# Cpk and Ppk Calculation
Cpk = min((USL - transformed_mean) / (3 * transformed_std), (transformed_mean - LSL) / (3 * transformed_std))
Ppk = min((USL - mean) / (3 * std_dev_sample), (mean - LSL) / (3 * std_dev_sample))

# Display Results
print("Before Johnson Transformation:")
print(f"Mean: {mean:.4f}, Std Dev: {std_dev_sample:.4f}")
print(f"Cp: {Cp:.4f}, Cpk: {Cpk:.4f}\n")

print("After Johnson Transformation:")
print(f"Transformed Mean: {transformed_mean:.4f}, Transformed Std Dev: {transformed_std:.4f}")
print(f"Cp: {Cp:.4f}, Cpk: {Cpk:.4f}")
print(f"Pp: {Pp:.4f}, Ppk: {Ppk:.4f}")
