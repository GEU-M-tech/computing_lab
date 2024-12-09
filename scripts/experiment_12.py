import pandas as pd

file_path = '../data/burden-of-disease-by-cause.csv'
data = pd.read_csv(file_path)

cleaned_data = data.drop_duplicates()

cleaned_data.to_csv('../data/cleaned_dataset.csv', index=False)

print(f"Original dataset had {len(data)} rows.")
print(f"Cleaned dataset has {len(cleaned_data)} rows.")
