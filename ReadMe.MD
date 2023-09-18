# TradeX: Automated Trading Platform 📈



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Software](#running-the-software)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

TradeX is an automated trading platform designed to backtest and execute trading strategies. Built with Python, it offers a range of features from data retrieval to strategy implementation and visualization.

## Features

- **Data Retrieval**: Fetch historical price data from various sources.
- **Trading Strategies**: Implement popular trading strategies like Moving Averages and Bollinger Bands.
- **Backtesting**: Test your strategies on historical data.
- **Visualization**: Generate insightful graphs and tables.
- **User Interface**: Command-line and planned web interface for user interaction.

## Technologies Used

- Python
- Pandas
- Plotly
- Yahoo Finance API

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/Belalaskaik/TradeX.git
    ```
2. Navigate to the project directory
    ```bash
    cd TradeX
    ```
3. Install required packages
    ```bash
    pip install -r requirements.txt
    ```

### Running the Software

#### For Backtesting:
1. Navigate to the `view` folder.
2. Run `backtest.py`:
    ```bash
    python backtest.py
    ```
3. Follow the on-screen prompts to enter your trading strategy and time period.

#### For Data Visualization:
1. Navigate to the `view` folder.
2. Run `display.py`:
    ```bash
    python display.py
    ```
3. The script will automatically generate HTML files for plots and tables.

