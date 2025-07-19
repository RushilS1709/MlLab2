import pandas as pd
import numpy as np

excel_file_path = "mllab1\Lab Session Data.xlsx"



df = pd.read_excel(excel_file_path,sheet_name='Purchase data')
print(df.head())

df['is_high'] = df['Payment (Rs)'] > 200


for i in range(len(df)):
    if df.loc[i,"Payment (Rs)"]>200:
        df.loc[i,"is_high"]="rich"
    else:
        df.loc[i,"is_high"]="poor"    

print(df)