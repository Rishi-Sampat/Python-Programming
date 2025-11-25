import pandas as pd
excel_file_path="E:\College\Python Programming\Lab_22\sample_data.xlsx"
df_excel=pd.read_excel(excel_file_path)

print("\nExcel Data:")
print(df_excel)

entry_count=df_excel.shape[0]
print("\nNumber of entries in Excel file:",entry_count)
