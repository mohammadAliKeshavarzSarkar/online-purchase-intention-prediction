
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split

# 1. Load the UCI dataset
dataset = fetch_ucirepo(id=468)

X = dataset.data.features
y = dataset.data.targets["Revenue"]

# 2. Divide observations into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 3. Inspect the results
print("TRAINING AND TESTING SETS")

print("\nTraining features:", X_train.shape)
print("Testing features:", X_test.shape)

print("\nTraining target distribution:")
print(y_train.value_counts())
print(y_train.value_counts(normalize=True) * 100)

print("\nTesting target distribution:")
print(y_test.value_counts())
print(y_test.value_counts(normalize=True) * 100)




# LESSON 12 — INVESTIGATING PAGEVALUES
# Combine features and target for exploratory analysis only
analysis_df = X.copy()
analysis_df["Revenue"] = y

print("\nPAGEVALUES — BY PURCHASE OUTCOME")

print(
    analysis_df.groupby("Revenue")["PageValues"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(3)
)

print("\nPERCENTAGE WITH PAGEVALUES > 0")

print(
    analysis_df.groupby("Revenue")["PageValues"]
    .apply(lambda values: (values > 0).mean() * 100)
    .round(2)
)

print("\nPAGEVALUES CORRELATION WITH REVENUE")

print(
    analysis_df["PageValues"].corr(
        analysis_df["Revenue"].astype(int)
    )
)



# LESSON 13 — CATEGORICAL FEATURES

categorical_features = [
    "Month",
    "VisitorType",
    "Browser",
    "OperatingSystems",
    "Region",
    "TrafficType",
    "Weekend"
]

print("\nCATEGORICAL FEATURE ANALYSIS")

for feature in categorical_features:

    print(f"\nFeature: {feature}")

    print("Data type:", X_train[feature].dtype)

    print("Number of unique categories:",
          X_train[feature].nunique())

    print("Unique categories:",
          X_train[feature].unique())

    print("Category distribution:")
    print(X_train[feature].value_counts())



# LESSON 13 — ONE-HOT ENCODING

from sklearn.preprocessing import OneHotEncoder

one_hot_features = [
    "Month",
    "VisitorType",
    "Browser",
    "OperatingSystems",
    "Region",
    "TrafficType"
]

encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

X_train_encoded = encoder.fit_transform(
    X_train[one_hot_features]
)

X_test_encoded = encoder.transform(
    X_test[one_hot_features]
)

encoded_feature_names = encoder.get_feature_names_out(
    one_hot_features
)

print("\nONE-HOT ENCODING RESULTS")

print("Training shape:", X_train_encoded.shape)
print("Testing shape:", X_test_encoded.shape)

print("\nEncoded feature names:")
print(encoded_feature_names)

encoded_df = pd.DataFrame(
    X_train_encoded,
    columns=encoded_feature_names,
    index=X_train.index
)

print("\nVISITOR TYPE — BEFORE AND AFTER ENCODING")

visitor_comparison = pd.concat([
    X_train[["VisitorType"]],
    encoded_df[[
        "VisitorType_New_Visitor",
        "VisitorType_Other",
        "VisitorType_Returning_Visitor"
    ]]
], axis=1)

print(visitor_comparison.head(10).to_string())
