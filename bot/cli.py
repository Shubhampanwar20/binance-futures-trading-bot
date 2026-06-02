"""Simple CLI to place orders on Binance Futures Testnet"""

import os
import argparse
import sys
from dotenv import load_dotenv

# Load API keys
load_dotenv()

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logging

logger = setup_logging()


def main():
    parser = argparse.ArgumentParser(
        description="Place orders on Binance Futures Testnet"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(2)

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ API keys missing in .env")
        sys.exit(2)

    client = BinanceFuturesClient(
        api_key=api_key,
        api_secret=api_secret,
        base_url="https://testnet.binancefuture.com",
    )

    print("\n📌 Order Request Summary")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price: {price}")

    try:
        resp = place_order(client, args.symbol, side, order_type, quantity, price)
    except Exception as e:
        print(f"\n❌ Order failed: {e}")
        sys.exit(1)

    print("\n✅ Order Response")
    for k in ("orderId", "status", "origQty", "executedQty", "avgPrice"):
        if k in resp:
            print(f"{k}: {resp[k]}")

    print("\nDone.")


if __name__ == "__main__":
    main()