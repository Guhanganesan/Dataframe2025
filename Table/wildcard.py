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

# 1. Using `%` wildcard (Any characters, similar to SQL's `LIKE '%A%'`):
print("=== Using Wildcard '%A%' (contains 'A') ===")
contains_A_df = df[df['CustomerName'].str.contains('A', case=False)]  # Case insensitive
print(contains_A_df)

print("\n")

# 2. Using `_` wildcard (Exactly one character, similar to SQL's `LIKE '_A%'`):
print("=== Using Wildcard '_A%' (second character is 'A') ===")
second_char_is_A_df = df[df['CustomerName'].str.match('^._A', na=False)]  # Second character is 'A'
print(second_char_is_A_df)

print("\n")

# 3. Using `LIKE 'A%'` (starts with 'A')
print("=== Using Wildcard 'A%' (starts with 'A') ===")
starts_with_A_df = df[df['CustomerName'].str.startswith('A')]  # Starts with 'A'
print(starts_with_A_df)

print("\n")

# 4. Using `LIKE '%A'` (ends with 'A')
print("=== Using Wildcard '%A' (ends with 'A') ===")
ends_with_A_df = df[df['CustomerName'].str.endswith('A')]  # Ends with 'A'
print(ends_with_A_df)

print("\n")

# 5. Using `LIKE '_A%'` (second character is 'A')
print("=== Using Wildcard '_A%' (second character is 'A') ===")
second_character_is_A_df = df[df['CustomerName'].str.match('^._A', na=False)]  # Second character is 'A'
print(second_character_is_A_df)


# === Using Wildcard '%A%' (contains 'A') ===
#    CustomerID                        CustomerName         ContactName                      Address          City PostalCode  Country
# 0           1            Alfreds Futterkiste       Maria Anders            Obere Str. 57         Berlin       12209   Germany
# 1           2  Ana Trujillo Emparedados y helados    Ana Trujillo    Avda. de la Constitución 2222   México D.F.       05021   Mexico
# 2           3         Antonio Moreno Taquería      Antonio Moreno           Mataderos 2314     México D.F.       05023   Mexico


# === Using Wildcard '_A%' (second character is 'A') ===
#    CustomerID                        CustomerName         ContactName                      Address          City PostalCode  Country
# 0           1            Alfreds Futterkiste       Maria Anders            Obere Str. 57         Berlin       12209   Germany
# 1           2  Ana Trujillo Emparedados y helados    Ana Trujillo    Avda. de la Constitución 2222   México D.F.       05021   Mexico
# 2           3         Antonio Moreno Taquería      Antonio Moreno           Mataderos 2314     México D.F.       05023   Mexico


# === Using Wildcard 'A%' (starts with 'A') ===
#    CustomerID                        CustomerName       ContactName                      Address          City PostalCode  Country
# 0           1            Alfreds Futterkiste       Maria Anders            Obere Str. 57         Berlin       12209   Germany
# 1           2  Ana Trujillo Emparedados y helados    Ana Trujillo    Avda. de la Constitución 2222   México D.F.       05021   Mexico
# 2           3         Antonio Moreno Taquería      Antonio Moreno           Mataderos 2314     México D.F.       05023   Mexico


# === Using Wildcard '%A' (ends with 'A') ===
#    CustomerID                        CustomerName      ContactName                      Address          City PostalCode  Country
# 3           4                      Cardinal      Tom B. Erichsen                    Skagen 21     Stavanger       4006    Norway


# === Using Wildcard '_A%' (second character is 'A') ===
#    CustomerID                        CustomerName         ContactName                      Address          City PostalCode  Country
# 0           1            Alfreds Futterkiste       Maria Anders            Obere Str. 57         Berlin       12209   Germany
# 1           2  Ana Trujillo Emparedados y helados    Ana Trujillo    Avda. de la Constitución 2222   México D.F.       05021   Mexico
# 2           3         Antonio Moreno Taquería      Antonio Moreno           Mataderos 2314     México D.F.       05023   Mexico
