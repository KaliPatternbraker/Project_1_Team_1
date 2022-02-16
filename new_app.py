from pathlib import Path
from telnetlib import X3PAD 
import pandas as pd
import questionary
import sys

# Asking the use to enter a csvpath in order to load in the chosen stock data 

def load_stock_data(csvpath):
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    user_df = pd.read_csv(csvpath)
    return user_df

user_path = questionary.text("Enter the file path you would like to conduct this altman z-score analysis on:").ask()

utilities_df = load_stock_data(user_path)
print(utilities_df.head())

# Cleaning data which is pulled in:

utilities_df["Identifier"] = utilities_df["Identifier"].astype("string")

utilities_df["Identifier"] = utilities_df["Identifier"].str.replace('NYSE:','', regex=False)
utilities_df["Identifier"] = utilities_df["Identifier"].str.replace('NasdaqGS:','', regex=False)

utilities_df.rename(columns={"Identifier":"Ticker"}, inplace=True)

print(utilities_df.tail())
 
# Asking the user to choose amongs the stocks uploaded from the csv file:
 
 
tickers = ["ED", "DTE", "D", "SRE", "XEL", "ETR", "AEP", "PEG", "CMS", "ES", "WEC"]
ticker = questionary.select("Select the ticker you would like to conduct the altman z-score analysis on:", choices=tickers).ask()

user_ticker = utilities_df.loc[utilities_df["Ticker"]==ticker]

print(user_ticker.head())

# csvpath = Path("/Users/michaeladut/Desktop/Projects/Project_1_Team_1/Resources/utilities_data.csv")

# Z-score Calculator:

# Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5

# where 

# X1 = Working Capital / Total Assets. Measures liquid assets in relation to the size of the company.
# X2 = Retained Earnings / Total Assets. Measures profitability that reflects the company's age and earning power.
# X3 = Earnings Before Interest and Taxes / Total Assets. Measures operating efficiency apart from tax and leveraging factors. It recognizes operating earnings as being important to long-term viability.
# X4 = Market Value of Equity / Book Value of Total Liabilities. Adds market dimension that can show up security price fluctuation as a possible red flag.
# X5 = Sales / Total Assets. Standard measure for total asset turnover (varies greatly from industry to industry).

ticker_current_assets = user_ticker["OCA"] + user_ticker["AR"] + user_ticker["INV"]

ticker_current_liabilities = user_ticker["OCL"] + user_ticker["PREPAID"] + user_ticker["AP"]

X1 =(ticker_current_assets - ticker_current_liabilities)/user_ticker["TOTAL ASSETS"]
X2 = user_ticker["RETAINED EARNINGS"]/user_ticker["TOTAL ASSETS"]
X3 = user_ticker["EBIT"]/user_ticker["TOTAL ASSETS"]
X4 = user_ticker["EBIT"]/ticker_current_liabilities
X5 = user_ticker["AR"]/user_ticker["TOTAL ASSETS"]

print(X1)
print(X2)
print(X3)
print(X4)
print(X5)

altman_z_score = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

print(f"the altman z-score data for the stock you have provided is seen below: \n{altman_z_score}")
