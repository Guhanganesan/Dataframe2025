# SELECT COUNT(CustomerID), Country
# FROM Customers
# GROUP BY Country
# ORDER BY COUNT(CustomerID) DESC;

import pandas as pd

# Sample 'Customers' DataFrame
customers_data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7],
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 
                     'Around the Horn', 'Berglunds snabbköp', 'Blauer See Delikatessen', 'Blondel père et fils'],
    'Country': ['Germany', 'Mexico', 'Mexico', 'UK', 'Sweden', 'Germany', 'France']
}

customers = pd.DataFrame(customers_data)

# 1. Group by 'Country' and count the number of 'CustomerID' in each group
country_counts = customers.groupby('Country')['CustomerID'].count().reset_index()

# 2. Rename the count column to 'CustomerCount'
country_counts = country_counts.rename(columns={'CustomerID': 'CustomerCount'})

# 3. Sort the result by 'CustomerCount' in descending order
country_counts_sorted = country_counts.sort_values('CustomerCount', ascending=False)

# Display the result
print(country_counts_sorted)

#    Country  CustomerCount
# 0  Mexico              2
# 1  Germany             2
# 2  UK                  1
# 3  Sweden              1
# 4  France              1
