import pandas as pd

df = pd.read_csv('test_nz.csv')

df.to_xml('probar.xml')
#print(df.to_string())