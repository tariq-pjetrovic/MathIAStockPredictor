def calculate_sma(prices, window):
    """
    Calculate the Simple Moving Average (SMA).
    """
    moving_averages = []
    for i in range(len(prices) - window + 1):
        window_prices = prices[i:i+window]
        moving_averages.append(sum(window_prices) / window)
    return moving_averages

def calculate_daily_percentage_change(prices):
    """
    Calculate daily percentage changes.
    """
    changes = []
    for i in range(1, len(prices)):
        change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
        changes.append(change)
    return changes

import math

def calculate_volatility(changes):
    """
    Calculate volatility (standard deviation of percentage changes).
    """
    if not changes:
        return 0
    mean = sum(changes) / len(changes)
    variance = sum((x - mean) ** 2 for x in changes) / len(changes)
    return math.sqrt(variance)
