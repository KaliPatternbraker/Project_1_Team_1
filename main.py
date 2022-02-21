from pathlib import Path
import pandas as pd
import questionary
import sys
from utilities.calculator import z_score_calculator

# Asking the user to enter a csvpath in order to load in the chosen stock data 

def load_stock_data(csvpath):
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Error! Cannot find this path: {csvpath}")

    user_df = pd.read_csv(csvpath)
    return user_df

user_path = questionary.text("Enter the file path you would like to conduct this Altman Z-Score analysis on:").ask()

utilities_df = load_stock_data(user_path)

# Cleaning data which is pulled in:

utilities_df["Identifier"] = utilities_df["Identifier"].astype("string")

utilities_df["Identifier"] = utilities_df["Identifier"].str.replace('NYSE:','', regex=False)
utilities_df["Identifier"] = utilities_df["Identifier"].str.replace('NasdaqGS:','', regex=False)

utilities_df.rename(columns={"Identifier":"Ticker"}, inplace=True)

print(utilities_df.tail())
 
# Ask the user to choose among the stock tickers uploaded from the csv file:
 
tickers = ["ED", "DTE", "D", "SRE", "XEL", "ETR", "AEP", "PEG", "CMS", "ES", "WEC"]
ticker = questionary.select("Select the ticker you would like to conduct the altman z-score analysis on:", choices=tickers).ask()

user_ticker = utilities_df.loc[utilities_df["Ticker"]==ticker]
user_ticker.set_index(["Ticker","Year","Quarter"], inplace=True)

# Check to make sure the stock ticker data is pulled:
print(user_ticker.head()) 

# Store the Z-Score calculations for the chosen stock ticker in a variable:

user_z_score = z_score_calculator(user_ticker)
print(f"The Quarterly Altman Z-Score calculations for {ticker} are as follows: \n{user_z_score}")
