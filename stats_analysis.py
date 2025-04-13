import csv
import statistics
import matplotlib.pyplot as plt
import os

def read_closing_prices(file_path):
    """
    Read a CSV file, extract and return the closing prices as a list of floats.
    Assumes the CSV file has a header row that includes a 'close' column.
    """
    closing_prices = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        # Identify the 'close' column index
        close_index = None
        for i, header in enumerate(headers):
            if header.strip().lower() == "close":
                close_index = i
                break
        
        if close_index is None:
            print("Error: 'close' column not found in the CSV data.")
            return closing_prices
        
        # Process each row
        for row in reader:
            # Skip rows that are empty or don't have enough columns
            if len(row) <= close_index:
                continue
            try:
                closing_prices.append(float(row[close_index]))
            except ValueError:
                # Skip rows where conversion to float fails
                continue
                
    closing_prices.reverse()
    return closing_prices

def compute_statistics(prices):
    """
    Compute the mean, median, and range of a list of prices.
    """
    mean_val = statistics.mean(prices)
    median_val = statistics.median(prices)
    range_val = max(prices) - min(prices)
    mode_val = statistics.mode(prices)
    variance_val = statistics.variance(prices)
    return mean_val, median_val, range_val, mode_val, variance_val

def plot_boxplot(prices):
    """
    Display a box plot of the given prices.
    """
    plt.boxplot(prices, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title("Box Plot of Stock Closing Prices")
    plt.ylabel("Price")
    plt.show()

def main():
    file_path = "data/daily_AAPL.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist. Please check the file path.")
        return
    
    prices = read_closing_prices(file_path)
    if not prices:
        print("No valid closing prices were found in the file.")
        return
    
    # Compute statistics: mean, median, and range.
    mean_val, median_val, range_val, mode_val, variance_val = compute_statistics(prices)
    
    # Display the computed values, rounded to 3 significant figures.
    print("Mean:", round(mean_val, 3))
    print("Median:", round(median_val, 3))
    print("Range:", round(range_val, 3))
    print("Mode:", round(mode_val, 3))
    print("Variance:", round(variance_val, 3))
    
    # Visualize the distribution using a box plot.
    plot_boxplot(prices)

if __name__ == '__main__':
    main()
