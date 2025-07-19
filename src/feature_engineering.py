import pandas as pd

def engineer_features(df):
    grouped = df.groupby("wallet")
    features = pd.DataFrame(index=grouped.groups.keys())

    features["total_txns"] = grouped.size()
    features["num_deposits"] = grouped["type"].apply(lambda x: (x == "deposit").sum())
    features["num_borrows"] = grouped["type"].apply(lambda x: (x == "borrow").sum())
    features["num_repays"] = grouped["type"].apply(lambda x: (x == "repay").sum())
    features["num_liquidations"] = grouped["type"].apply(lambda x: (x == "liquidationcall").sum())
    features["total_amount"] = grouped["amount"].sum()
    features["avg_asset_price"] = grouped["assetPriceUSD"].mean()

    return features.fillna(0)
