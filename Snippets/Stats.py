import os
import numpy as np
import pandas as pd

cwd = os.getcwd()
os.chdir('/Users/usreei/Desktop')
os.listdir('.')
file = 'gamestats.xlsx'
xlsx = pd.ExcelFile(file)
# print(xl.sheet_names)
df1 = pd.read_excel(xlsx, 'Sheet1')

df2 = df1.set_index(['Deck Used'])
df3 = df1.set_index(['Deck Against'])

# print(df6.sum())
# print(df7.sum())

# print(df1.columns)
df4 = df1.columns


def Grouper():
    for i in df4:
        if i == 'Win':
            continue
        elif i == 'Loss':
            continue
        group = df1.set_index([i])
        group['Played'] = group['Win'] + group['Loss']
        group['Win Rate'] = group['Win'] / group['Played'] * 100
        print(group.round({'Win Rate': 2}))
        print('\n')


##Grouper()

print(df1.groupby('Deck Used')['Deck Against'].value_counts())


df5 = df1['Deck Used'].unique()
print(df5)
def DeckGrouper():
    for i in df5:
        if i == 'Win':
            continue
        elif i == 'Loss':
            continue
        group = df1.groupby([i])
        group['Played'] = group['Win'] + group['Loss']
        group['Win Rate'] = group['Win'] / group['Played'] * 100
        print(group.round({'Win Rate': 2}))
        print('\n')


DeckGrouper()