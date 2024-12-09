import pandas as pd
import matplotlib.pyplot as plt

file_path = '../data/burden-of-disease-by-cause.csv'
data = pd.read_csv(file_path)

india_data = data[data['Entity'] == 'India']

columns_to_plot = [col for col in india_data.columns if col not in ['Entity', 'Code', 'Year']]
years = india_data['Year']
disease_data = india_data[columns_to_plot].set_index(years)

normalized_data = (disease_data / disease_data.iloc[0]) * 100

plt.figure(figsize=(14, 8))
for disease in normalized_data.columns:
    plt.plot(normalized_data.index, normalized_data[disease], label=disease, alpha=0.7)

plt.title('Relative Increase in Disease Burden in India', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Burden of Disease (% of First Year)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
