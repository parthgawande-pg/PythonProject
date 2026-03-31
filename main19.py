import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Line Plot (Total Profit)
plt.plot(df['month_number'], df['total_profit'])
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# Multiline Plot (All products)
for col in df.columns[1:-1]:
    plt.plot(df['month_number'], df[col], label=col)

plt.legend()
plt.title("Product Sales")
plt.show()

# Bar Chart (Face Cream vs Face Wash)
plt.bar(df['month_number'], df['facecream'], label='Face Cream')
plt.bar(df['month_number'], df['facewash'], label='Face Wash')
plt.legend()
plt.show()

# Pie Chart (Total sales per product)
total = df.iloc[:,1:-1].sum()
plt.pie(total, labels=total.index, autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.show()