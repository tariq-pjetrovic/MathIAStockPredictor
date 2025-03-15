import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from model import StockPredictor

X = np.array([[i] for i in range(1, 146)])
y = np.array([ ... ])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

predictor = StockPredictor()
predictor.train(X_train, y_train)

predictions = predictor.predict(X_test)

mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R² Score:", r2)
