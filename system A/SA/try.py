import pandas as pds
from nest_asyncio import apply

df = pds.read_excel('try.xlsx', sheet_name=1)

def print_main():
    pass

print(df.columns)
print('\n')
print(df.select_dtypes(include='int'))
print('\n')
print(df.select_dtypes(include='object'))