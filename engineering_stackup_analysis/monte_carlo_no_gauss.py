# pylint: disable=all

import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_analysis(tolerances, num_simulations=100000, distribution="normal"):
    """Monte Carlo simulation with different tolerance distributions."""
    num_components = len(tolerances)
    simulated_results = np.zeros(num_simulations)

    for i in range(num_components):
        tol = tolerances[i]

        if distribution == "normal":
            samples = np.random.normal(0, tol, num_simulations)  # Średnia = 0, odchylenie standardowe = tol
        elif distribution == "uniform":
            samples = np.random.uniform(-tol, tol, num_simulations)  # Rozkład jednostajny
        elif distribution == "triangular":
            samples = np.random.triangular(-tol, 0, tol, num_simulations)  # Środek 0, min -tol, max tol
        else:
            raise ValueError("Nieobsługiwany typ rozkładu!")

        simulated_results += samples  # Sumujemy tolerancje dla każdej iteracji

    return simulated_results

# Lista tolerancji dla poszczególnych komponentów (w mm)
component_tolerances = [0.1, 0.05, 0.02, 0.08, 0.04]
num_simulations = 100000

# Monte Carlo dla różnych rozkładów
results_normal = monte_carlo_analysis(component_tolerances, num_simulations, distribution="normal")
results_uniform = monte_carlo_analysis(component_tolerances, num_simulations, distribution="uniform")
results_triangular = monte_carlo_analysis(component_tolerances, num_simulations, distribution="triangular")

# Wyznaczanie przedziałów ufności (3σ)
sigma_normal = np.std(results_normal)
sigma_uniform = np.std(results_uniform)
sigma_triangular = np.std(results_triangular)

# Tworzenie histogramów
plt.figure(figsize=(12, 6))
plt.hist(results_normal, bins=50, density=True, alpha=0.6, color='b', label="Normalny")
plt.hist(results_uniform, bins=50, density=True, alpha=0.6, color='g', label="Jednostajny")
plt.hist(results_triangular, bins=50, density=True, alpha=0.6, color='r', label="Trójkątny")

plt.axvline(-3 * sigma_normal, color='b', linestyle='dashed', linewidth=2, label=f"3σ Normalny: ±{3*sigma_normal:.3f} mm")
plt.axvline(3 * sigma_normal, color='b', linestyle='dashed', linewidth=2)
plt.axvline(-3 * sigma_uniform, color='g', linestyle='dashed', linewidth=2, label=f"3σ Jednostajny: ±{3*sigma_uniform:.3f} mm")
plt.axvline(3 * sigma_uniform, color='g', linestyle='dashed', linewidth=2)
plt.axvline(-3 * sigma_triangular, color='r', linestyle='dashed', linewidth=2, label=f"3σ Trójkątny: ±{3*sigma_triangular:.3f} mm")
plt.axvline(3 * sigma_triangular, color='r', linestyle='dashed', linewidth=2)

plt.xlabel("Suma tolerancji (mm)")
plt.ylabel("Gęstość prawdopodobieństwa")
plt.title("Monte Carlo: Analiza stack-up dla różnych rozkładów")
plt.legend()
plt.grid()
plt.show()

# Wyniki
print(f"Monte Carlo (Normalny) 3σ: ±{3*sigma_normal:.3f} mm")
print(f"Monte Carlo (Jednostajny) 3σ: ±{3*sigma_uniform:.3f} mm")
print(f"Monte Carlo (Trójkątny) 3σ: ±{3*sigma_triangular:.3f} mm")