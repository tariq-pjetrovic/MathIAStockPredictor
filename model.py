import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class StockPredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse

if __name__ == '__main__':
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([150, 152, 153, 155, 157])
    predictor = StockPredictor()
    predictor.train(X, y)
    print("Predicted value for day 6:", predictor.predict(np.array([[6]]))[0])
    print("MSE on training data:", predictor.evaluate(X, y))
