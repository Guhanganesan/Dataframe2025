# To filter rows in a pandas DataFrame with multiple conditions, you can use conditional indexing (similar to a SQL `WHERE` clause). Here's how you can apply the conditions `Country = 'Spain'` and `CustomerName LIKE 'G%'` in pandas.

### Example: Filter Data with Multiple Conditions
###  WHERE Country = 'Spain' AND CustomerName LIKE 'G%';

# Assume you have a DataFrame with a **Country** column and a **CustomerName** column, and you want to filter rows where:
# - **Country** is `'Spain'`
# - **CustomerName** starts with the letter `'G'` (like the SQL `LIKE 'G%'` condition)

# Here’s how to do that:

#python
import pandas as pd

# Sample DataFrame
data = {
    'CustomerName': [
        'George Wells', 'Gustavo Orosco', 'Giovanni Rizzo', 'Ana Trujillo Emparedados y helados', 
        'Antonio Moreno Taquería', 'Around the Horn', 'Gerry Greenspan', 'Bólido Comidas preparadas'
    ],
    'City': [
        'Madrid', 'Barcelona', 'Seville', 'México D.F.', 'México D.F.', 'London', 'Madrid', 'Madrid'
    ],
    'Country': [
        'Spain', 'Spain', 'Spain', 'Mexico', 'Mexico', 'UK', 'Spain', 'Spain'
    ]
}

df = pd.DataFrame(data)

# Filter the DataFrame where Country is 'Spain' and CustomerName starts with 'G'
df_filtered = df[(df['Country'] == 'Spain') & (df['CustomerName'].str.startswith('G'))]

# Display the filtered DataFrame
print(df_filtered)
#

### Output:

#
#     CustomerName     City Country
# 0    George Wells   Madrid   Spain
# 1  Gustavo Orosco  Barcelona   Spain
# 2   Giovanni Rizzo  Seville   Spain
# 6   Gerry Greenspan   Madrid   Spain
# #

### Explanation:
# - `(df['Country'] == 'Spain')`: This checks if the **Country** column is `'Spain'`.
# - `(df['CustomerName'].str.startswith('G'))`: This checks if the **CustomerName** starts with the letter `'G'`, similar to SQL’s `LIKE 'G%'` condition.
# - The `&` operator combines these two conditions, and we use parentheses `()` to ensure proper evaluation order.

### Alternative: Using `.str.contains()` (for more complex pattern matching)
# If you want to use more advanced pattern matching (such as SQL’s `LIKE` with wildcards), you can use the `.str.contains()` method, which allows for regex-based filtering. Here's an example with the `LIKE 'G%'` condition using `.str.contains()`:

#python
# Using .str.contains() to match names that start with 'G'
df_filtered = df[(df['Country'] == 'Spain') & (df['CustomerName'].str.contains('^G', regex=True))]

# Display the filtered DataFrame
print(df_filtered)
#

### Output (same as above):

#
#     CustomerName     City Country
# 0    George Wells   Madrid   Spain
# 1  Gustavo Orosco  Barcelona   Spain
# 2   Giovanni Rizzo  Seville   Spain
# 6   Gerry Greenspan   Madrid   Spain
# #

### Explanation of `.str.contains()`:
# - `'^G'`: The caret `^` indicates that the string should start with `G`, effectively achieving the same result as `LIKE 'G%'` in SQL.

# Let me know if you need further details or examples!