import pandas as pd
import numpy as np

def generate_sample_data(num_samples=100, seed=42):
    np.random.seed(seed)

    genders = np.random.choice(['Male', 'Female'], size=num_samples)

    blood_sugar_levels = np.round(np.random.normal(loc=100, scale=15, size=num_samples), 2)
 
    names = [f"Person_{i}" for i in range(1, num_samples + 1)]


    ages = np.random.randint(20, 81, size=num_samples)

    sample_data = pd.DataFrame({
        'Name': names,
        'Gender': genders,
        'Age': ages,
        'Blood Sugar Level (mg/dL)': blood_sugar_levels
    })

    return sample_data


sample_data = generate_sample_data()
print(sample_data.head(10))
sample_data.to_csv('blood_sugar_data.csv', index=False)
