import requests

DEX_TOKEN_API = "https://api.dexscreener.com/latest/dex/tokens/"
DEX_PAIR_API = "https://api.dexscreener.com/latest/dex/pairs/solana/"


def get_token_pairs(ca):
    try:
        response = requests.get(DEX_TOKEN_API + ca, timeout=10)
        data = response.json()
        return data.get("pairs", [])
    except Exception as e:
        print("Token pairs hatası:", e)
        return []


def get_best_pair(ca):
    pairs = get_token_pairs(ca)

    if not pairs:
        return None

    # liquidity usd en yüksek olan pair
    best_pair = max(
        pairs,
        key=lambda p: p.get("liquidity", {}).get("usd", 0)
    )

    return best_pair


def get_pair_detail(pair_address):
    try:
        response = requests.get(DEX_PAIR_API + pair_address, timeout=10)
        data = response.json()
        return data.get("pair", {})
    except Exception as e:
        print("Pair detail hatası:", e)
        return {}


def calculate_simple_roi(pair_detail):
    try:
        current_price = float(pair_detail.get("priceUsd", 0))
        price_change_24h = float(pair_detail.get("priceChange", {}).get("h24", 0))

        if current_price == 0:
            return None

        # 24 saat önceki fiyat tahmini
        first_price_estimate = current_price / (1 + price_change_24h / 100)

        roi = current_price / first_price_estimate

        return {
            "first_price_estimate": first_price_estimate,
            "current_price": current_price,
            "roi": roi
        }

    except Exception as e:
        print("ROI hesaplama hatası:", e)
        return None
