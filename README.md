# Binance Futures Testnet Trading Bot

A Python-based trading bot that interacts with the Binance USDT-M Futures Testnet API. The application supports MARKET and LIMIT order placement through a command-line interface while following clean code architecture, input validation, logging, and error handling practices.

## Features

* Place MARKET orders on Binance Futures Testnet
* Place LIMIT orders on Binance Futures Testnet
* Support BUY and SELL order sides
* Command-line interface using argparse
* Input validation for all user inputs
* Secure API key management using environment variables
* Detailed logging of requests, responses, and errors
* Exception handling for invalid input, API errors, and network failures
* Modular and reusable project structure

## Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading_bot.log
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.9+
* Binance Futures Testnet Account
* Binance Testnet API Key and Secret

## Installation

### Clone Repository

```bash
git clone https://github.com/Shubhampanwar20/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
```

## Usage

### MARKET BUY Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

### MARKET SELL Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side SELL \
--type MARKET \
--quantity 0.001
```

### LIMIT BUY Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--quantity 0.001 \
--price 100000
```

### LIMIT SELL Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 150000
```

## Sample Output

```text
📌 Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

✅ Order Response
orderId: 13791491757
status: NEW
origQty: 0.0010
executedQty: 0.0000
avgPrice: 0.00

Done.
```

## Logging

All API requests, responses, and errors are logged automatically.

Example log:

```text
2026-06-02 14:35:36 | INFO | trading_bot | Placing order
2026-06-02 14:35:37 | INFO | trading_bot | Response 200
```

Log file location:

```text
logs/trading_bot.log
```

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing LIMIT price
* Invalid quantity values
* API authentication errors
* Network failures
* Binance API errors

## Assumptions

* Binance Futures Testnet account is active.
* API credentials are valid.
* Internet connectivity is available.
* Only MARKET and LIMIT orders are required.

## Technologies Used

* Python 3.x
* Requests
* Python Dotenv
* Binance Futures REST API

## Author

Shubham Panwar

GitHub:
https://github.com/Shubhampanwar20
