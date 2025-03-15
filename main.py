import numpy as np
from data_automator import fetch_stock_data, save_to_file, extract_closing_prices
from data_processor import calculate_sma, calculate_daily_percentage_change, calculate_volatility
from model import StockPredictor
from visualizer import plot_stock_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    symbol = "AAPL"
    api_key = "M2WILJVN48U2MICM"
    
    csv_data = fetch_stock_data(symbol, api_key)
    if csv_data is None:
        return
    file_name = f"daily_{symbol}.csv"
    save_to_file(csv_data, file_name)
    
    prices = extract_closing_prices(csv_data)
    if not prices:
        print("No closing prices found!")
        return

    days = np.array([[i] for i in range(1, len(prices) + 1)])
    prices = np.array(prices)
    
    X_train, X_test, y_train, y_test = train_test_split(days, prices, test_size=0.2, random_state=42)
    
    predictor = StockPredictor()
    predictor.train(X_train, y_train)

    predictions = predictor.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print("Mean Squared Error:", mse)
    print("R² Score:", r2)
    
    next_day = np.array([[len(prices) + 1]])
    predicted_price = predictor.predict(next_day)[0]
    print(f"Predicted closing price for day {len(prices) + 1}: {predicted_price}")
    
    regression_line = predictor.predict(days)
    
    plot_stock_data(days.flatten(), prices, regression_line, len(prices) + 1, predicted_price)

if __name__ == '__main__':
    main()