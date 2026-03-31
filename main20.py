import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Amdocs'],
    'Recruitments': [120, 150, 180, 90, 110, 95]
}

df = pd.DataFrame(data)


plt.bar(df['Company'], df['Recruitments'])
plt.title("Recruitments")
plt.show()


plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
plt.show()


plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
centre = plt.Circle((0,0),0.70,fc='white')
plt.gca().add_artist(centre)
plt.show()

comp = df[df['Company'].isin(['IBM','Amdocs'])]
plt.bar(comp['Company'], comp['Recruitments'])
plt.title("IBM vs Amdocs")
plt.show()