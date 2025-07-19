import pandas as pd
import json

def load_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    flat_records = []

    for record in data:
        flat = {
            "wallet": record.get("userWallet"),
            "type": record.get("action", "").lower(),
            "timestamp": record.get("timestamp"),
        }

        action_data = record.get("actionData", {})
        flat["amount"] = float(action_data.get("amount", 0)) / (10 ** 6)
        flat["asset"] = action_data.get("assetSymbol", None)
        flat["assetPriceUSD"] = float(action_data.get("assetPriceUSD", 0))
        flat_records.append(flat)

    return pd.DataFrame(flat_records)
