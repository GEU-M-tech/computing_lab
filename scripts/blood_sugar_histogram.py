import pandas as pd
import matplotlib.pyplot as plt

file_path = '../data/blood_sugar_data.csv'
data = pd.read_csv(file_path)

bld_bins = [50, 70, 90, 110, 130, 150]
bld_labels = ['50-69', '70-89', '90-109', '110-129', '130-149']

data['Blood Sugar Range'] = pd.cut(data['bld'], bins=bld_bins, labels=bld_labels)

males = data[data['gender'] == 'Male']
females = data[data['gender'] == 'Female']

male_counts = males['Blood Sugar Range'].value_counts(sort=False)
female_counts = females['Blood Sugar Range'].value_counts(sort=False)

plt.figure(figsize=(10, 6))

bar_width = 0.4
positions = range(len(bld_labels))

plt.bar([p - bar_width/2 for p in positions], male_counts, width=bar_width, alpha=0.7, label='Males', color='blue', edgecolor='black')
plt.bar([p + bar_width/2 for p in positions], female_counts, width=bar_width, alpha=0.7, label='Females', color='red', edgecolor='black')

plt.xlabel('Blood Sugar Level (mg/dL)')
plt.ylabel('Number of People')
plt.title('Distribution of Blood Sugar Levels by Gender')
plt.xticks(range(len(bld_labels)), bld_labels)


plt.legend()

plt.tight_layout()
plt.show()