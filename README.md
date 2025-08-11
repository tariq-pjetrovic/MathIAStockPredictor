# AI Stock Market Predictor

A Python project that predicts short-term stock price trends using historical data and linear regression.

## Features
- Fetches daily stock data from the Alpha Vantage API
- Calculates basic technical indicators (SMA, volatility, daily % change)
- Trains a linear regression model on historical prices
- Predicts the next day's closing price
- Visualizes historical prices, regression line, and predicted value

## Tech Stack
- **Languages:** Python
- **Libraries:** requests, csv, io, math, numpy, matplotlib, scikit-learn
- **API:** Alpha Vantage

## How It Works
1. Download daily stock data via API  
2. Extract and process closing prices  
3. Split into training/testing sets  
4. Train a regression model  
5. Evaluate performance (MSE, R²)  
6. Plot the prediction vs. actual prices

## Note
This tool is for **educational purposes only** and is **not financial advice**.
