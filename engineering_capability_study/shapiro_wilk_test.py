# pylint: disable=all
"""
You can check data normality using the Shapiro-Wilk test in Python with the scipy.stats.shapiro() function.
The test determines whether a dataset follows a normal distribution.

How to Interpret the Results
H₀ (Null Hypothesis): Data is normally distributed
H₁ (Alternative Hypothesis): Data is not normally distributed
If p-value > 0.05 → Fail to reject H₀ → Data is likely normal ✅
If p-value ≤ 0.05 → Reject H₀ → Data is not normal ❌
When to Apply a Johnson Transformation?
If the Shapiro-Wilk p-value ≤ 0.05, apply Johnson transformation or another normalization technique.
If p-value > 0.05, the data is already normal, and you can directly calculate Cp, Cpk, Pp, Ppk.

"""


import numpy as np
import scipy.stats as stats

# Sample Data: Replace with your actual measurements
data = np.array([50.05, 50.02, 49.98, 50.03, 50.00, 49.97, 50.06, 50.01, 50.02, 49.99])

# Perform Shapiro-Wilk test
stat, p_value = stats.shapiro(data)

# Display results
print(f"Shapiro-Wilk Test Statistic: {stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret the result
alpha = 0.05  # Significance level (5%)
if p_value > alpha:
    print("Data appears to be normally distributed (Fail to reject H0)")
else:
    print("Data is NOT normally distributed (Reject H0)")
