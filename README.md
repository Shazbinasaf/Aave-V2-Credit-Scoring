# Aave V2 Wallet Credit Scoring

## Overview

This project builds a wallet-level credit scoring system for users interacting with the Aave V2 DeFi protocol. The aim is to assign a credit score between 0 and 1000 to each wallet address based on their historical transaction behavior. The scoring reflects financial responsibility, where a higher score indicates more trustworthy behavior.

---

## Features

* Load and preprocess raw Aave V2 transaction data.
* Engineer features from wallet-level activity.
* Heuristically score wallets based on their behavior.
* Export final scores as JSON.
* Analyze and interpret the score distribution.

---

## Project Structure

```
aave-credit-scoring/
│
├── data/
│   └── user-wallet-transactions.json
│
├── src/
│   ├── main.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── scoring_model.py
│
├── wallet_scores.json
├── analysis.md
├── README.md
├── requirements.txt
└── .venv/
```

---

## Methodology

### 1. Preprocessing

We parse and flatten the nested transaction records from JSON, standardizing columns such as `wallet`, `type`, `amount`, `assetPriceUSD`, and `timestamp`.

### 2. Feature Engineering

We compute meaningful behavior-based features for each wallet:

* Total number of transactions
* Number of deposits, borrows, repayments, liquidations
* Total amount transacted
* Average asset price transacted

### 3. Scoring Logic

Each wallet is assigned a base score (e.g., 600), which is adjusted using simple heuristics:

* Reward:

  * Deposits: +5 points each
  * Repayments: +3 points each
  * Total volume: up to +100 points
* Penalty:

  * Borrows: -4 points each
  * Liquidations: -10 points each

Scores are clipped between 0 and 1000.

### 4. Output

Final scores are exported to `wallet_scores.json` for further analysis.

---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd aave-credit-scoring
   ```
2. Set up virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. Run scoring script:

   ```bash
   cd src
   python main.py
   ```

---

## Requirements

```
pandas
scikit-learn
matplotlib
seaborn
```

---

## Author

Shaz Bin Asaf
BTech AI & Data Science
2025

---

## License

This project is open-source under the MIT License.
