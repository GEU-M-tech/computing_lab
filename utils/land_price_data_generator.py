import pandas as pd
import numpy as np

def generate_land_data(num_samples=100, seed=42):
    np.random.seed(seed)
    land_areas = np.random.randint(100, 1001, size=num_samples)

    prices = np.round(land_areas * np.random.normal(loc=200, scale=50, size=num_samples), 2)

    land_data = pd.DataFrame({
        'area': land_areas,
        'price': prices
    })

    return land_data

land_data = generate_land_data()

print(land_data.head(10))
land_data.to_csv('../data/home_price_data.csv', index=False)