
import pandas as pd
import matplotlib.pyplot as plt

file_path = '../data/burden-of-disease-by-cause.csv'
data = pd.read_csv(file_path)

# Filter data for India
india_data = data[data['Entity'] == 'India']

# Identify the correct column for cardiovascular diseases
heart_disease_column = 'DALYs (Disability-Adjusted Life Years) - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)'

# Extract the burden of heart diseases over the years
heart_disease_burden = india_data[['Year', heart_disease_column]].rename(columns={heart_disease_column: 'Heart Disease Burden'})

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(heart_disease_burden['Year'], heart_disease_burden['Heart Disease Burden'], marker='o', color='red')

plt.title('Burden of Cardiovascular Diseases in India Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Disability-Adjusted Life Years (DALYs)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()