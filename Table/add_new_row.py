# INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
# VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

# In pandas, there isn't an `INSERT INTO` SQL-like operation, but you can **add a new row** to a DataFrame using several methods, such as `loc[]`, `append()`, or `concat()`.

### Example: Adding a New Row to a DataFrame

# To simulate an **`INSERT INTO`** SQL query like the one you provided, you can add a new row to your pandas DataFrame using `loc[]` or `append()`.

# Here’s how to do that:

### 1. **Using `loc[]`**:
#python
import pandas as pd

# Sample DataFrame (Customers)
data = {
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno'],
    'Address': ['Obere Str. 57', 'Avda. de la Constitución 2222', 'Mataderos 2314'],
    'City': ['Berlin', 'México D.F.', 'México D.F.'],
    'PostalCode': ['12209', '05021', '05023'],
    'Country': ['Germany', 'Mexico', 'Mexico']
}

df = pd.DataFrame(data)

# New row to insert
new_row = {
    'CustomerName': 'Cardinal',
    'ContactName': 'Tom B. Erichsen',
    'Address': 'Skagen 21',
    'City': 'Stavanger',
    'PostalCode': '4006',
    'Country': 'Norway'
}

# Using loc[] to insert the new row
df.loc[len(df)] = new_row

# Display the updated DataFrame
print(df)
#

### Output:
#
#                       CustomerName         ContactName                        Address          City PostalCode  Country
# 0             Alfreds Futterkiste           Maria Anders               Obere Str. 57        Berlin       12209   Germany
# 1  Ana Trujillo Emparedados y helados           Ana Trujillo  Avda. de la Constitución 2222   México D.F.       05021    Mexico
# 2                Antonio Moreno Taquería      Antonio Moreno              Mataderos 2314   México D.F.       05023    Mexico
# 3                        Cardinal         Tom B. Erichsen                    Skagen 21     Stavanger       4006    Norway
#

### 2. **Using `append()` Method** (Deprecated in Pandas 2.0, prefer `concat()`):
#python
# New row as a DataFrame (for append method)
new_row_df = pd.DataFrame([{
    'CustomerName': 'Cardinal',
    'ContactName': 'Tom B. Erichsen',
    'Address': 'Skagen 21',
    'City': 'Stavanger',
    'PostalCode': '4006',
    'Country': 'Norway'
}])

# Use append to add the new row to the existing DataFrame
df = df.append(new_row_df, ignore_index=True)

# Display the updated DataFrame
print(df)
#

### Output:
#
#                       CustomerName         ContactName                        Address          City PostalCode  Country
# 0             Alfreds Futterkiste           Maria Anders               Obere Str. 57        Berlin       12209   Germany
# 1  Ana Trujillo Emparedados y helados           Ana Trujillo  Avda. de la Constitución 2222   México D.F.       05021    Mexico
# 2                Antonio Moreno Taquería      Antonio Moreno              Mataderos 2314   México D.F.       05023    Mexico
# 3                        Cardinal         Tom B. Erichsen                    Skagen 21     Stavanger       4006    Norway
#

### 3. **Using `concat()` Method** (Recommended with newer versions of pandas):
#python
# New row as a DataFrame (for concat method)
new_row_df = pd.DataFrame([{
    'CustomerName': 'Cardinal',
    'ContactName': 'Tom B. Erichsen',
    'Address': 'Skagen 21',
    'City': 'Stavanger',
    'PostalCode': '4006',
    'Country': 'Norway'
}])

# Use concat to add the new row to the existing DataFrame
df = pd.concat([df, new_row_df], ignore_index=True)

# Display the updated DataFrame
print(df)
#

### Output:
#
#                       CustomerName         ContactName                        Address          City PostalCode  Country
# 0             Alfreds Futterkiste           Maria Anders               Obere Str. 57        Berlin       12209   Germany
# 1  Ana Trujillo Emparedados y helados           Ana Trujillo  Avda. de la Constitución 2222   México D.F.       05021    Mexico
# 2                Antonio Moreno Taquería      Antonio Moreno              Mataderos 2314   México D.F.       05023    Mexico
# 3                        Cardinal         Tom B. Erichsen                    Skagen 21     Stavanger       4006    Norway
#

# For Multiple Values

import pandas as pd

# Sample DataFrame (Customers)
data = {
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno'],
    'Address': ['Obere Str. 57', 'Avda. de la Constitución 2222', 'Mataderos 2314'],
    'City': ['Berlin', 'México D.F.', 'México D.F.'],
    'PostalCode': ['12209', '05021', '05023'],
    'Country': ['Germany', 'Mexico', 'Mexico']
}

df = pd.DataFrame(data)

# New rows to insert (as a DataFrame)
new_rows = pd.DataFrame([
    {'CustomerName': 'Cardinal', 'ContactName': 'Tom B. Erichsen', 'Address': 'Skagen 21', 'City': 'Stavanger', 'PostalCode': '4006', 'Country': 'Norway'},
    {'CustomerName': 'Greasy Burger', 'ContactName': 'Per Olsen', 'Address': 'Gateveien 15', 'City': 'Sandnes', 'PostalCode': '4306', 'Country': 'Norway'},
    {'CustomerName': 'Tasty Tee', 'ContactName': 'Finn Egan', 'Address': 'Streetroad 19B', 'City': 'Liverpool', 'PostalCode': 'L1 0AA', 'Country': 'UK'}
])

# Using concat to add new rows
df = pd.concat([df, new_rows], ignore_index=True)

# Display the updated DataFrame
print(df)


# Adding rows using loc[]:
df.loc[len(df)] = ['Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway']
df.loc[len(df)] = ['Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway']
df.loc[len(df)] = ['Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK']

# Display the updated DataFrame
print(df)