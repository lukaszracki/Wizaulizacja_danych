import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

df = pd.read_excel('imiona.xlsx')
df2 = pd.read_csv('zamowienia.csv', sep=';')

#zadanie 1
# ts = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(ts)
# ts.plot()
# plt.xticks(df['Rok'].unique())
# plt.xticks(rotation=90)
# plt.show()

#zadanie 2
# ts = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(ts)
# ts.plot.bar()
# plt.show()

#zadanie 3
# ts = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(ts)
# ts.plot.pie(subplots=True, autopct='%.2f%%')
# plt.show()

#zadanie 4
# ts = df2.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
# print(ts)
# ts.plot.bar()
# plt.show()
