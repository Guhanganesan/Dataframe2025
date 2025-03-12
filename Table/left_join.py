# SELECT Customers.CustomerName, Orders.OrderID
# FROM Customers
# LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
# ORDER BY Customers.CustomerName;

import pandas as pd

# Sample 'Customers' DataFrame
customers_data = {
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Cardinal']
}

customers = pd.DataFrame(customers_data)

# Sample 'Orders' DataFrame
orders_data = {
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 2, 3]
}

orders = pd.DataFrame(orders_data)

# Perform the LEFT JOIN (pandas equivalent of SQL LEFT JOIN)
result = pd.merge(customers, orders, on='CustomerID', how='left')

# Select relevant columns: CustomerName and OrderID
result = result[['CustomerName', 'OrderID']]

# Sort by CustomerName (similar to ORDER BY Customers.CustomerName)
result = result.sort_values('CustomerName')

# Display the result
print(result)
