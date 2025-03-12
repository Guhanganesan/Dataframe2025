# In pandas, you can **order** or **sort** the DataFrame by a specific column using the `.sort_values()` method. If you want to order the rows by a column, such as `Price`, you can do it like this.

### Example: Sort Data by `Price` Column

# Assuming you have a DataFrame with a `Price` column and you want to sort it in ascending or descending order:

#python
import pandas as pd

# Sample DataFrame with a Price column
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Price': [10.5, 15.0, 7.25, 20.0]
}

df = pd.DataFrame(data)

# Sort by 'Price' in ascending order (default)
df_sorted_asc = df.sort_values(by='Price')

# Display the sorted DataFrame
print("Sorted by Price (ascending):")
print(df_sorted_asc)
#

### Output:

#
# Sorted by Price (ascending):
#       Product  Price
# 2  Product C   7.25
# 0  Product A  10.50
# 1  Product B  15.00
# 3  Product D  20.00
#

### Example: Sort by `Price` in Descending Order

# To sort by `Price` in descending order, you can use the `ascending=False` parameter:

#python
# Sort by 'Price' in descending order
df_sorted_desc = df.sort_values(by='Price', ascending=False)

# Display the sorted DataFrame
print("Sorted by Price (descending):")
print(df_sorted_desc)
#

### Output:

#
# Sorted by Price (descending):
#       Product  Price
# 3  Product D  20.00
# 1  Product B  15.00
# 0  Product A  10.50
# 2  Product C   7.25
#

### Multiple Column Sort

# If you want to sort by multiple columns, you can pass a list to the `by` parameter:

#python
# Sample DataFrame with multiple columns
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Price': [10.5, 15.0, 7.25, 15.0],
    'Stock': [100, 50, 150, 50]
}

df = pd.DataFrame(data)

# Sort by 'Price' in ascending order, and 'Stock' in descending order
df_sorted_multi = df.sort_values(by=['Price', 'Stock'], ascending=[True, False])

print("Sorted by Price (ascending) and Stock (descending):")
print(df_sorted_multi)
#

### Output:

#
# Sorted by Price (ascending) and Stock (descending):
#       Product  Price  Stock
# 2  Product C   7.25    150
# 0  Product A  10.50    100
# 1  Product B  15.00     50
# 3  Product D  15.00     50
#