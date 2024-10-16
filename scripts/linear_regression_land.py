import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

data = pd.read_csv('../data/home_price_data.csv')

land_data = pd.DataFrame(data)

X = land_data[['area']]
y = land_data['price']


model = LinearRegression()
model.fit(X, y)


y_pred = model.predict(X)


mse = root_mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)


print(f'Linear Regression Coefficients:\nSlope: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}')
print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')


plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression: Land Area vs Price')
plt.xlabel('Land Area (m²)')
plt.ylabel('Price ($)')
plt.legend()
plt.grid()
plt.show()