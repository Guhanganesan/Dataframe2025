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

# MIN: Find the smallest PostalCode (lexicographically as they are strings)
min_value = df['PostalCode'].min()
print("MIN PostalCode:", min_value)

# MAX: Find the largest PostalCode (lexicographically as they are strings)
max_value = df['PostalCode'].max()
print("MAX PostalCode:", max_value)

# COUNT: Count the number of rows in CustomerName
row_count = df['CustomerName'].count()
print("COUNT CustomerName:", row_count)

# SUM: If we had a numeric column like 'Sales', we would use df['Sales'].sum()
# For demonstration, using 'PostalCode' to show sum behavior (though not applicable here)
sum_value = df['PostalCode'].apply(pd.to_numeric, errors='coerce').sum()  # Convert to numeric and sum
print("SUM PostalCode (numeric conversion):", sum_value)

# AVG: Calculate the average of a numerical column (if applicable)
avg_value = df['PostalCode'].apply(pd.to_numeric, errors='coerce').mean()  # Convert to numeric and calculate mean
print("AVG PostalCode (numeric conversion):", avg_value)
