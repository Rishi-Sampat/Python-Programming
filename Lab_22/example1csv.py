import pandas as pd
csv_file_path=r"E:\College\Python Programming\Lab_22\sample_data.csv"
df_csv=pd.read_csv(csv_file_path)
print("CSV Data:")
print(df_csv)

filtered_data=df_csv[df_csv['Age']>30]
print("\nFiltered Data (Age>30):")
print(filtered_data)
