import requests
import csv
import io
import os

def fetch_stock_data(symbol, api_key):
    """
    Fetch stock data from Alpha Vantage API as CSV text.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&datatype=csv"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Fetched data for {symbol}.")
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

def save_to_file(data, file_name, folder="data"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"Data saved to {file_path}")


def extract_closing_prices(csv_data):
    closing_prices = []
    csv_file = io.StringIO(csv_data)
    reader = csv.reader(csv_file)
    headers = next(reader)
    
    close_index = None
    for i, header in enumerate(headers):
        if header.strip().lower() == "close":
            close_index = i
            break
    if close_index is None:
        print("No 'close' column found!")
        return closing_prices
    
    for row in reader:
        try:
            closing_prices.append(float(row[close_index]))
        except ValueError:
            continue
    
    closing_prices.reverse()
    return closing_prices