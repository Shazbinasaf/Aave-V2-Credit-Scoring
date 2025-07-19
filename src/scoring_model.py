import numpy as np

def generate_scores(features):
    scores = []

    for _, row in features.iterrows():
        score = 600  # base

        # Reward deposit/repay behavior
        score += 5 * row["num_deposits"]
        score += 3 * row["num_repays"]

        # Penalize borrow/liquidation
        score -= 4 * row["num_borrows"]
        score -= 10 * row["num_liquidations"]

        # Adjust for volume
        score += min(row["total_amount"] * 0.05, 100)

        score = max(0, min(1000, int(score)))
        scores.append(score)

    return scores
