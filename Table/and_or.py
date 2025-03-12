# WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');
import pandas as pd

# Sample DataFrame
data = {
    'CustomerName': [
        'George Wells', 'Gustavo Orosco', 'Giovanni Rizzo', 'Ana Trujillo Emparedados y helados', 
        'Antonio Moreno Taquería', 'Around the Horn', 'Gerry Greenspan', 'Rafael Rios'
    ],
    'City': [
        'Madrid', 'Barcelona', 'Seville', 'México D.F.', 'México D.F.', 'London', 'Madrid', 'Seville'
    ],
    'Country': [
        'Spain', 'Spain', 'Spain', 'Mexico', 'Mexico', 'UK', 'Spain', 'Spain'
    ]
}

df = pd.DataFrame(data)

# Filter the DataFrame where Country is 'Spain' and CustomerName starts with 'G' or 'R'
df_filtered = df[(df['Country'] == 'Spain') & 
                 ((df['CustomerName'].str.startswith('G')) | (df['CustomerName'].str.startswith('R')))]

# Display the filtered DataFrame
print(df_filtered)
