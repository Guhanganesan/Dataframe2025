import pandas as pd

# Sample DataFrame with Country column
data = {
    'CustomerName': [
        'Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería',
        'Around the Horn', 'Berglunds snabbköp', 'Blauer See Delikatessen', 'Blondel père et fils',
        'Bólido Comidas preparadas', 'Bon app\'', 'Bottom-Dollar Marketse', 'B\'s Beverages',
        'Cactus Comidas para llevar', 'Centro comercial Moctezuma'
    ],
    'City': [
        'Berlin', 'México D.F.', 'México D.F.', 'London', 'Luleå', 'Mannheim', 'Strasbourg', 'Madrid', 
        'Marseille', 'Tsawassen', 'London', 'Buenos Aires', 'México D.F.'
    ],
    'Country': [
        'Germany', 'Mexico', 'Mexico', 'UK', 'Sweden', 'Germany', 'France', 'Spain', 'France', 'Canada', 'UK', 'Argentina', 'Mexico'
    ]
}

df = pd.DataFrame(data)

# Filter rows where the Country is 'Mexico'
df_mexico = df.loc[df['Country'] == 'Mexico']

# Display the filtered DataFrame
print(df_mexico)
