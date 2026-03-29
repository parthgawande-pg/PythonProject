import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Data:\n")
print(df)

author = input("Enter author name: ")
print("\nBooks by author:\n")
print(df[df['author'] == author])

pub = input("Enter publishing house: ")
print("\nBooks by publisher:\n")
print(df[df['publisher'] == pub])

print("\nCheapest Book:\n")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:\n")
print(df.loc[df['price'].idxmax()])

print("\nSorted by Year:\n")
print(df.sort_values(by='year'))