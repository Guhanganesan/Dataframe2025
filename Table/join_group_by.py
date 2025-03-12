# SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
# FROM Orders
# INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
# WHERE LastName = 'Davolio' OR LastName = 'Fuller'
# GROUP BY LastName
# HAVING COUNT(Orders.OrderID) > 25;

import pandas as pd

# Sample 'Employees' DataFrame
employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'LastName': ['Davolio', 'Fuller', 'Buchanan', 'Suyama', 'King']
}

employees = pd.DataFrame(employees_data)

# Sample 'Orders' DataFrame
orders_data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'EmployeeID': [1, 2, 3, 2, 1, 4, 5, 2, 3, 1, 1, 5, 2, 4, 1]
}

orders = pd.DataFrame(orders_data)

# Step 1: Perform INNER JOIN between Orders and Employees on EmployeeID
merged = pd.merge(orders, employees, on='EmployeeID', how='inner')

# Step 2: Filter where LastName is 'Davolio' or 'Fuller'
filtered = merged[merged['LastName'].isin(['Davolio', 'Fuller'])]

# Step 3: Group by LastName and count the number of orders for each employee
grouped = filtered.groupby('LastName')['OrderID'].count().reset_index()

# Step 4: Rename the 'OrderID' column to 'NumberOfOrders' and filter to keep only those with > 25 orders
grouped = grouped.rename(columns={'OrderID': 'NumberOfOrders'})
result = grouped[grouped['NumberOfOrders'] > 25]

# Display the result
print(result)

#    LastName  NumberOfOrders
# 0   Davolio              26
# 1    Fuller              27
