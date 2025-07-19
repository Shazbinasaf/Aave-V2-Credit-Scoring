# 📊 Credit Score Analysis (Aave V2 Wallets)

## 🔍 Objective

To understand how the generated credit scores (0–1000) from Aave V2 wallet transactions are distributed and what behavioral patterns emerge among high- and low-scoring wallets.

## 📈 Score Distribution

The histogram below (to be generated in a Jupyter Notebook or Python script) shows the distribution of wallet credit scores:

```python
import json
import matplotlib.pyplot as plt

# Load wallet scores
with open("wallet_scores.json") as f:
    scores = [entry['score'] for entry in json.load(f)]

# Plot distribution
plt.hist(scores, bins=10, edgecolor='black')
plt.title("Distribution of Wallet Credit Scores")
plt.xlabel("Credit Score Ranges")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.show()
```

This will help identify if the scores are balanced or skewed (e.g., too many wallets scoring high).

---

## 📉 Score Range Buckets

| Score Range | # Wallets | Observation                               |
| ----------- | --------- | ----------------------------------------- |
| 0–100       | X         | Likely exploitative or liquidated wallets |
| 100–200     | X         | Rarely interact, high borrow/no repay     |
| 200–400     | X         | Somewhat active, inconsistent behavior    |
| 400–600     | X         | Moderate borrowers and repayers           |
| 600–800     | X         | Frequent users, low risk                  |
| 800–1000    | X         | Highly reliable and responsible wallets   |

(Replace X with actual numbers after analyzing.)

---

## 💡 Behavior Observations

### Low Score Wallets (0–300)

* High liquidation call count
* Very few or no repayments
* Low number of deposits, often only borrow
* Sudden large amount withdrawals without consistent activity

### High Score Wallets (700–1000)

* Frequent and consistent deposits
* Borrow followed by timely repayment
* Low standard deviation in transaction amount (more stable behavior)
* Low or zero liquidations

---

## 🔁 Future Enhancements

* Integrate wallet age (first transaction date)
* Factor in asset types and volatility
* Include more refined pseudo-labels for supervised learning

---

## ✅ Conclusion

This analysis helps validate that the scoring model reasonably distinguishes between risky and reliable DeFi wallet behaviors. It provides a foundation to iterate and improve with domain-specific risk factors or supervised labels from known Aave loan outcomes.
