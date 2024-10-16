import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
highs = np.array([36, 33, 35, 30, 33, 34, 29, 33, 36, 33, 35, 32, 32, 33, 34, 35, 35, 32, 35, 36, 36, 36, 37, 37, 36, 30, 34, 33, 34, 34])
lows = np.array([27, 27, 25, 24, 25, 26, 25, 26, 27, 27, 26, 26, 24, 23, 24, 24, 26, 25, 25, 23, 26, 26, 26, 28, 28, 26, 25, 24, 25, 24])


plt.figure(figsize=(10, 6))
plt.plot(days, highs, 'r-', marker='o', label='High Temp (°C)')
plt.plot(days, lows, 'b-', marker='x', label='Low Temp (°C)')


plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°C)')
plt.title('High and Low Temperatures in Dehradun (Sept 2024)')
plt.xticks(days)
plt.grid(True)


plt.legend()

plt.tight_layout()
plt.show()