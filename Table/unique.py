# To get distinct (unique) values from a specific column in a pandas DataFrame, you can use the `.unique()` method or `.drop_duplicates()`. Both will return the unique values in a column, but they work slightly differently.

### 1. **Using `.unique()` Method**
# The `.unique()` method returns the unique values as a NumPy array.

#python
import pandas as pd

# Sample DataFrame
data = {
    'CustomerName': [
        'Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería',
        'Around the Horn', 'Berglunds snabbköp', 'Blauer See Delikatessen', 'Blondel père et fils',
        'Bólido Comidas preparadas', 'Bon app\'', 'Bottom-Dollar Marketse', 'B\'s Beverages',
        'Cactus Comidas para llevar', 'Centro comercial Moctezuma'
    ],
    'City': [
        'Berlin', 'México D.F.', 'México D.F.', 'London', 'Luleå', 'Mannheim', 'Strasbourg', 'Madrid', 
        'Marseille', 'Tsawassen', 'London', 'Buenos Aires', 'México D.F.'
    ]
}

df = pd.DataFrame(data)

# Get unique values from the 'City' column
unique_cities = df['City'].unique()

print(unique_cities)
#

### Output:
#
# ['Berlin' 'México D.F.' 'London' 'Luleå' 'Mannheim' 'Strasbourg' 'Madrid'
#  'Marseille' 'Tsawassen' 'Buenos Aires']
#

### 2. **Using `.drop_duplicates()` Method**
# The `.drop_duplicates()` method returns a DataFrame with unique values. You can use it if you want the result as a DataFrame rather than a NumPy array.

#python
# Get distinct values from the 'City' column and return it as a DataFrame
unique_cities_df = df['City'].drop_duplicates()

print(unique_cities_df)
#

### Output:
#
# 0           Berlin
# 1       México D.F.
# 3           London
# 4            Luleå
# 5         Mannheim
# 6       Strasbourg
# 7           Madrid
# 8         Marseille
# 9        Tsawassen
# 11    Buenos Aires
# Name: City, dtype: object
#

### 3. **Using `groupby()` (Another Approach)**
# You can also get distinct values using `groupby()` and then access the unique column values:

#python
# Group by 'City' and get unique values
unique_cities_groupby = df.groupby('City').size().index

print(unique_cities_groupby)
#

### Output:
#
# Index(['Berlin', 'Buenos Aires', 'London', 'Luleå', 'Madrid', 'Mannheim',
#        'Marseille', 'México D.F.', 'Strasbourg', 'Tsawassen'],
#       dtype='object', name='City')
#