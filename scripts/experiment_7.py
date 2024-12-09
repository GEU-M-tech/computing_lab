import statistics
from typing import List, Union
import random

class DataImputer:
    def __init__(self, data: List[Union[float, int, None]]):
        self.data = data
        self.clean_data = [x for x in data if x is not None]
    
    def mean_imputation(self) -> List[float]:
        """Replace missing values with the mean of the dataset."""
        if not self.clean_data:
            return self.data
        
        mean_value = statistics.mean(self.clean_data)
        return [mean_value if x is None else x for x in self.data]
    
    def median_imputation(self) -> List[float]:
        """Replace missing values with the median of the dataset."""
        if not self.clean_data:
            return self.data
        
        median_value = statistics.median(self.clean_data)
        return [median_value if x is None else x for x in self.data]

    
dataset = [10, None, 15, 20, None, 25, 30, None, 35]
    
imputer = DataImputer(dataset)
    
mean_imputed = imputer.mean_imputation()
median_imputed = imputer.median_imputation()

print("Original dataset:", dataset)
print("Mean imputation:", mean_imputed)
print("Median imputation:", median_imputed)