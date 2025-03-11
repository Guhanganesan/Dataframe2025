import pandas as pd 
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)
"""
   0
0  1
1  2
2  3
3  4
4  5
"""

#Add Columns
data=[["Raja",23],["Anbu",22],["Siva",25]]
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)
"""
   Name  Age
0  Raja   23
1  Anbu   22
2  Siva   25
"""


#Change the data type
data=[["Raja",23],["Anbu",22],["Siva",25]]
df=pd.DataFrame(data,columns=["Name","Age"], dtype=float)
print(df)
"""
   Name   Age
0  Raja  23.0
1  Anbu  22.0
2  Siva  25.0
"""

#Dict of ndarrays
data={"Name":["Raja","Anbu","Siva"], "Age":[23,22,25]}
df=pd.DataFrame(data)
print(df)
"""
   Name  Age
0  Raja   23
1  Anbu   22
2  Siva   25
"""

#indexed DataFrame
data={"Name":["Raja","Anbu","Siva"], 
       "Age":[23,22,25]}
df=pd.DataFrame(data, index=["I","II","III"])
print(df)
"""
     Name  Age
I    Raja   23
II   Anbu   22
III  Siva   25
"""

#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data)
print(df)
"""
   Name  Age     Mobile
0  Anbu   22  7623873.0
1  Raja   23        NaN
2  Siva   24  9878967.0

NaN, standing for not a number, is a member of a numeric data type that can be interpreted as 
a value that is undefined or unrepresentable, especially in floating-point arithmetic.
"""

#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data, index=["Rank1","Rank2","Rank3"] , 
   columns=["Name","Age","Mobile Number"] ) # wrong column name
print(df)
"""
       Name  Age  Mobile Number
Rank1  Anbu   22            NaN
Rank2  Raja   23            NaN
Rank3  Siva   24            NaN
"""

data={
      "Name":pd.Series(["Arun","Kanna","Kesav"],  
                index=[1,2,3]),
      "Age":pd.Series([22,24,23],  
                index=[1,2,4])
}
df=pd.DataFrame(data)
print(df)
"""
    Name   Age
1   Arun  22.0
2  Kanna  24.0
3  Kesav   NaN
4    NaN  23.0
"""

print(df["Name"])
"""
1     Arun
2    Kanna
3    Kesav
4      NaN
"""

#Add a new column
df["Mobile"]=pd.Series([627732,732737,547547],
             index=[1,2,3])
print(df)
"""
    Name   Age    Mobile
1   Arun  22.0  627732.0
2  Kanna  24.0  732737.0
3  Kesav   NaN  547547.0
4    NaN  23.0       NaN
""" 

#Delete column
del df["Mobile"]
print(df)
"""
    Name   Age
1   Arun  22.0
2  Kanna  24.0
3  Kesav   NaN
4    NaN  23.0
"""