import pandas as pd

# Sample DataFrame (Customers)
data = {
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Cardinal'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Tom B. Erichsen'],
    'Address': ['Obere Str. 57', 'Avda. de la Constitución 2222', 'Mataderos 2314', 'Skagen 21'],
    'City': ['Berlin', 'México D.F.', 'México D.F.', 'Stavanger'],
    'PostalCode': ['12209', '05021', '05023', '4006'],
    'Country': ['Germany', 'Mexico', 'Mexico', 'Norway']
}

df = pd.DataFrame(data)

# 1. Using Aliases for Columns (Renaming)
df_aliased = df.rename(columns={'CustomerName': 'Name', 'City': 'Location'})

# Displaying the DataFrame with column aliases
print("=== DataFrame with Column Aliases ===")
print(df_aliased)

print("\n")

# 2. Simulating Table Alias (Using Multiple DataFrames)
# Let's simulate a "table alias" by creating another DataFrame with a different variable name
df_customers = df  # This can be seen as the "Customers" table in SQL
df_alias = df_customers[['CustomerID', 'Name', 'Location']]  # Use 'Name' and 'Location' columns, applying alias logic

# Displaying the aliased table
print("=== DataFrame with Table Alias (df_alias) ===")
print(df_alias)