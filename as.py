import pandas as pd

# 1. Create a dictionary with sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 22, 35],
    "City": ["New York", "London", "Paris", "Tokyo"]
}

# 2. Convert the dictionary into a pandas DataFrame (a 2D table)
df = pd.DataFrame(data)

# 3. Print the complete table
print("--- Full DataFrame ---")
print(df)

# 4. Filter and display rows where Age is greater than 25
print("\n--- People older than 25 ---")
older_than_25 = df[df["Age"] > 25]
print(older_than_25)

