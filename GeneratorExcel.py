import pandas as pd

df = pd.read_csv("dataCSV.csv")
df.to_excel("dataExcel.xlsx")