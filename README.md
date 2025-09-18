# DATA ENGINEERING TOOLKIT

This project was created as part of the [Data Engineering Community](https://dataengineeringcommunity.com/) LaunchPad, with the goal of building practical, job-ready skills through hands-on exercises.

This repository is a collection of beginner-friendly scripts and resources designed to practice and demonstrate core Data Engineering skills. It follows best practices in version control with the Gitflow branching strategy, incorporates GitHub workflows, and simulates collaboration through pull requests and code reviews.

The toolkit focuses on the fundamental building blocks of a data pipeline:

- Cleaning raw data

- Transforming data into usable formats

- Loading data into storage

Here is an overview of the Gitflow branching model used for this project::

- ***Main branch***: for stable, production-ready code.

- ***Develop branch***: for integration.

- ***Feature branches***: *(feature/branch-name)* for new features or scripts.

---

## Documentation

---

## Code Examples

<<<<<<< HEAD
*Example: Data Transformation*

The following is an example from the src/ directory, showcasing a function that transforms raw data into a more usable format. This function takes a Pandas DataFrame and aggregates it to calculate key metrics.

```python
# src/data_transformation.py
import pandas as pd

def calculate_daily_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily sales and average transaction value from a raw transactions DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with 'transaction_date' and 'transaction_amount' columns.

    Returns:
        pd.DataFrame: A new DataFrame with daily aggregated metrics.
    """
    # Ensure the date column is in datetime format
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    # Group by date and calculate total sales and transaction count
    daily_summary = df.groupby(df['transaction_date'].dt.date).agg(
        total_sales=('transaction_amount', 'sum'),
        total_transactions=('transaction_amount', 'count')
    ).reset_index()

    # Calculate average transaction value
    daily_summary['avg_transaction_value'] = daily_summary['total_sales'] / daily_summary['total_transactions']
    
    return daily_summary

if __name__ == '__main__':
    # Sample data
    data = {
        'transaction_date': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02'],
        'transaction_amount': [10.50, 20.00, 15.00, 25.50]
    }
    sample_df = pd.DataFrame(data)

    # Apply the transformation
    transformed_df = calculate_daily_metrics(sample_df)
    print("Transformed Daily Metrics DataFrame:")
    print(transformed_df)
=======
*Example: Data Cleaning*

The following is an example code showcasing a function that cleans raw data into a more usable format.


```python

# src/data_transformation.py

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
>>>>>>> a4587b9 (updated README)

---

## Contribution Guide

Contributions are welcome! Follow these steps to contribute to the toolkit and enhance its functionality. Please follow the instruction below;

1. Fork this repository and clone it locally.

```bash

git clone https://github.com/your-username/data-engineering-toolkit.git
cd data-engineering-toolkit


2. Create a new `feature branch` from `develop` using the format below. ***All new work should be done on a dedicated `feature branch`.***

```bash
git checkout develop
git pull origin develop
git checkout -b feature/add-new-loading-scri


3. Commit changes frequently with clear commit messages.


4. Push your branch and open a Pull Request from your `feature branch` into `develop`.

- Include a summary of changes.

- Add code examples or screenshots if relevant.

- Provide testing instructions.


6. The PR will be reviewed and once approved, it will be merged into `develop`.
