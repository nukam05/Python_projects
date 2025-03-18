# pylint: disable=all
"""Explanation:
Data Input: You need to replace the data array with your actual measurements (X, Y) coordinates.
Fourier Transform (FFT). 
The np.fft.fft() function is used to compute the FFT of the
X and Y coordinate data.
Magnitude Calculation: The np.abs() function calculates the magnitude of the Fourier components.
Plotting: The script plots the first 100 harmonics for both the X and Y components using matplotlib.
Graph Interpretation:
X Harmonics.
The first plot shows the frequency components of the X-axis data.
Y Harmonics.
The second plot shows the frequency components of the Y-axis data.
The peak values in the graph correspond to the dominant frequency components (harmonics) in the circular data.
Conclusion.
This approach will allow you to extract the harmonics from the circular measurement data using Fourier Transform. 
The harmonic peaks represent the frequency components that make up the circular shape. If you have more complex data or noise, 
you might need additional steps like windowing or filtering."""



import numpy as np
import matplotlib.pyplot as plt

# Simulated Circular Data (Replace with your actual data)
# Assuming the data is in a list of tuples: (X, Y) coordinates
data = np.array([
    [25.000, 0.000], [24.500, 5.000], [23.000, 9.000], [20.000, 12.000], [16.000, 13.500],
    [12.000, 12.000], [9.000, 9.000], [7.000, 5.000], [5.000, 0.000], [5.500, -5.000],
    [7.000, -9.000], [10.000, -10.500], [14.000, -10.000], [17.000, -7.000], [19.000, -3.500],
    [20.000, 0.000]  # Closing the circle
])

# X and Y coordinates of the raw data
x_data = data[:, 0]
y_data = data[:, 1]

# Fourier Transform of X and Y components
fft_x = np.fft.fft(x_data)
fft_y = np.fft.fft(y_data)

# Frequency axis (harmonics)
frequencies = np.fft.fftfreq(len(x_data), 1)  # Use 1 as sample spacing for simplicity

# Magnitude of FFT components (first 100 harmonics)
harmonics_x = np.abs(fft_x)[:100]
harmonics_y = np.abs(fft_y)[:100]

# Plotting the harmonics for both X and Y components
plt.figure(figsize=(12, 6))

# Plot the magnitude of the first 100 harmonics of X and Y
plt.subplot(2, 1, 1)
plt.plot(frequencies[:100], harmonics_x, label='X Harmonics')
plt.title("Fourier Transform - Harmonics of X Coordinates")
plt.xlabel("Harmonic")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frequencies[:100], harmonics_y, label='Y Harmonics', color='orange')
plt.title("Fourier Transform - Harmonics of Y Coordinates")
plt.xlabel("Harmonic")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()
