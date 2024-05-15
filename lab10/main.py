import numpy as np
import pandas as pd

# zadanie 1
df = pd.read_excel('imiona.xlsx')

# zadanie 2

df_over_1000 = df[df['Liczba'] > 1000]
# print({df_over_1000})

df_Lukasz = df[df['Imie'] == 'ŁUKASZ']
# print(df_Lukasz)

suma_urodzonych = df['Liczba'].sum()
# print(f'Suma urodzonych dzieci: {suma_urodzonych}')

suma_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()
# print(f'Suma urodzonych w latach 2000-2005: {suma_2000_2005}')

suma_ch_i_d = df.groupby('Plec')['Liczba'].sum()
#print(suma_ch_i_d)

popular_names = df.sort_values(by='Liczba', ascending=False).groupby(['Rok', 'Plec']).head(1)
# print(popular_names)


#zadanie 3

df2 = pd.read_csv('zamowienia.csv', sep=';')
# print(df2['Sprzedawca'].unique())
# print(df2.sort_values(by='Utarg', ascending=False).head(5))
print(df2.groupby('Kraj').count('idZamowienia'))