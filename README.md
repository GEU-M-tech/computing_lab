# COMPUTING LAB [M.TECH 1ST SEM]

## Repo Structure:

```bash
├───data
│       blood_sugar_data.csv
│       home_price_data.csv
│       houses_data.csv
│       insurance_data.csv
│       
├───scripts
│       blood_sugar_histogram.py
│       linear_regression_land.py
│       logistic_regression.py
│       multi_regression.py
│       weather_info.py
│
└───utils
        blood_sugar_data_generator.py
        home_price_data_generator.py
        insaurance_data_generator.py
        land_price_data_generator.py
```

## Usage
- Ensure Python & Git are installed locally
```bash
git clone https://github.com/GEU-M-tech/computing_lab
cd computing_lab
```
- Run the following command to install required packages
```bash
pip install -r requirement.txt
```

- You may run the data generators before running scripts

## Data Generators
```bash
cd ./utils
python land_price_data_generator.py
```

## Running Scripts
```bash
cd ../
cd ./scripts
python linear_regression_land.py
```

- Matplot graphs might not be visible on linux enviroment. Use this to resolve
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install PyQt6
```