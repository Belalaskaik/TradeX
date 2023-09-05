import sys
import os

# Get the current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))

# # Get the path to module.py
# module_directory = os.path.join(current_directory, 'TradingStrat.py')
# TradingStrat = __import__(module_directory, fromlist=[''])
from project.Model import DataRetrieverAdapter
from project.Account import Account
from project.TradingStrat import TradingStrategy
# import jsonLoader
import pandas as pd


def get_user_input():
    strategy_choice = input("Enter the strategy to use (MA/BB/Both): ").lower()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    return strategy_choice, start_date, end_date



def Ibacktest():
    # Load price data

    price_data_object = DataRetrieverAdapter()
    price_data = price_data_object.load_price_data()

    # Get user input for strategy and time period
    # strategy_choice, start_date, end_date = get_user_input()

    # Create instance of TradingStrategy class based on user's strategy choice
    
    strategy_choice = 'ma'
    start_date = '2023-01-01'
    end_date = '2023-08-04'
    strategy = TradingStrategy(price_data['FNGD'], price_data['FNGU'], strategy_choice=strategy_choice, window_size=20)

        
    # Create instance of Account class
    account = Account()

    final_balance, returnsP, returnsD= account.backtest_strategy(strategy, price_data, start_date, end_date)    
    print(f"\nFinal Account Balance: ${final_balance:.2f}")
    print(f"Returns Gained: ${returnsD:.2f}")
    print(f"Returns Percentage: {returnsP:.2%}")

Ibacktest()