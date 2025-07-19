from preprocess import load_json
from feature_engineering import engineer_features
from scoring_model import generate_scores
import pandas as pd

def main():
    df = load_json("data/user-wallet-transactions.json")
    features = engineer_features(df)
    scores = generate_scores(features)

    features["score"] = scores
    features.reset_index().to_json("wallet_scores.json", orient="records", indent=2)
    print(" Wallet scores saved to wallet_scores.json")

if __name__ == "__main__":
    main()
