import pandas as pd
import os

os.chdir('files')

data = pd.read_excel('titanic_train.xlsx')

print(data.loc[4:9, ['PassengerId', 'Survived', 'Pclass']])

print('#######')

print('Średnia wieku pasażerów statku: {}'.format(round(data.loc[0:, 'Age'].mean(), 2)))

print('Ilość osób, która przeżyła katastrofe: {}'.format(data.loc[0:, 'Survived'].sum()))

print('Statystyki podstawowe dla 2 grup: {}'.format(data.groupby('Sex').describe()))

print('Statystyki podstawowe klas pasażerów: {}'.format(data.groupby('Pclass').count()))
 