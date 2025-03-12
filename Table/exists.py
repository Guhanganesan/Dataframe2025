# SELECT SupplierName
# FROM Suppliers
# WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);

import pandas as pd

# Sample 'Suppliers' DataFrame
suppliers_data = {
    'SupplierID': [1, 2, 3],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C']
}
suppliers = pd.DataFrame(suppliers_data)

# Sample 'Products' DataFrame
products_data = {
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
    'SupplierID': [1, 2, 2, 3, 1],
    'Price': [25, 15, 30, 10, 40]
}
products = pd.DataFrame(products_data)

# Step 1: Merge the Suppliers and Products DataFrames on SupplierID
merged = pd.merge(products, suppliers, on='SupplierID', how='inner')

# Step 2: Filter products with Price < 20
filtered = merged[merged['Price'] < 20]

# Step 3: Get unique suppliers that have products with Price < 20
suppliers_with_cheap_products = filtered['SupplierName'].unique()

# Display the result
print(suppliers_with_cheap_products)

# Ans: ['Supplier A' 'Supplier B']


