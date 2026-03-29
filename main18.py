import pandas as pd

data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'UP', 'MP'],
    'Area': [307713, 196024, 342239, 240928, 308245],
    'Population': [124000000, 70000000, 81000000, 230000000, 85000000]
}

df = pd.DataFrame(data)

print("\nAll States Data:\n")
print(df)

print("\nState with Largest Area:\n")
print(df.loc[df['Area'].idxmax()])

print("\nState with Largest Population:\n")
print(df.loc[df['Population'].idxmax()])

df['Density'] = df['Population'] / df['Area']

print("\nPopulation Density:\n")
print(df[['State', 'Density']])

print("\nState with Highest Density:\n")
print(df.loc[df['Density'].idxmax()])