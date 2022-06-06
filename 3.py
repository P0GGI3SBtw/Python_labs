import pandas as pd
import os

os.chdir('files')

data = pd.read_excel('titanic_train.xlsx')

print(data.Age.min())

print('3)')
print(data.iloc[[2, 4, 30], 3:6])
