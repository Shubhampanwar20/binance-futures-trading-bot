"""Binance Futures client wrapper (REST + HMAC signature)

Uses the testnet base URL by default. Expects API key/secret passed in.
"""
import time
import hmac
import hashlib
import logging
from urllib.parse import urlencode

import requests

from .logging_config import setup_logging

logger = setup_logging()


class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, base_url: str = "https://testnet.binancefuture.com"):
        self.api_key = api_key
        self.api_secret = api_secret.encode()
        self.base_url = base_url.rstrip("/")

    def _sign(self, params: dict) -> str:
        query = urlencode(params, doseq=True)
        signature = hmac.new(self.api_secret, query.encode(), hashlib.sha256).hexdigest()
        return signature

    def _headers(self):
        return {"X-MBX-APIKEY": self.api_key}

    def post_order(self, symbol: str, side: str, type_: str, quantity: float, price: float = None, time_in_force: str = "GTC"):
        path = "/fapi/v1/order"
        url = self.base_url + path

        params = {
            "symbol": symbol,
            "side": side,
            "type": type_,
            "quantity": str(quantity),
            "timestamp": int(time.time() * 1000),
        }
        if type_ == "LIMIT":
            params.update({"price": str(price), "timeInForce": time_in_force})

        params["signature"] = self._sign(params)

        headers = self._headers()

        logger.info("POST %s %s", url, params)
        try:
            resp = requests.post(url, params=params, headers=headers, timeout=10)
            logger.info("Response %s: %s", resp.status_code, resp.text)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            logger.error("Order request failed: %s", e)
            raise
