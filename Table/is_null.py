import pandas as pd
import numpy as np

# Sample DataFrame with some 'NaN' values in the Address column
data = {
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Cardinal'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Tom B. Erichsen'],
    'Address': ['Obere Str. 57', np.nan, 'Mataderos 2314', np.nan],
    'City': ['Berlin', 'México D.F.', 'México D.F.', 'Stavanger'],
    'PostalCode': ['12209', '05021', '05023', '4006'],
    'Country': ['Germany', 'Mexico', 'Mexico', 'Norway']
}

df = pd.DataFrame(data)

# Filter rows where Address is NaN (NULL in SQL)
df_filtered = df[df['Address'].isna()]

# Display the filtered DataFrame
print(df_filtered)
