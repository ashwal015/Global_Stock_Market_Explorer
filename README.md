
# Global Stock Market Explorer


## Brief Summary
A Python-based data analytics and visualization project that fetches real-time historical stock market data using the Yahoo Finance API and presents key market trends through static and interactive visualizations.


## Overview
This project explores the performance of major global stocks by analyzing their closing price trends and daily return percentages over the past year. 
It provides both saved visual outputs and an interactive Streamlit dashboard for easy exploration.



## Problem Statement
Understanding stock market behavior requires analyzing historical price movements and return patterns.
This project aims to simplify stock market exploration by automatically collecting, processing, and visualizing stock data in a clear and interactive way.



## Dataset
- **Source:** Yahoo Finance (via `yfinance`)
- **Data Used:** 1 year of historical daily stock data  
- **API Call Used**

## Key Insights

- Stocks exhibit distinct price growth patterns over the one-year period, highlighting differences in long-term performance across companies.

- Daily return analysis reveals varying levels of volatility, with some stocks experiencing sharper short-term fluctuations than others.

- Higher volatility stocks tend to show larger day-to-day price movements, indicating increased risk compared to more stable assets.

- Combining closing price trends with daily return analysis provides a clearer understanding of both performance and risk characteristics.

More detailed insights can be inferred from generated charts.


## Tools and Technology

- IDE: PyCharm
- Languages: Python 3.x
- Libraries: 
          - yfinance – Fetches real-time and historical stock market data from Yahoo Finance
	  - pandas – Data cleaning, transformation, and analysis
	  - matplotlib – Basic data visualization and plotting
	  - plotly.express – Interactive and dynamic charts
	  - streamlit – Web-based dashboard for displaying stock market insights

## Method

1.	Fetch Stock Data
			- Retrieved 1-year historical data for selected stocks using Yahoo Finance API.
```python
stock = yf.Ticker(ticker)
hist = stock.history(period="1y")

```

2.	Clean and Process Data
			- Handled missing values
			- Calculated daily returns, moving averages, and volatility
3.	Save Processed Data
			- Stored cleaned stock data as CSV files in the data/ directory
4.	Generate Visualizations
			- Created and saved -> Closing Price Trends and Daily Return (%) plots
			- Saved outputs in the outputs/ folder
5.	Create Streamlit Dashboard
			- Built an interactive dashboard to explore stock prices and daily returns dynamically


## Dashboard / Model / Output:
- Interactive Streamlit dashboard for stock selection and trend exploration
- Saved static charts for offline analysis and documentation


## How to Run Project and Project Structure
Project Structure
```
Global_Stock_Market_Explorer/
│
├── data/              # Saved stock CSV files
├── outputs/           # Generated visualization images
├── app.py             # Main Python & Streamlit application
├── requirements.txt   # Project dependencies
└── README.md

```
## Steps to Run

1.Clone the repository 

2.Install dependencies 

```bash
 pip install -r requirements.txt 
```
3.Run the Streamlit application:
```bash 
-m streamlit run app.py
 ```
4.Open the browser link displayed in the terminal


## Results and Conclusion

- Successfully visualized and compared stock performance over a 1-year period.
- Combined static and interactive visualizations for better insights.
- Demonstrated end-to-end data analytics workflow using real-world APIs


## Future Work

- Add more financial metrics such as moving averages comparison and volatility ranking.
- Extend the dashboard to include more stocks and time ranges.
