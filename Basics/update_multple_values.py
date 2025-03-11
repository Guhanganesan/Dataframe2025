# If you want to update column **B** with the value **10** where **A** is in the set `(1, 2, 3, 4, 5)`, 
# you can do this using conditional indexing with `loc` and the `isin()` function, which checks if the values in column **A** are in the specified set.

# Here's how you can do it:

#python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7],
    'B': [10, 20, 30, 40, 50, 60, 70]
})

# Update column 'B' where column 'A' is in the set (1, 2, 3, 4, 5)
df.loc[df['A'].isin([1, 2, 3, 4, 5]), 'B'] = 10

print(df)
#

### Output:

#
#    A   B
# 0  1  10
# 1  2  10
# 2  3  10
# 3  4  10
# 4  5  10
# 5  6  60
# 6  7  70
#

### Explanation:
# - `df['A'].isin([1, 2, 3, 4, 5])` creates a boolean mask where it checks if the values in column **A** are in the list `[1, 2, 3, 4, 5]`.
# - `df.loc[<condition>, 'B'] = 10` updates column **B** to `10` where the condition is true.