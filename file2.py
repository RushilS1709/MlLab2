import pandas as pd
import numpy as np

excel_file_path = "mllab1\Lab Session Data.xlsx"



df = pd.read_excel(excel_file_path,sheet_name='Purchase data')
print(df.head())

df['high'] = df['Payment (Rs)'] > 200

for i in range(len(df)):
    if df.loc[i,"Payment (Rs)"]>200:
        df.loc[i,"high"]="Rich"
    else:
        df.loc[i,"high"]="Poor"    

print(df)
