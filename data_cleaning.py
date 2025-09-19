import pandas as pd

# Load the dataset
df = pd.read_csv("raw_sales_data.csv")
print("Initial data shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# Handle missing values by filling them with the mean of the column
df = df.fillna(df.mean(numeric_only=True))
print("Missing numeric values filled with column mean.")

# Remove rows with any remaining missing values
df = df.dropna()
print("After dropping remaining missing values:", df.shape)

# Convert date columns to a standard format (YYYY-MM-DD)
if "date_column" in df.columns:
    df["date_column"] = pd.to_datetime(df["date_column"], errors="coerce")
    print("Date column formatted to YYYY-MM-DD.")

# Save the cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned data saved to cleaned_data.csv")