# SELECT ProductID, ProductName, CategoryName
# FROM Products
# INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

import pandas as pd

# Sample 'Products' DataFrame
products_data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['Apple', 'Banana', 'Carrot', 'Date', 'Eggplant'],
    'CategoryID': [1, 2, 3, 2, 1]
}

products = pd.DataFrame(products_data)

# Sample 'Categories' DataFrame
categories_data = {
    'CategoryID': [1, 2, 3],
    'CategoryName': ['Fruits', 'Vegetables', 'Root Vegetables']
}

categories = pd.DataFrame(categories_data)

# Perform the INNER JOIN (pandas equivalent of SQL INNER JOIN)
result = pd.merge(products, categories, on='CategoryID', how='inner')

# Select relevant columns: ProductID, ProductName, CategoryName
result = result[['ProductID', 'ProductName', 'CategoryName']]

# Display the result
print(result)


#    ProductID ProductName        CategoryName
# 0          1       Apple               Fruits
# 1          5   Eggplant               Fruits
# 2          2      Banana          Vegetables
# 3          4        Date          Vegetables
