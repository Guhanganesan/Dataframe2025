import pandas as pd

# Sample DataFrame (Customers)
# UPDATE Customers
# SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
# WHERE CustomerID = 1;


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

# Update the row where CustomerID is 1
df.loc[df['CustomerID'] == 1, ['ContactName', 'City']] = ['Alfred Schmidt', 'Frankfurt']

# Display the updated DataFrame
print(df)
