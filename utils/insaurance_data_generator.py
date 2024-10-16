import pandas as pd
import numpy as np

def generate_insurance_data(num_samples=100, seed=42):
    np.random.seed(seed)


    ages = np.random.randint(18, 66, size=num_samples)

    probabilities = np.clip(0.1 + (ages - 18) * 0.02, 0, 1)  # Probability of buying insurance
    insurance_purchased = np.random.binomial(1, probabilities)


    insurance_data = pd.DataFrame({
        'age': ages,
        'insurance_purchased': insurance_purchased
    })

    return insurance_data


insurance_data = generate_insurance_data()


print(insurance_data.head(10))

insurance_data.to_csv('../data/insurance_data.csv', index=False)
