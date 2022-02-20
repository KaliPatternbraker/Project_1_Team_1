# This is the function which calculates the z-score and is called in the main

# The formula is is as follows:
    # Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5

# Where;
    # X1 = Working Capital / Total Assets. Measures liquid assets in relation to the size of the company.
    # X2 = Retained Earnings / Total Assets. Measures profitability that reflects the company's age and earning power.
    # X3 = Earnings Before Interest and Taxes / Total Assets. Measures operating efficiency apart from tax and leveraging factors. It recognizes operating earnings as being important to long-term viability.
    # X4 = Market Value of Equity / Book Value of Total Liabilities. Adds market dimension that can show up security price fluctuation as a possible red flag.
    # X5 = Sales / Total Assets. Standard measure for total asset turnover (varies greatly from industry to industry).

def z_score_calculator(ticker_df):
    current_assets = ticker_df["OCA"] + ticker_df["AR"] + ticker_df["INV"]
    current_liabilities = ticker_df["OCL"] + ticker_df["PREPAID"] + ticker_df["AP"]
    X1 =(current_assets- current_liabilities)/ticker_df["TOTAL ASSETS"]
    X2 = ticker_df["RETAINED EARNINGS"]/ticker_df["TOTAL ASSETS"]
    X3 = ticker_df["EBIT"]/ticker_df["TOTAL ASSETS"]
    X4 = ticker_df["EBIT"]/current_liabilities
    X5 = ticker_df["AR"]/ticker_df["TOTAL ASSETS"]

    z_score = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5
    return z_score