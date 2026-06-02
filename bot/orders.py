from .client import BinanceFuturesClient
from .logging_config import setup_logging

logger = setup_logging()


def place_order(client: BinanceFuturesClient, symbol: str, side: str, type_: str, quantity: float, price: float = None):
    """Place an order and return the API response dict."""
    logger.info("Placing order: %s %s %s qty=%s price=%s", symbol, side, type_, quantity, price)
    resp = client.post_order(symbol=symbol, side=side, type_=type_, quantity=quantity, price=price)
    logger.info("Order response: %s", resp)
    return resp
