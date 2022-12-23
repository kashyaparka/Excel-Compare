import pandas as pd
import xlsxwriter as xls
import numpy as np
from pathlib import Path

url1 = 'files/ZSD0109_7125_20221129.xlsx'
url2 = 'files/ZSD0109_7125_20221128.xlsx'

file_name = Path(url1).name
xls1 = pd.ExcelFile(url1)
xls2 = pd.ExcelFile(url2)
t = xls1.sheet_names
with pd.ExcelWriter(file_name,engine='xlsxwriter') as writer:
    for i in range(len(t)):
        sheetname = t[i]
        df1 = pd.read_excel(xls1,t[i])
        df2 = pd.read_excel(xls2,t[i])
        df1.sort_values(by='SO No',inplace=True)
        df2.sort_values(by='SO No',inplace=True)
        a=[]
        for i in range(len(df1)):
            if df1.iloc[i].equals(df2.iloc[i]):
                a.append('False')
            else:
                a.append('True') 
        df1['Updated'] = a
        print(df1)
        df1.to_excel(writer,sheetname, index=False)

    
        