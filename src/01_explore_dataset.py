
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

#month purchase
print("\nPURCHASE RATE BY MONTH AND VISITOR TYPE")

monthly_rates = (
    df.groupby(["Month", "VisitorType"])["Revenue"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

monthly_rates["purchase_rate_percent"] = (
    monthly_rates["mean"] * 100
)

print(
    monthly_rates[
        ["Month", "VisitorType", "count",
         "sum", "purchase_rate_percent"]
    ].round(2).to_string(index=False)
)

#lesson 7 - median and mean 
print("\nPRODUCT PAGE VISITS — SUMMARY STATISTICS")

product_stats = (
    df.groupby("Revenue")["ProductRelated"]
    .agg(["count", "mean", "median", "min", "max", "std"])
)

print(product_stats.round(2))


#calculate percentiles
print("\nPRODUCT PAGE VISITS — PERCENTILES")

percentiles = (
    df.groupby("Revenue")["ProductRelated"]
    .quantile([0.25, 0.50, 0.75, 0.95])
    .unstack()
)

percentiles.columns = ["Q1 (25%)", "Median (50%)",
                       "Q3 (75%)", "P95 (95%)"]

print(percentiles.round(2))

#matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for generated figures
figures_dir = Path("figures")
figures_dir.mkdir(exist_ok=True)

# Separate sessions by purchase outcome
no_purchase = df.loc[df["Revenue"] == False, "ProductRelated"]
purchase = df.loc[df["Revenue"] == True, "ProductRelated"]

# Create two histograms side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(no_purchase, bins=40, color="steelblue")
axes[0].set_title("No Purchase")
axes[0].set_xlabel("Product Pages Visited")
axes[0].set_ylabel("Number of Sessions")

axes[1].hist(purchase, bins=40, color="darkorange")
axes[1].set_title("Purchase")
axes[1].set_xlabel("Product Pages Visited")
axes[1].set_ylabel("Number of Sessions")

fig.suptitle("Distribution of Product Page Visits")
plt.tight_layout()

output_path = figures_dir / "product_pages_histogram.png"
plt.savefig(output_path, dpi=150)
plt.close(fig)

print(f"\nHistogram saved to: {output_path}")


#normalization
import numpy as np

print("\nCREATING NORMALIZED HISTOGRAM")

# Shared intervals: 0-10, 10-20, ..., 190-200
bins = np.arange(0, 211, 10)

# Each session contributes an equal fraction of its group
no_purchase_weights = np.ones(len(no_purchase)) * 100 / len(no_purchase)
purchase_weights = np.ones(len(purchase)) * 100 / len(purchase)

fig, ax = plt.subplots(figsize=(11, 5))

ax.hist(
    no_purchase,
    bins=bins,
    weights=no_purchase_weights,
    alpha=0.6,
    label="No Purchase",
    color="steelblue"
)

ax.hist(
    purchase,
    bins=bins,
    weights=purchase_weights,
    alpha=0.6,
    label="Purchase",
    color="darkorange"
)

ax.set_title("Product Page Visits by Purchase Outcome")
ax.set_xlabel("Product Pages Visited")
ax.set_ylabel("Percentage of Sessions")
ax.legend()

plt.tight_layout()

output_path = figures_dir / "product_pages_normalized.png"
plt.savefig(output_path, dpi=150)
plt.close(fig)

print(f"Normalized histogram saved to: {output_path}")
