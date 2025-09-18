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

This repository is organized into feature-specific branches and modules:

- Data Cleaning Script

    - Automates removal of nulls, duplicates, and unwanted characters.

    - Standardizes formats (e.g., dates, casing).

- Data Transformation Script

    - Applies business logic transformations.

    - Handles column renaming, aggregations, and feature engineering.

- Data Loading Script

    - Writes data to structured files (e.g., CSV, Parquet).

    - Ensures reproducibility and consistency in saved outputs.


---


## Code Examples

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
```

---


## Contribution Guide

Follow these steps to contribute to the toolkit and enhance its functionality.

1. Fork this repository and clone it locally.

   ```bash
   git clone [https://github.com/your-username/data-engineering-toolkit.git](https://github.com/your-username/data-engineering-toolkit.git)
   cd data-engineering-toolkit

2. Create a new feature branch from develop using the format below. All new work should be done on a dedicated `feature branch`.

    ```bash
    git checkout develop
    git pull origin develop
    git checkout -b feature/add-new-loading-scri
    ```


3. Commit changes frequently with clear commit messages.


4. Push your branch and open a Pull Request from your `feature branch` into `develop`.

    - Include a summary of changes.

    - Add code examples or screenshots if relevant.

    - Provide testing instructions.


6. The PR will be reviewed and once approved, it will be merged into `develop`.
