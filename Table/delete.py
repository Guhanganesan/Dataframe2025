# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

import pandas as pd

# Sample DataFrame (Customers)
data = {
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Cardinal'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Tom B. Erichsen'],
    'Address': ['Obere Str. 57', 'Avda. de la Constitución 2222', 'Mataderos 2314', 'Skagen 21'],
    'City': ['Berlin', 'México D.F.', 'México D.F.', 'Stavanger'],
    'PostalCode': ['12209', '05021', '05023', '4006'],
    'Country': ['Germany', 'Mexico', 'Mexico', 'Norway']
}

df = pd.DataFrame(data)

# Delete rows where CustomerName is 'Alfreds Futterkiste'
df = df[df['CustomerName'] != 'Alfreds Futterkiste']

# Display the updated DataFrame
print(df)