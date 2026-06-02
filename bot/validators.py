from typing import Optional


def validate_side(side: str) -> str:
    s = side.upper()
    if s not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")
    return s


def validate_order_type(type_: str) -> str:
    t = type_.upper()
    if t not in ("MARKET", "LIMIT"):
        raise ValueError("order type must be MARKET or LIMIT")
    return t


def validate_quantity(q: str) -> float:
    try:
        val = float(q)
    except Exception:
        raise ValueError("quantity must be a number")
    if val <= 0:
        raise ValueError("quantity must be > 0")
    return val


def validate_price(p: Optional[str], order_type: str) -> Optional[float]:
    if order_type == "LIMIT":
        if p is None:
            raise ValueError("price is required for LIMIT orders")
        try:
            val = float(p)
        except Exception:
            raise ValueError("price must be a number")
        if val <= 0:
            raise ValueError("price must be > 0")
        return val
    return None
