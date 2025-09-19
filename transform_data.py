import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_sales_data.csv")
print("Initial data shape:", df.shape)

#  1. Aggregation - Group by product and calculate total and average sales
agg_df = df.groupby("product").agg(
    total_sales=("sales", "sum"),
    avg_sales=("sales", "mean")
).reset_index()
print("Aggregation complete. Sample:")
print(agg_df.head())

# 2. Filtering - Keep only rows where sales > 100
filtered_df = df[df["sales"] > 100]
print("Filtering complete. New shape:", filtered_df.shape)

# 3. Pivoting / Melting - Pivot: total sales per product per region
pivot_df = df.pivot_table(
    index="product", 
    columns="region", 
    values="sales", 
    aggfunc="sum"
).reset_index()
print("Pivoting complete. Sample:")
print(pivot_df.head())

# 4. Deriving New Features - Create a new column 'total_value' = price * quantity
df["total_value"] = df["price"] * df["quantity"]
print("New feature 'total_value' created. Sample:")
print(df[["product", "price", "quantity", "total_value"]].head())

# 5. Joining / Merging - Suppose we have another dataset with product info
product_info = pd.DataFrame({
    "product": ["A", "B", "C"],
    "category": ["Electronics", "Clothing", "Home"]
})

merged_df = df.merge(product_info, on="product", how="left")
print("Merging complete. Sample:")
print(merged_df.head())

# Save transformed data
merged_df.to_csv("transformed_sales_data.csv", index=False)
print("Transformed data saved to transformed_sales_data.csv")
