##want to update values in a DataFrame based on specific conditions, #can use conditional indexing. Below are a few examples to help you:

### 1. **Update Based on a Condition for a Single Column**
#can use `loc` with a condition to update values in a specific column.

#python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Update column 'A' where values in 'B' are greater than 30
df.loc[df['B'] > 30, 'A'] = 100  # Set values in column 'A' to 100 where 'B' > 30

print(df)
#

### 2. **Update Multiple Columns Based on a Condition**
#can apply conditions to multiple columns and update them accordingly.

#python
# Update both columns 'A' and 'B' where 'A' is greater than 2
df.loc[df['A'] > 2, ['A', 'B']] = [50, 500]

print(df)
#

### 3. **Update Using Multiple Conditions**
#can combine multiple conditions using logical operators (e.g., `&` for AND, `|` for OR).

#python
# Update 'A' where 'B' is greater than 20 and 'A' is less than 5
df.loc[(df['B'] > 20) & (df['A'] < 5), 'A'] = 200

print(df)
#

### 4. **Updating Based on a Condition with `apply`**
#your condition involves more complex logic, #can use the `apply()` function.

#python
# Example using apply to modify column 'A' based on custom conditions
# def update_values(row):
#     row['B'] > 20:
#         return 100  
#     return row['A']

# df['A'] = df.apply(update_values, axis=1)
# print(df)
#

### 5. **Using `np.where()` for Conditional Updates**
#Another way to perform conditional updates is using `numpy.where()`. This is especially useful for element-wise conditions.

#python
import numpy as np

# Update 'A' using np.where where 'B' is greater than 20
df['A'] = np.where(df['B'] > 20, 999, df['A'])

print(df)
#

### Example Output:

# For this example:

#python
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})
#

# After applying the conditional update:

#python
df.loc[df['B'] > 30, 'A'] = 100
#

# The DataFrame will look like:

#
#      A   B
# 0    1  10
# 1    2  20
# 2    3  30
# 3  100  40
# 4  100  50
#

