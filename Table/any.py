# SELECT ProductName
# FROM Products
# WHERE ProductID = ANY
#   (SELECT ProductID
#   FROM OrderDetails
#   WHERE Quantity = 10);


import pandas as pd

# Sample 'Products' DataFrame
products_data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5']
}
products = pd.DataFrame(products_data)

# Sample 'OrderDetails' DataFrame
order_details_data = {
    'OrderDetailID': [101, 102, 103, 104],
    'ProductID': [1, 2, 3, 4],
    'Quantity': [10, 20, 10, 30]
}
order_details = pd.DataFrame(order_details_data)

# Step 1: Get the ProductIDs from OrderDetails where Quantity = 10
product_ids_with_quantity_10 = order_details[order_details['Quantity'] == 10]['ProductID']

# Step 2: Filter Products where ProductID is in the list from the above step
filtered_products = products[products['ProductID'].isin(product_ids_with_quantity_10)]

# Display the result (ProductName)
print(filtered_products[['ProductName']])
