import pandas as pd

# Sample DataFrame with multiple columns
data = {
    'CustomerID': [1, 15, 30, 45, 70, 80, 100],
    'CustomerName': ['Anna', 'George', 'Antonio', 'Alfred', 'Gustavo', 'Giovanni', 'Blake'],
    'Country': ['Spain', 'Germany', 'Italy', 'Spain', 'France', 'Spain', 'Mexico'],
    'City': ['Madrid', 'Berlin', 'Rome', 'Barcelona', 'Paris', 'London', 'Mexico City']
}

df = pd.DataFrame(data)

# Apply multiple conditions:
df_filtered = df[
    (df['Country'] != 'Spain') &  # Country is NOT 'Spain'
    (~df['CustomerName'].str.startswith('A')) &  # CustomerName does NOT start with 'A'
    (~df['CustomerID'].between(10, 60)) &  # CustomerID is NOT between 10 and 60
    (~df['City'].isin(['Paris', 'London']))  # City is NOT in ['Paris', 'London']
]

# Display the filtered DataFrame
print(df_filtered)
