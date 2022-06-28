import pandas as pd
import numpy as np

# Creating a dataframe and saving as test.csv in current directory
df = pd.DataFrame(np.random.randn(100000, 3), columns=list('ABC'))
df.to_csv('data.csv', index = False)

# Reading in test.csv and saving as test.xlsx

df_new = pd.read_csv('data.csv')
writer = pd.ExcelWriter('data.xlsx')
df_new.to_excel(writer, index = False)
writer.save()
