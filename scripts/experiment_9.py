import pandas as pd
import matplotlib.pyplot as plt

path = "../data/burden-of-disease-by-cause.csv"
data = pd.read_csv(path)

india_data = data[data['Entity'] == 'India']

total_burden_india = india_data.sum(numeric_only=True)

total_burden_india = total_burden_india[~total_burden_india.index.isin(['Year'])]

burden_percentages = (total_burden_india / total_burden_india.sum()) * 100

burden_percentages = burden_percentages.sort_values()

plt.figure(figsize=(12, 8))
burden_percentages.plot(kind='barh', color='skyblue', edgecolor='black')

plt.title('Burden of Disease in India (Percentage)', fontsize=16)
plt.xlabel('Percentage of Total DALYs (%)', fontsize=14)
plt.ylabel('Disease Categories', fontsize=14)
plt.tight_layout()
plt.show()