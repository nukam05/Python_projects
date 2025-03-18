# pylint: disable=all

"""Simple measurement of cpk,cp,ppk,pp based on sample data and specification limits."""

import numpy as np

# Sample data: Replace with your actual measurements
data = np.array([50.05, 50.02, 49.98, 50.03, 50.00, 
50.05, 50.07, 49.98, 50.03, 50.00, 
50.05, 50.02, 49.98, 50.03, 50.00, 
50.05, 50.02, 49.98, 50.08, 50.00, 
50.05, 50.02, 49.98, 50.00, 50.00, 
49.97, 50.06, 50.01, 50.02, 49.99])

# Specification Limits
USL = 50.10  # Upper Spec Limit
LSL = 49.90  # Lower Spec Limit

# Compute Statistics
mean = np.mean(data)
std_dev_sample = np.std(data, ddof=1)  # Sample Standard Deviation
std_dev_population = np.std(data, ddof=0)  # Population Standard Deviation

# Cp and Pp Calculation
Cp = (USL - LSL) / (6 * std_dev_population)
Pp = (USL - LSL) / (6 * std_dev_sample)

# Cpk and Ppk Calculation
Cpk = min((USL - mean) / (3 * std_dev_population), (mean - LSL) / (3 * std_dev_population))
Ppk = min((USL - mean) / (3 * std_dev_sample), (mean - LSL) / (3 * std_dev_sample))

# Display Results
print(f"Mean: {mean:.4f}")
print(f"Sample Std Dev (Pp, Ppk): {std_dev_sample:.4f}")
print(f"Population Std Dev (Cp, Cpk): {std_dev_population:.4f}")
print(f"Cp: {Cp:.4f}, Cpk: {Cpk:.4f}")
print(f"Pp: {Pp:.4f}, Ppk: {Ppk:.4f}")
