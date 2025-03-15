import matplotlib.pyplot as plt

def plot_stock_data(days, prices, regression_line, next_day, predicted_price):
    plt.figure(figsize=(10, 6))
    plt.scatter(days, prices, color="blue", label="Actual Prices")
    plt.plot(days, regression_line, color="red", label="Regression Line")
    plt.scatter([next_day], [predicted_price], color="green", marker="x", s=100, label="Predicted Price")
    plt.xlabel("Day")
    plt.ylabel("Closing Price")
    plt.title("Stock Price Prediction")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    days = list(range(1, 11))
    prices = [150, 152, 153, 155, 157, 156, 158, 160, 162, 161]
    regression_line = prices
    plot_stock_data(days, prices, regression_line, 11, 163)
