import pandas as pd
import matplotlib.pyplot as plt

path = "../data/burden-of-disease-by-cause.csv"
data = pd.read_csv(path)

india_data = data[data['Entity'] == 'India']

average_burden_india = india_data.mean(numeric_only=True)

average_burden_india = average_burden_india[~average_burden_india.index.isin(['Year'])]

plt.figure(figsize=(12, 8))
average_burden_india.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')

plt.title('Average Burden of Disease in India', fontsize=16)
plt.xlabel('Average DALYs (Number)', fontsize=14)
plt.ylabel('Disease Categories', fontsize=14)
plt.tight_layout()
plt.show()
