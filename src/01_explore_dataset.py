
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Download the UCI Online Shoppers dataset
dataset = fetch_ucirepo(id=468)

# Input features and target variable
X = dataset.data.features
y = dataset.data.targets

# Combine them for exploration
df = pd.concat([X, y], axis=1)

from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

df.to_csv(data_folder / "online_shoppers_intention.csv", index=False)

print("Dataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head().to_string())

print("\nPurchase distribution:")
print(df["Revenue"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDATA TYPES")
print(df.dtypes)

print("\nVISITOR TYPES")
print(df["VisitorType"].value_counts())

print("\nAVERAGE PRODUCT PAGES BY PURCHASE OUTCOME")
print(df.groupby("Revenue")["ProductRelated"].mean())

# next step
print("\nPURCHASE RATE BY VISITOR TYPE")

purchase_rates = (
    df.groupby("VisitorType")["Revenue"]
    .agg(["count", "sum", "mean"])
)

purchase_rates["purchase_rate_percent"] = (
    purchase_rates["mean"] * 100
)

print(purchase_rates.round(2))
