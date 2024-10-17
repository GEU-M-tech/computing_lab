import pandas as pd
import numpy as np

def generate_houses_data(num_houses=50):
    np.random.seed(42)
    areas = np.random.randint(800, 4000, num_houses)
    ages = np.random.randint(1, 50, num_houses)
    prices = (areas * np.random.randint(1000, 5000, num_houses)) / (ages * 0.1 + 1)

    houses_data = pd.DataFrame({
        'area': areas,
        'age': ages,
        'price': prices.astype(int)
    })
    
    return houses_data

all_iterations_data = pd.DataFrame()

for i in range(100):
    iteration_data = generate_houses_data()
    iteration_data['Iteration'] = i + 1
    all_iterations_data = pd.concat([all_iterations_data, iteration_data], ignore_index=True)

all_iterations_data.to_csv('../data/houses_data.csv', index=False)